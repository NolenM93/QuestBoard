import 'package:hive/hive.dart';

part 'team.g.dart';

@HiveType(typeId: 11)
class Team extends HiveObject {
  @HiveField(0)
  final String id;

  @HiveField(1)
  final String name;

  @HiveField(2)
  final String description;

  @HiveField(3)
  final String leaderId;

  @HiveField(4)
  final List<String> memberIds;

  @HiveField(5)
  final DateTime createdAt;

  @HiveField(6)
  final String mascotId;

  @HiveField(7)
  final int totalXP;

  @HiveField(8)
  final String? githubRepo;

  @HiveField(9)
  final List<String> tags;

  @HiveField(10)
  final TeamSettings settings;

  @HiveField(11)
  final String? inviteCode;

  @HiveField(12)
  final List<Sprint> sprints;

  Team({
    required this.id,
    required this.name,
    required this.description,
    required this.leaderId,
    this.memberIds = const [],
    required this.createdAt,
    required this.mascotId,
    this.totalXP = 0,
    this.githubRepo,
    this.tags = const [],
    required this.settings,
    this.inviteCode,
    this.sprints = const [],
  });

  Team copyWith({
    String? id,
    String? name,
    String? description,
    String? leaderId,
    List<String>? memberIds,
    DateTime? createdAt,
    String? mascotId,
    int? totalXP,
    String? githubRepo,
    List<String>? tags,
    TeamSettings? settings,
    String? inviteCode,
    List<Sprint>? sprints,
  }) {
    return Team(
      id: id ?? this.id,
      name: name ?? this.name,
      description: description ?? this.description,
      leaderId: leaderId ?? this.leaderId,
      memberIds: memberIds ?? this.memberIds,
      createdAt: createdAt ?? this.createdAt,
      mascotId: mascotId ?? this.mascotId,
      totalXP: totalXP ?? this.totalXP,
      githubRepo: githubRepo ?? this.githubRepo,
      tags: tags ?? this.tags,
      settings: settings ?? this.settings,
      inviteCode: inviteCode ?? this.inviteCode,
      sprints: sprints ?? this.sprints,
    );
  }

  Sprint? get currentSprint {
    final now = DateTime.now();
    try {
      return sprints.firstWhere(
        (sprint) => now.isAfter(sprint.startDate) && now.isBefore(sprint.endDate),
      );
    } catch (e) {
      return null;
    }
  }
}

@HiveType(typeId: 12)
class TeamSettings extends HiveObject {
  @HiveField(0)
  final bool isPublic;

  @HiveField(1)
  final bool allowInvites;

  @HiveField(2)
  final int maxMembers;

  @HiveField(3)
  final String? welcomeMessage;

  @HiveField(4)
  final List<String> allowedDomains;

  TeamSettings({
    this.isPublic = false,
    this.allowInvites = true,
    this.maxMembers = 20,
    this.welcomeMessage,
    this.allowedDomains = const [],
  });
}

@HiveType(typeId: 13)
class Sprint extends HiveObject {
  @HiveField(0)
  final String id;

  @HiveField(1)
  final String name;

  @HiveField(2)
  final String? description;

  @HiveField(3)
  final DateTime startDate;

  @HiveField(4)
  final DateTime endDate;

  @HiveField(5)
  final List<String> questIds;

  @HiveField(6)
  final String teamId;

  @HiveField(7)
  final SprintGoals goals;

  Sprint({
    required this.id,
    required this.name,
    this.description,
    required this.startDate,
    required this.endDate,
    this.questIds = const [],
    required this.teamId,
    required this.goals,
  });

  Sprint copyWith({
    String? id,
    String? name,
    String? description,
    DateTime? startDate,
    DateTime? endDate,
    List<String>? questIds,
    String? teamId,
    SprintGoals? goals,
  }) {
    return Sprint(
      id: id ?? this.id,
      name: name ?? this.name,
      description: description ?? this.description,
      startDate: startDate ?? this.startDate,
      endDate: endDate ?? this.endDate,
      questIds: questIds ?? this.questIds,
      teamId: teamId ?? this.teamId,
      goals: goals ?? this.goals,
    );
  }

  bool get isActive {
    final now = DateTime.now();
    return now.isAfter(startDate) && now.isBefore(endDate);
  }

  double get progress {
    if (questIds.isEmpty) return 0.0;
    final now = DateTime.now();
    final duration = endDate.difference(startDate);
    final elapsed = now.difference(startDate);
    return (elapsed.inMilliseconds / duration.inMilliseconds).clamp(0.0, 1.0);
  }
}

@HiveType(typeId: 14)
class SprintGoals extends HiveObject {
  @HiveField(0)
  final int targetXP;

  @HiveField(1)
  final int targetQuests;

  @HiveField(2)
  final Map<String, int> skillTargets;

  @HiveField(3)
  final String? specialGoal;

  SprintGoals({
    this.targetXP = 0,
    this.targetQuests = 0,
    this.skillTargets = const {},
    this.specialGoal,
  });
}
