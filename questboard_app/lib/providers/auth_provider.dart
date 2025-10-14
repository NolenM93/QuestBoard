import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:questboard_app/models/user.dart';
import 'package:questboard_app/services/auth_service.dart';

final authServiceProvider = Provider<AuthService>((ref) {
  return AuthService();
});

final currentUserProvider = StateNotifierProvider<CurrentUserNotifier, AsyncValue<User?>>((ref) {
  return CurrentUserNotifier(ref.watch(authServiceProvider));
});

class CurrentUserNotifier extends StateNotifier<AsyncValue<User?>> {
  final AuthService _authService;

  CurrentUserNotifier(this._authService) : super(const AsyncValue.loading()) {
    _loadUser();
  }

  Future<void> _loadUser() async {
    try {
      await _authService.initialize();
      
      final user = _authService.getCurrentUser();
      
      state = AsyncValue.data(user);
    } catch (e, stack) {
      state = AsyncValue.error(e, stack);
    }
  }

  Future<void> login(String email, String password) async {
    state = const AsyncValue.loading();
    try {
      final user = await _authService.login(email, password);
      state = AsyncValue.data(user);
    } catch (e, stack) {
      state = AsyncValue.error(e, stack);
      rethrow;
    }
  }

  Future<void> signup(String username, String email, String password) async {
    state = const AsyncValue.loading();
    try {
      final user = await _authService.signup(username, email, password);
      state = AsyncValue.data(user);
    } catch (e, stack) {
      state = AsyncValue.error(e, stack);
      rethrow;
    }
  }

  Future<void> logout() async {
    await _authService.logout();
    state = const AsyncValue.data(null);
  }

  Future<void> updateUser(User user) async {
    await _authService.updateUser(user);
    state = AsyncValue.data(user);
  }

  void refresh() {
    final user = _authService.getCurrentUser();
    state = AsyncValue.data(user);
  }
}
