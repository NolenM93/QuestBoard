import 'package:hive_flutter/hive_flutter.dart';
import 'package:questboard_app/models/quest.dart';
import 'package:uuid/uuid.dart';

class QuestService {
  static const String _questBoxName = 'quests';
  Box<Quest>? _questBox;

  Future<void> initialize() async {
    _questBox = await Hive.openBox<Quest>(_questBoxName);
  }

  Future<Quest> createQuest(Quest quest) async {
    await _questBox!.put(quest.id, quest);
    return quest;
  }

  Future<void> updateQuest(Quest quest) async {
    await _questBox!.put(quest.id, quest);
  }

  Future<void> deleteQuest(String questId) async {
    await _questBox!.delete(questId);
  }

  Quest? getQuest(String questId) {
    return _questBox?.get(questId);
  }

  List<Quest> getAllQuests() {
    return _questBox?.values.toList() ?? [];
  }

  List<Quest> getQuestsByStatus(QuestStatus status) {
    return _questBox?.values
        .where((quest) => quest.status == status)
        .toList() ?? [];
  }

  List<Quest> getQuestsByType(QuestType type) {
    return _questBox?.values
        .where((quest) => quest.type == type)
        .toList() ?? [];
  }

  List<Quest> getQuestsByAssignee(String userId) {
    return _questBox?.values
        .where((quest) => quest.assigneeId == userId)
        .toList() ?? [];
  }

  List<Quest> getActiveQuests() {
    return _questBox?.values
        .where((quest) => quest.status == QuestStatus.inProgress || quest.status == QuestStatus.todo)
        .toList() ?? [];
  }

  List<Quest> getCompletedQuests() {
    return _questBox?.values
        .where((quest) => quest.status == QuestStatus.completed)
        .toList() ?? [];
  }

  Future<void> completeQuest(String questId) async {
    final quest = _questBox?.get(questId);
    if (quest != null) {
      final updatedQuest = quest.copyWith(
        status: QuestStatus.completed,
        completedAt: DateTime.now(),
      );
      await _questBox!.put(questId, updatedQuest);
    }
  }

  Future<void> startQuest(String questId) async {
    final quest = _questBox?.get(questId);
    if (quest != null) {
      final updatedQuest = quest.copyWith(
        status: QuestStatus.inProgress,
      );
      await _questBox!.put(questId, updatedQuest);
    }
  }

  Quest generateSampleQuest({
    required String title,
    required QuestType type,
    required QuestDifficulty difficulty,
    required String assigneeId,
    required String teamId,
  }) {
    return Quest(
      id: const Uuid().v4(),
      title: title,
      description: 'Sample quest description',
      type: type,
      difficulty: difficulty,
      status: QuestStatus.todo,
      assigneeId: assigneeId,
      teamId: teamId,
      xpReward: Quest.getXPForDifficulty(difficulty),
      createdAt: DateTime.now(),
      steps: [],
      dependsOn: [],
    );
  }
}

