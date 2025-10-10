import 'package:hive/hive.dart';

part 'quest.g.dart';

@HiveType(typeId: 2)
enum QuestType {
  @HiveField(0)
  brainstorm,
  @HiveField(1)
  build,
  @HiveField(2)
  promote,
  @HiveField(3)
  research,
  @HiveField(4)
  test,
  @HiveField(5)
  review,
  @HiveField(6)
  learn,
}

@HiveType(typeId: 3)
enum QuestDifficulty {
  @HiveField(0)
  easy,
  @HiveField(1)
  medium,
  @HiveField(2)
  hard,
  @HiveField(3)
  epic,
}

@HiveType(typeId: 4)
enum QuestStatus {
  @HiveField(0)
  todo,
  @HiveField(1)
  inProgress,
  @HiveField(2)
  completed,
  @HiveField(3)
  blocked,
  @HiveField(4)
  cancelled,
}

@HiveType(typeId: 5)
class Quest extends HiveObject {
  @HiveField(0)
  final String id;

  @HiveField(1)
  final String title;

  @HiveField(2)
  final String description;

  @HiveField(3)
  final QuestType type;

  @HiveField(4)
  final QuestDifficulty difficulty;

  @HiveField(5)
  final int xpReward;

  @HiveField(6)
  final QuestStatus status;

  @HiveField(7)
  final String assigneeId;

  @HiveField(8)
  final String teamId;

  @HiveField(9)
  final DateTime createdAt;

  @HiveField(10)
  final DateTime? dueDate;

  @HiveField(11)
  final DateTime? completedAt;

  @HiveField(12)
  final List<String> tags;

  @HiveField(13)
  final List<QuestStep> steps;

  @HiveField(14)
  final String? githubBranch;

  @HiveField(15)
  final List<String> attachmentUrls;

  @HiveField(16)
  final int estimatedHours;

  @HiveField(17)
  final List<String> dependsOn;

  Quest({
    required this.id,
    required this.title,
    required this.description,
    required this.type,
    required this.difficulty,
    required this.xpReward,
    this.status = QuestStatus.todo,
    required this.assigneeId,
    required this.teamId,
    required this.createdAt,
    this.dueDate,
    this.completedAt,
    this.tags = const [],
    this.steps = const [],
    this.githubBranch,
    this.attachmentUrls = const [],
    this.estimatedHours = 1,
    this.dependsOn = const [],
  });

  Quest copyWith({
    String? id,
    String? title,
    String? description,
    QuestType? type,
    QuestDifficulty? difficulty,
    int? xpReward,
    QuestStatus? status,
    String? assigneeId,
    String? teamId,
    DateTime? createdAt,
    DateTime? dueDate,
    DateTime? completedAt,
    List<String>? tags,
    List<QuestStep>? steps,
    String? githubBranch,
    List<String>? attachmentUrls,
    int? estimatedHours,
    List<String>? dependsOn,
  }) {
    return Quest(
      id: id ?? this.id,
      title: title ?? this.title,
      description: description ?? this.description,
      type: type ?? this.type,
      difficulty: difficulty ?? this.difficulty,
      xpReward: xpReward ?? this.xpReward,
      status: status ?? this.status,
      assigneeId: assigneeId ?? this.assigneeId,
      teamId: teamId ?? this.teamId,
      createdAt: createdAt ?? this.createdAt,
      dueDate: dueDate ?? this.dueDate,
      completedAt: completedAt ?? this.completedAt,
      tags: tags ?? this.tags,
      steps: steps ?? this.steps,
      githubBranch: githubBranch ?? this.githubBranch,
      attachmentUrls: attachmentUrls ?? this.attachmentUrls,
      estimatedHours: estimatedHours ?? this.estimatedHours,
      dependsOn: dependsOn ?? this.dependsOn,
    );
  }

  double get progress {
    if (steps.isEmpty) return status == QuestStatus.completed ? 1.0 : 0.0;
    final completedSteps = steps.where((step) => step.isCompleted).length;
    return completedSteps / steps.length;
  }

  static int getXPForDifficulty(QuestDifficulty difficulty) {
    switch (difficulty) {
      case QuestDifficulty.easy:
        return 15;
      case QuestDifficulty.medium:
        return 35;
      case QuestDifficulty.hard:
        return 75;
      case QuestDifficulty.epic:
        return 150;
    }
  }

  static String getColorForType(QuestType type) {
    switch (type) {
      case QuestType.brainstorm:
        return '#FF6B35';
      case QuestType.build:
        return '#4ECDC4';
      case QuestType.promote:
        return '#45B7D1';
      case QuestType.research:
        return '#96CEB4';
      case QuestType.test:
        return '#FFEAA7';
      case QuestType.review:
        return '#DDA0DD';
      case QuestType.learn:
        return '#FFB6C1';
    }
  }
}

@HiveType(typeId: 6)
class QuestStep extends HiveObject {
  @HiveField(0)
  final String id;

  @HiveField(1)
  final String title;

  @HiveField(2)
  final bool isCompleted;

  @HiveField(3)
  final DateTime? completedAt;

  @HiveField(4)
  final String? notes;

  QuestStep({
    required this.id,
    required this.title,
    this.isCompleted = false,
    this.completedAt,
    this.notes,
  });

  QuestStep copyWith({
    String? id,
    String? title,
    bool? isCompleted,
    DateTime? completedAt,
    String? notes,
  }) {
    return QuestStep(
      id: id ?? this.id,
      title: title ?? this.title,
      isCompleted: isCompleted ?? this.isCompleted,
      completedAt: completedAt ?? this.completedAt,
      notes: notes ?? this.notes,
    );
  }
}
