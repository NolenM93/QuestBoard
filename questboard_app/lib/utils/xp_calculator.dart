import 'package:questboard_app/models/quest.dart';
import 'package:questboard_app/models/achievement.dart';
import 'package:questboard_app/models/user.dart';

/// XP Calculator utility for consistent XP calculations across the app
class XPCalculator {
  /// Calculate XP reward for completing a quest
  static int calculateQuestXP(Quest quest) {
    int baseXP = Quest.getXPForDifficulty(quest.difficulty);
    
    // Bonus for completing all steps
    if (quest.steps.isNotEmpty) {
      final allStepsComplete = quest.steps.every((step) => step.isCompleted);
      if (allStepsComplete) {
        baseXP = (baseXP * 1.1).round();
      }
    }
    
    // Bonus for completing before due date
    if (quest.dueDate != null && quest.completedAt != null) {
      if (quest.completedAt!.isBefore(quest.dueDate!)) {
        final daysEarly = quest.dueDate!.difference(quest.completedAt!).inDays;
        if (daysEarly > 0) {
          baseXP = (baseXP * (1 + (daysEarly * 0.05))).round();
        }
      }
    }
    
    return baseXP;
  }
  
  /// Calculate XP required for next user level
  static int xpForNextLevel(int currentLevel) {
    return currentLevel * 100;
  }
  
  /// Calculate total XP required to reach a specific level
  static int totalXPForLevel(int level) {
    int total = 0;
    for (int i = 1; i < level; i++) {
      total += xpForNextLevel(i);
    }
    return total;
  }
  
  /// Calculate current level from total XP
  static int levelFromXP(int totalXP) {
    int level = 1;
    int xpNeeded = 0;
    
    while (xpNeeded <= totalXP) {
      xpNeeded += xpForNextLevel(level);
      if (xpNeeded <= totalXP) {
        level++;
      }
    }
    
    return level;
  }
  
  /// Calculate progress to next level (0.0 to 1.0)
  static double progressToNextLevel(int totalXP) {
    final currentLevel = levelFromXP(totalXP);
    final xpAtCurrentLevel = totalXPForLevel(currentLevel);
    final xpForNext = xpForNextLevel(currentLevel);
    final currentProgress = totalXP - xpAtCurrentLevel;
    
    return (currentProgress / xpForNext).clamp(0.0, 1.0);
  }
  
  /// Calculate team XP bonus (teams get bonus XP)
  static int calculateTeamXPBonus(int baseXP, int teamSize) {
    // 5% bonus per team member (max 50%)
    final bonusMultiplier = (teamSize * 0.05).clamp(0, 0.5);
    return (baseXP * bonusMultiplier).round();
  }
  
  /// Calculate streak bonus XP
  static int calculateStreakBonus(int baseXP, int streakDays) {
    // 2% bonus per day of streak (max 100%)
    final bonusMultiplier = (streakDays * 0.02).clamp(0, 1.0);
    return (baseXP * bonusMultiplier).round();
  }
  
  /// Calculate XP for achieving an achievement
  static int calculateAchievementXP(Achievement achievement) {
    return Achievement.getXPForTier(achievement.tier);
  }
  
  /// Calculate mascot level from experience
  static int mascotLevelFromXP(int experience) {
    return (experience / 50).floor() + 1;
  }
  
  /// Calculate XP needed for mascot's next level
  static int mascotXPForNextLevel(int currentLevel) {
    return currentLevel * 50;
  }
  
  /// Get skill points based on quest type
  static Map<String, int> calculateSkillPoints(Quest quest) {
    Map<String, int> points = {};
    
    switch (quest.type) {
      case QuestType.brainstorm:
        points['creativity'] = 5;
        points['planning'] = 3;
        break;
      case QuestType.build:
        points['coding'] = 8;
        points['problem_solving'] = 5;
        break;
      case QuestType.promote:
        points['communication'] = 7;
        points['marketing'] = 5;
        break;
      case QuestType.research:
        points['analysis'] = 6;
        points['documentation'] = 4;
        break;
      case QuestType.test:
        points['quality_assurance'] = 7;
        points['attention_to_detail'] = 5;
        break;
      case QuestType.review:
        points['collaboration'] = 6;
        points['feedback'] = 5;
        break;
      case QuestType.learn:
        points['learning'] = 8;
        points['adaptation'] = 4;
        break;
    }
    
    // Difficulty multiplier
    final multiplier = _getDifficultyMultiplier(quest.difficulty);
    points.updateAll((key, value) => (value * multiplier).round());
    
    return points;
  }
  
  static double _getDifficultyMultiplier(QuestDifficulty difficulty) {
    switch (difficulty) {
      case QuestDifficulty.easy:
        return 1.0;
      case QuestDifficulty.medium:
        return 1.5;
      case QuestDifficulty.hard:
        return 2.0;
      case QuestDifficulty.epic:
        return 3.0;
    }
  }
  
  /// Calculate leaderboard score (combination of XP, achievements, and activity)
  static int calculateLeaderboardScore(User user, int questsCompleted, int daysActive) {
    int score = user.totalXP;
    score += user.achievementIds.length * 50;
    score += questsCompleted * 25;
    score += daysActive * 10;
    
    return score;
  }
}
