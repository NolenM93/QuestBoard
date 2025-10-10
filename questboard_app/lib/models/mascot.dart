import 'package:hive/hive.dart';

part 'mascot.g.dart';

@HiveType(typeId: 15)
enum MascotType {
  @HiveField(0)
  sloth,
  @HiveField(1)
  phoenix,
  @HiveField(2)
  dragon,
  @HiveField(3)
  unicorn,
  @HiveField(4)
  robot,
  @HiveField(5)
  cat,
  @HiveField(6)
  owl,
}

@HiveType(typeId: 16)
enum MascotMood {
  @HiveField(0)
  happy,
  @HiveField(1)
  excited,
  @HiveField(2)
  focused,
  @HiveField(3)
  tired,
  @HiveField(4)
  celebrating,
  @HiveField(5)
  thinking,
  @HiveField(6)
  sleeping,
}

@HiveType(typeId: 17)
class Mascot extends HiveObject {
  @HiveField(0)
  final String id;

  @HiveField(1)
  final String name;

  @HiveField(2)
  final MascotType type;

  @HiveField(3)
  final int level;

  @HiveField(4)
  final int experience;

  @HiveField(5)
  final MascotMood currentMood;

  @HiveField(6)
  final String skinId;

  @HiveField(7)
  final List<String> unlockedSkins;

  @HiveField(8)
  final Map<String, String> accessories;

  @HiveField(9)
  final MascotStats stats;

  @HiveField(10)
  final DateTime lastInteraction;

  @HiveField(11)
  final List<String> phrases;

  Mascot({
    required this.id,
    required this.name,
    required this.type,
    this.level = 1,
    this.experience = 0,
    this.currentMood = MascotMood.happy,
    this.skinId = 'default',
    this.unlockedSkins = const ['default'],
    this.accessories = const {},
    required this.stats,
    required this.lastInteraction,
    this.phrases = const [],
  });

  Mascot copyWith({
    String? id,
    String? name,
    MascotType? type,
    int? level,
    int? experience,
    MascotMood? currentMood,
    String? skinId,
    List<String>? unlockedSkins,
    Map<String, String>? accessories,
    MascotStats? stats,
    DateTime? lastInteraction,
    List<String>? phrases,
  }) {
    return Mascot(
      id: id ?? this.id,
      name: name ?? this.name,
      type: type ?? this.type,
      level: level ?? this.level,
      experience: experience ?? this.experience,
      currentMood: currentMood ?? this.currentMood,
      skinId: skinId ?? this.skinId,
      unlockedSkins: unlockedSkins ?? this.unlockedSkins,
      accessories: accessories ?? this.accessories,
      stats: stats ?? this.stats,
      lastInteraction: lastInteraction ?? this.lastInteraction,
      phrases: phrases ?? this.phrases,
    );
  }

  int get experienceForNextLevel => level * 50;

  String get evolutionStage {
    if (level < 5) return 'Baby';
    if (level < 15) return 'Young';
    if (level < 30) return 'Adult';
    if (level < 50) return 'Elder';
    return 'Legendary';
  }

  bool get needsAttention {
    final hoursSinceInteraction = DateTime.now().difference(lastInteraction).inHours;
    return hoursSinceInteraction > 24;
  }

  List<String> getPhrasesForMood() {
    switch (currentMood) {
      case MascotMood.happy:
        return [
          "Great job on that quest!",
          "You're doing amazing!",
          "Keep up the fantastic work!",
        ];
      case MascotMood.excited:
        return [
          "Wow! That was incredible!",
          "Let's tackle the next challenge!",
          "I'm so pumped for this quest!",
        ];
      case MascotMood.focused:
        return [
          "Let's concentrate on this task.",
          "Focus mode: activated!",
          "Time to get things done!",
        ];
      case MascotMood.tired:
        return [
          "Maybe it's time for a break?",
          "Don't forget to rest!",
          "Even heroes need downtime.",
        ];
      case MascotMood.celebrating:
        return [
          "🎉 Quest completed! 🎉",
          "Victory dance time!",
          "Another achievement unlocked!",
        ];
      case MascotMood.thinking:
        return [
          "Hmm, let me think about this...",
          "What's the best approach here?",
          "Planning is key to success!",
        ];
      case MascotMood.sleeping:
        return [
          "Zzz... Quest notifications off...",
          "Sweet dreams of completed quests...",
          "Even mascots need their beauty sleep!",
        ];
    }
  }
}

@HiveType(typeId: 18)
class MascotStats extends HiveObject {
  @HiveField(0)
  final int questsWitnessed;

  @HiveField(1)
  final int achievementsUnlocked;

  @HiveField(2)
  final int daysActive;

  @HiveField(3)
  final int timesInteracted;

  @HiveField(4)
  final Map<String, int> emotionHistory;

  MascotStats({
    this.questsWitnessed = 0,
    this.achievementsUnlocked = 0,
    this.daysActive = 0,
    this.timesInteracted = 0,
    this.emotionHistory = const {},
  });

  MascotStats copyWith({
    int? questsWitnessed,
    int? achievementsUnlocked,
    int? daysActive,
    int? timesInteracted,
    Map<String, int>? emotionHistory,
  }) {
    return MascotStats(
      questsWitnessed: questsWitnessed ?? this.questsWitnessed,
      achievementsUnlocked: achievementsUnlocked ?? this.achievementsUnlocked,
      daysActive: daysActive ?? this.daysActive,
      timesInteracted: timesInteracted ?? this.timesInteracted,
      emotionHistory: emotionHistory ?? this.emotionHistory,
    );
  }
}

@HiveType(typeId: 19)
class MascotSkin extends HiveObject {
  @HiveField(0)
  final String id;

  @HiveField(1)
  final String name;

  @HiveField(2)
  final String description;

  @HiveField(3)
  final String imageUrl;

  @HiveField(4)
  final bool isUnlockable;

  @HiveField(5)
  final Map<String, dynamic> unlockCriteria;

  @HiveField(6)
  final bool isSeasonal;

  @HiveField(7)
  final String? seasonId;

  MascotSkin({
    required this.id,
    required this.name,
    required this.description,
    required this.imageUrl,
    this.isUnlockable = true,
    this.unlockCriteria = const {},
    this.isSeasonal = false,
    this.seasonId,
  });
}
