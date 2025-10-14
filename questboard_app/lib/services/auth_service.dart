import 'package:hive_flutter/hive_flutter.dart';
import 'package:questboard_app/models/user.dart';
import 'package:uuid/uuid.dart';

class AuthService {
  static const String _userBoxName = 'users';
  static const String _currentUserKey = 'current_user_id';
  
  Box? _userBox;
  Box? _prefsBox;

  Future<void> initialize() async {
    _userBox = await Hive.openBox(_userBoxName);
    _prefsBox = await Hive.openBox('prefs');
  }

  User _userFromMap(Map<dynamic, dynamic> map) {
    return User(
      id: map['id'] as String,
      username: map['username'] as String,
      email: map['email'] as String,
      avatarUrl: map['avatarUrl'] as String? ?? '',
      totalXP: map['totalXP'] as int? ?? 0,
      level: map['level'] as int? ?? 1,
      achievementIds: List<String>.from(map['achievementIds'] as List? ?? []),
      joinDate: DateTime.parse(map['joinDate'] as String),
      teamId: map['teamId'] as String?,
      skillPoints: Map<String, int>.from(map['skillPoints'] as Map? ?? {}),
      preferences: UserPreferences(
        enableNotifications: map['preferences']?['enableNotifications'] as bool? ?? true,
        enableSounds: map['preferences']?['enableSounds'] as bool? ?? true,
        theme: map['preferences']?['theme'] as String? ?? 'auto',
        mascotSkin: map['preferences']?['mascotSkin'] as String? ?? 'default',
      ),
    );
  }

  Map<String, dynamic> _userToMap(User user) {
    return {
      'id': user.id,
      'username': user.username,
      'email': user.email,
      'avatarUrl': user.avatarUrl,
      'totalXP': user.totalXP,
      'level': user.level,
      'achievementIds': user.achievementIds,
      'joinDate': user.joinDate.toIso8601String(),
      'teamId': user.teamId,
      'skillPoints': user.skillPoints,
      'preferences': {
        'enableNotifications': user.preferences.enableNotifications,
        'enableSounds': user.preferences.enableSounds,
        'theme': user.preferences.theme,
        'mascotSkin': user.preferences.mascotSkin,
      },
    };
  }

  Future<User?> login(String email, String password) async {
    await Future.delayed(const Duration(milliseconds: 500)); // Simulate API call
    
    
    // Check if user exists
    final userMaps = _userBox!.values.cast<Map>();
    final matchingUsers = userMaps.where((map) => map['email'] == email);
    
    
    if (matchingUsers.isEmpty) {
      throw Exception('User not found. Please sign up first.');
    }
    
    final user = _userFromMap(matchingUsers.first);
    
    // In production, verify password hash
    await _prefsBox!.put(_currentUserKey, user.id);
    
    return user;
  }

  Future<User> signup(String username, String email, String password) async {
    try {
      await Future.delayed(const Duration(milliseconds: 500)); // Simulate API call
      
      
      // Check if email already exists
      final userMaps = _userBox!.values.cast<Map>();
      final existingUsers = userMaps.where((map) => map['email'] == email);
      if (existingUsers.isNotEmpty) {
        throw Exception('Email already registered');
      }
      
      // Create new user
      final user = User(
        id: const Uuid().v4(),
        username: username,
        email: email,
        totalXP: 0,
        level: 1,
        achievementIds: [],
        joinDate: DateTime.now(),
        skillPoints: const {},
        preferences: UserPreferences(
          enableNotifications: true,
          enableSounds: true,
          theme: 'auto',
          mascotSkin: 'default',
        ),
      );
      
      final userMap = _userToMap(user);
      
      await _userBox!.put(user.id, userMap);
      
      await _prefsBox!.put(_currentUserKey, user.id);
      
      return user;
    } catch (e) {
      rethrow;
    }
  }

  Future<void> logout() async {
    await _prefsBox!.delete(_currentUserKey);
  }

  User? getCurrentUser() {
    final userId = _prefsBox?.get(_currentUserKey);
    
    if (userId == null) {
      return null;
    }
    
    final userMap = _userBox?.get(userId);
    
    if (userMap == null) {
      return null;
    }
    
    try {
      final user = _userFromMap(userMap as Map);
      return user;
    } catch (e) {
      return null;
    }
  }

  Future<void> updateUser(User user) async {
    await _userBox!.put(user.id, _userToMap(user));
  }

  bool get isLoggedIn {
    return _prefsBox?.get(_currentUserKey) != null;
  }
}
