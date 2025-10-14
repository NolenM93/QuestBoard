import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:questboard_app/models/quest.dart';
import 'package:questboard_app/services/quest_service.dart';

final questServiceProvider = Provider<QuestService>((ref) {
  return QuestService();
});

final questsProvider = StateNotifierProvider<QuestsNotifier, AsyncValue<List<Quest>>>((ref) {
  return QuestsNotifier(ref.watch(questServiceProvider));
});

class QuestsNotifier extends StateNotifier<AsyncValue<List<Quest>>> {
  final QuestService _questService;

  QuestsNotifier(this._questService) : super(const AsyncValue.loading()) {
    _loadQuests();
  }

  Future<void> _loadQuests() async {
    try {
      await _questService.initialize();
      final quests = _questService.getAllQuests();
      state = AsyncValue.data(quests);
    } catch (e, stack) {
      state = AsyncValue.error(e, stack);
    }
  }

  Future<void> createQuest(Quest quest) async {
    try {
      await _questService.createQuest(quest);
      await refresh();
    } catch (e, stack) {
      state = AsyncValue.error(e, stack);
      rethrow;
    }
  }

  Future<void> updateQuest(Quest quest) async {
    try {
      await _questService.updateQuest(quest);
      await refresh();
    } catch (e, stack) {
      state = AsyncValue.error(e, stack);
      rethrow;
    }
  }

  Future<void> deleteQuest(String questId) async {
    try {
      await _questService.deleteQuest(questId);
      await refresh();
    } catch (e, stack) {
      state = AsyncValue.error(e, stack);
      rethrow;
    }
  }

  Future<void> completeQuest(String questId) async {
    try {
      await _questService.completeQuest(questId);
      await refresh();
    } catch (e, stack) {
      state = AsyncValue.error(e, stack);
      rethrow;
    }
  }

  Future<void> startQuest(String questId) async {
    try {
      await _questService.startQuest(questId);
      await refresh();
    } catch (e, stack) {
      state = AsyncValue.error(e, stack);
      rethrow;
    }
  }

  Future<void> refresh() async {
    await _loadQuests();
  }

  List<Quest> getActiveQuests() {
    return state.value?.where(
      (quest) => quest.status == QuestStatus.inProgress || quest.status == QuestStatus.todo
    ).toList() ?? [];
  }

  List<Quest> getQuestsByStatus(QuestStatus status) {
    return state.value?.where((quest) => quest.status == status).toList() ?? [];
  }
}
