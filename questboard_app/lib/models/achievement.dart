import 'package:hive/hive.dart';

part 'achievement.g.dart';

@HiveType(typeId: 7)
enum AchievementType {
  @HiveField(0)
  contribution,
  @HiveField(1)
  leadership,
  @HiveField(2)
  creativity,
  @HiveField(3)
  consistency,
  @HiveField(4)
  collaboration,
  @HiveField(5)
  milestone,
  @HiveField(6)
  special,
}

@HiveType(typeId: 8)
enum BadgeTier {
  @HiveField(0)
  bronze,
  @HiveField(1)
  silver,
  @HiveField(2)
  gold,
  @HiveField(3)
  platinum,
  @HiveField(4)
  diamond,
}

@HiveType(typeId: 9)
class Achievement extends HiveObject {
  @HiveField(0)
  final String id;

  @HiveField(1)
  final String title;

  @HiveField(2)
  final String description;

  @HiveField(3)
  final AchievementType type;

  @HiveField(4)
  final BadgeTier tier;

  @HiveField(5)
  final String iconUrl;

  @HiveField(6)
  final int xpReward;

  @HiveField(7)
  final Map<String, dynamic> criteria;

  @HiveField(8)
  final bool isHidden;

  @HiveField(9)
  final String? seasonId;

  Achievement({
    required this.id,
    required this.title,
    required this.description,
    required this.type,
    required this.tier,
    required this.iconUrl,
    required this.xpReward,
    required this.criteria,
    this.isHidden = false,
    this.seasonId,
  });

  Achievement copyWith({
    String? id,
    String? title,
    String? description,
    AchievementType? type,
    BadgeTier? tier,
    String? iconUrl,
    int? xpReward,
    Map<String, dynamic>? criteria,
    bool? isHidden,
    String? seasonId,
  }) {
    return Achievement(
      id: id ?? this.id,
      title: title ?? this.title,
      description: description ?? this.description,
      type: type ?? this.type,
      tier: tier ?? this.tier,
      iconUrl: iconUrl ?? this.iconUrl,
      xpReward: xpReward ?? this.xpReward,
      criteria: criteria ?? this.criteria,
      isHidden: isHidden ?? this.isHidden,
      seasonId: seasonId ?? this.seasonId,
    );
  }

  static String getColorForTier(BadgeTier tier) {
    switch (tier) {
      case BadgeTier.bronze:
        return '#CD7F32';
      case BadgeTier.silver:
        return '#C0C0C0';
      case BadgeTier.gold:
        return '#FFD700';
      case BadgeTier.platinum:
        return '#E5E4E2';
      case BadgeTier.diamond:
        return '#B9F2FF';
    }
  }

  static int getXPForTier(BadgeTier tier) {
    switch (tier) {
      case BadgeTier.bronze:
        return 50;
      case BadgeTier.silver:
        return 100;
      case BadgeTier.gold:
        return 200;
      case BadgeTier.platinum:
        return 400;
      case BadgeTier.diamond:
        return 800;
    }
  }
}

@HiveType(typeId: 10)
class UserAchievement extends HiveObject {
  @HiveField(0)
  final String achievementId;

  @HiveField(1)
  final String userId;

  @HiveField(2)
  final DateTime unlockedAt;

  @HiveField(3)
  final double progress;

  @HiveField(4)
  final bool isCompleted;

  UserAchievement({
    required this.achievementId,
    required this.userId,
    required this.unlockedAt,
    this.progress = 0.0,
    this.isCompleted = false,
  });

  UserAchievement copyWith({
    String? achievementId,
    String? userId,
    DateTime? unlockedAt,
    double? progress,
    bool? isCompleted,
  }) {
    return UserAchievement(
      achievementId: achievementId ?? this.achievementId,
      userId: userId ?? this.userId,
      unlockedAt: unlockedAt ?? this.unlockedAt,
      progress: progress ?? this.progress,
      isCompleted: isCompleted ?? this.isCompleted,
    );
  }
}
