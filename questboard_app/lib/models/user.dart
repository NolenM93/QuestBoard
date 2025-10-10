import 'package:hive/hive.dart';

part 'user.g.dart';

@HiveType(typeId: 0)
class User extends HiveObject {
  @HiveField(0)
  final String id;

  @HiveField(1)
  final String username;

  @HiveField(2)
  final String email;

  @HiveField(3)
  final String avatarUrl;

  @HiveField(4)
  final int totalXP;

  @HiveField(5)
  final int level;

  @HiveField(6)
  final List<String> achievementIds;

  @HiveField(7)
  final DateTime joinDate;

  @HiveField(8)
  final String? teamId;

  @HiveField(9)
  final Map<String, int> skillPoints;

  @HiveField(10)
  final UserPreferences preferences;

  User({
    required this.id,
    required this.username,
    required this.email,
    this.avatarUrl = '',
    this.totalXP = 0,
    this.level = 1,
    this.achievementIds = const [],
    required this.joinDate,
    this.teamId,
    this.skillPoints = const {},
    required this.preferences,
  });

  User copyWith({
    String? id,
    String? username,
    String? email,
    String? avatarUrl,
    int? totalXP,
    int? level,
    List<String>? achievementIds,
    DateTime? joinDate,
    String? teamId,
    Map<String, int>? skillPoints,
    UserPreferences? preferences,
  }) {
    return User(
      id: id ?? this.id,
      username: username ?? this.username,
      email: email ?? this.email,
      avatarUrl: avatarUrl ?? this.avatarUrl,
      totalXP: totalXP ?? this.totalXP,
      level: level ?? this.level,
      achievementIds: achievementIds ?? this.achievementIds,
      joinDate: joinDate ?? this.joinDate,
      teamId: teamId ?? this.teamId,
      skillPoints: skillPoints ?? this.skillPoints,
      preferences: preferences ?? this.preferences,
    );
  }

  static int calculateLevel(int xp) {
    return (xp / 100).floor() + 1;
  }

  int get xpForNextLevel => (level * 100) - totalXP;
}

@HiveType(typeId: 1)
class UserPreferences extends HiveObject {
  @HiveField(0)
  final bool enableNotifications;

  @HiveField(1)
  final bool enableSounds;

  @HiveField(2)
  final String theme;

  @HiveField(3)
  final String mascotSkin;

  UserPreferences({
    this.enableNotifications = true,
    this.enableSounds = true,
    this.theme = 'auto',
    this.mascotSkin = 'default',
  });
}
