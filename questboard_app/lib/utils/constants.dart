import 'package:flutter/material.dart';

/// Constants for color schemes used throughout the app
class AppColors {
  // Primary Brand Colors
  static const Color primary = Color(0xFF6C5CE7);
  static const Color primaryDark = Color(0xFF5F3DC4);
  static const Color primaryLight = Color(0xFF9B8DE8);
  
  static const Color secondary = Color(0xFF00D2D3);
  static const Color secondaryDark = Color(0xFF00A8A9);
  static const Color secondaryLight = Color(0xFF4DECEC);
  
  // Quest Type Colors
  static const Color brainstorm = Color(0xFFFF6B35);
  static const Color build = Color(0xFF4ECDC4);
  static const Color promote = Color(0xFF45B7D1);
  static const Color research = Color(0xFF96CEB4);
  static const Color test = Color(0xFFFFEAA7);
  static const Color review = Color(0xFFDDA0DD);
  static const Color learn = Color(0xFFFFB6C1);
  
  // Badge Tier Colors
  static const Color bronze = Color(0xFFCD7F32);
  static const Color silver = Color(0xFFC0C0C0);
  static const Color gold = Color(0xFFFFD700);
  static const Color platinum = Color(0xFFE5E4E2);
  static const Color diamond = Color(0xFFB9F2FF);
  
  // Status Colors
  static const Color success = Color(0xFF00B894);
  static const Color warning = Color(0xFFFDCB6E);
  static const Color error = Color(0xFFFF7675);
  static const Color info = Color(0xFF74B9FF);
  
  // Difficulty Colors
  static const Color difficultyEasy = Color(0xFF55EFC4);
  static const Color difficultyMedium = Color(0xFFFDCB6E);
  static const Color difficultyHard = Color(0xFFFF7675);
  static const Color difficultyEpic = Color(0xFFD63031);
  
  // Neutral Colors
  static const Color backgroundLight = Color(0xFFF5F6FA);
  static const Color backgroundDark = Color(0xFF2D3436);
  static const Color cardLight = Color(0xFFFFFFFF);
  static const Color cardDark = Color(0xFF353B48);
  static const Color textPrimary = Color(0xFF2D3436);
  static const Color textSecondary = Color(0xFF636E72);
  static const Color textLight = Color(0xFFB2BEC3);
  
  // Mascot Mood Colors
  static const Color moodHappy = Color(0xFFFDCB6E);
  static const Color moodExcited = Color(0xFFFF6B6B);
  static const Color moodFocused = Color(0xFF4ECDC4);
  static const Color moodTired = Color(0xFF95A5A6);
  static const Color moodCelebrating = Color(0xFFF39C12);
  static const Color moodThinking = Color(0xFF9B59B6);
  static const Color moodSleeping = Color(0xFF7F8C8D);
}

/// Text styles used throughout the app
class AppTextStyles {
  static const String fontFamily = 'Poppins';
  
  // Headings
  static const TextStyle h1 = TextStyle(
    fontSize: 32,
    fontWeight: FontWeight.bold,
    fontFamily: fontFamily,
    letterSpacing: -0.5,
  );
  
  static const TextStyle h2 = TextStyle(
    fontSize: 28,
    fontWeight: FontWeight.bold,
    fontFamily: fontFamily,
    letterSpacing: -0.5,
  );
  
  static const TextStyle h3 = TextStyle(
    fontSize: 24,
    fontWeight: FontWeight.bold,
    fontFamily: fontFamily,
  );
  
  static const TextStyle h4 = TextStyle(
    fontSize: 20,
    fontWeight: FontWeight.w600,
    fontFamily: fontFamily,
  );
  
  // Body Text
  static const TextStyle bodyLarge = TextStyle(
    fontSize: 16,
    fontWeight: FontWeight.normal,
    fontFamily: fontFamily,
  );
  
  static const TextStyle bodyMedium = TextStyle(
    fontSize: 14,
    fontWeight: FontWeight.normal,
    fontFamily: fontFamily,
  );
  
  static const TextStyle bodySmall = TextStyle(
    fontSize: 12,
    fontWeight: FontWeight.normal,
    fontFamily: fontFamily,
  );
  
  // Special Text
  static const TextStyle button = TextStyle(
    fontSize: 16,
    fontWeight: FontWeight.w600,
    fontFamily: fontFamily,
    letterSpacing: 0.5,
  );
  
  static const TextStyle caption = TextStyle(
    fontSize: 12,
    fontWeight: FontWeight.normal,
    fontFamily: fontFamily,
    color: AppColors.textSecondary,
  );
  
  static const TextStyle xpBadge = TextStyle(
    fontSize: 14,
    fontWeight: FontWeight.bold,
    fontFamily: fontFamily,
    color: Colors.white,
  );
}

/// Spacing constants
class AppSpacing {
  static const double xs = 4.0;
  static const double sm = 8.0;
  static const double md = 16.0;
  static const double lg = 24.0;
  static const double xl = 32.0;
  static const double xxl = 48.0;
}

/// Border radius constants
class AppRadius {
  static const double sm = 8.0;
  static const double md = 12.0;
  static const double lg = 16.0;
  static const double xl = 24.0;
  static const double full = 999.0;
}

/// Animation durations
class AppDurations {
  static const Duration fast = Duration(milliseconds: 200);
  static const Duration medium = Duration(milliseconds: 300);
  static const Duration slow = Duration(milliseconds: 500);
  static const Duration xpAnimation = Duration(milliseconds: 1000);
}

/// App-wide constants
class AppConstants {
  static const String appName = 'QuestBoard';
  static const String appTagline = 'Gamified Team Progress Tracker';
  static const int maxTeamMembers = 20;
  static const int maxQuestTitleLength = 100;
  static const int maxQuestDescriptionLength = 500;
  static const int maxTeamNameLength = 50;
  static const int baseXPForLevel = 100;
  static const int mascotLevelUpXP = 50;
}
