import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:questboard_app/models/quest.dart';
import 'package:questboard_app/utils/constants.dart';

class QuestsScreen extends ConsumerWidget {
  const QuestsScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Quests'),
        actions: [
          IconButton(
            icon: const Icon(Icons.filter_list),
            onPressed: () {
              _showFilterDialog(context);
            },
          ),
        ],
      ),
      body: _buildQuestsList(context),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () {
          _showCreateQuestDialog(context);
        },
        icon: const Icon(Icons.add),
        label: const Text('Create Quest'),
      ),
    );
  }

  Widget _buildQuestsList(BuildContext context) {
    // For now, show empty state - this will be populated with actual quest data later
    return _buildEmptyState(context);
  }

  Widget _buildEmptyState(BuildContext context) {
    return Center(
      child: Padding(
        padding: const EdgeInsets.all(AppSpacing.xl),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              width: 120,
              height: 120,
              decoration: BoxDecoration(
                color: AppColors.primary.withValues(alpha: 0.1),
                borderRadius: BorderRadius.circular(AppRadius.xl),
              ),
              child: Icon(
                Icons.task_outlined,
                size: 64,
                color: AppColors.primary.withValues(alpha: 0.5),
              ),
            ),
            const SizedBox(height: AppSpacing.xl),
            Text(
              'No Quests Yet',
              style: AppTextStyles.h2.copyWith(
                color: AppColors.textPrimary,
              ),
            ),
            const SizedBox(height: AppSpacing.md),
            Text(
              'Create your first quest to start your adventure!',
              style: AppTextStyles.bodyLarge.copyWith(
                color: AppColors.textSecondary,
              ),
              textAlign: TextAlign.center,
            ),
            const SizedBox(height: AppSpacing.xl),
            ElevatedButton.icon(
              onPressed: () {
                _showCreateQuestDialog(context);
              },
              icon: const Icon(Icons.add),
              label: const Text('Create Your First Quest'),
              style: ElevatedButton.styleFrom(
                backgroundColor: AppColors.primary,
                foregroundColor: Colors.white,
                padding: const EdgeInsets.symmetric(
                  horizontal: AppSpacing.xl,
                  vertical: AppSpacing.md,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  void _showCreateQuestDialog(BuildContext context) {
    showDialog(
      context: context,
      builder: (context) => const CreateQuestDialog(),
    );
  }

  void _showFilterDialog(BuildContext context) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Filter Quests'),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Text(
              'Filter options coming soon!',
              style: AppTextStyles.bodyMedium.copyWith(
                color: AppColors.textSecondary,
              ),
            ),
          ],
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(context).pop(),
            child: const Text('Close'),
          ),
        ],
      ),
    );
  }
}

class CreateQuestDialog extends StatefulWidget {
  const CreateQuestDialog({super.key});

  @override
  State<CreateQuestDialog> createState() => _CreateQuestDialogState();
}

class _CreateQuestDialogState extends State<CreateQuestDialog> {
  final _titleController = TextEditingController();
  final _descriptionController = TextEditingController();
  QuestType _selectedType = QuestType.build;
  QuestDifficulty _selectedDifficulty = QuestDifficulty.medium;
  DateTime? _dueDate;

  @override
  Widget build(BuildContext context) {
    return AlertDialog(
      title: Row(
        children: [
          Icon(
            Icons.add_task,
            color: AppColors.primary,
          ),
          const SizedBox(width: AppSpacing.sm),
          const Text('Create New Quest'),
        ],
      ),
      content: SizedBox(
        width: double.maxFinite,
        child: SingleChildScrollView(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              TextField(
                controller: _titleController,
                decoration: const InputDecoration(
                  labelText: 'Quest Title',
                  hintText: 'Enter a descriptive title',
                  border: OutlineInputBorder(),
                ),
              ),
              const SizedBox(height: AppSpacing.md),
              TextField(
                controller: _descriptionController,
                decoration: const InputDecoration(
                  labelText: 'Description',
                  hintText: 'What needs to be accomplished?',
                  border: OutlineInputBorder(),
                ),
                maxLines: 3,
              ),
              const SizedBox(height: AppSpacing.md),
              DropdownButtonFormField<QuestType>(
                value: _selectedType,
                decoration: const InputDecoration(
                  labelText: 'Quest Type',
                  border: OutlineInputBorder(),
                ),
                items: QuestType.values.map((type) {
                  return DropdownMenuItem(
                    value: type,
                    child: Row(
                      children: [
                        Icon(
                          _getQuestTypeIcon(type),
                          color: _getQuestTypeColor(type),
                        ),
                        const SizedBox(width: AppSpacing.sm),
                        Text(_formatQuestType(type)),
                      ],
                    ),
                  );
                }).toList(),
                onChanged: (value) {
                  if (value != null) {
                    setState(() {
                      _selectedType = value;
                    });
                  }
                },
              ),
              const SizedBox(height: AppSpacing.md),
              DropdownButtonFormField<QuestDifficulty>(
                value: _selectedDifficulty,
                decoration: const InputDecoration(
                  labelText: 'Difficulty',
                  border: OutlineInputBorder(),
                ),
                items: QuestDifficulty.values.map((difficulty) {
                  return DropdownMenuItem(
                    value: difficulty,
                    child: Row(
                      children: [
                        Icon(
                          _getDifficultyIcon(difficulty),
                          color: _getDifficultyColor(difficulty),
                        ),
                        const SizedBox(width: AppSpacing.sm),
                        Text(_formatDifficulty(difficulty)),
                      ],
                    ),
                  );
                }).toList(),
                onChanged: (value) {
                  if (value != null) {
                    setState(() {
                      _selectedDifficulty = value;
                    });
                  }
                },
              ),
              const SizedBox(height: AppSpacing.md),
              ListTile(
                contentPadding: EdgeInsets.zero,
                leading: Icon(
                  Icons.calendar_today,
                  color: AppColors.primary,
                ),
                title: Text(_dueDate == null ? 'Set Due Date (Optional)' : 'Due Date'),
                subtitle: _dueDate == null 
                    ? null 
                    : Text('${_dueDate!.day}/${_dueDate!.month}/${_dueDate!.year}'),
                trailing: _dueDate == null 
                    ? null 
                    : IconButton(
                        icon: const Icon(Icons.clear),
                        onPressed: () {
                          setState(() {
                            _dueDate = null;
                          });
                        },
                      ),
                onTap: () async {
                  final date = await showDatePicker(
                    context: context,
                    initialDate: DateTime.now().add(const Duration(days: 7)),
                    firstDate: DateTime.now(),
                    lastDate: DateTime.now().add(const Duration(days: 365)),
                  );
                  if (date != null) {
                    setState(() {
                      _dueDate = date;
                    });
                  }
                },
              ),
            ],
          ),
        ),
      ),
      actions: [
        TextButton(
          onPressed: () => Navigator.of(context).pop(),
          child: const Text('Cancel'),
        ),
        ElevatedButton(
          onPressed: _titleController.text.isNotEmpty ? _createQuest : null,
          style: ElevatedButton.styleFrom(
            backgroundColor: AppColors.primary,
            foregroundColor: Colors.white,
          ),
          child: const Text('Create Quest'),
        ),
      ],
    );
  }

  void _createQuest() {
    if (_titleController.text.trim().isEmpty) return;

    // TODO: Implement quest creation logic with providers
    // For now, just show a success message and close dialog
    
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text('Quest "${_titleController.text}" created!'),
        backgroundColor: AppColors.success,
      ),
    );
    
    Navigator.of(context).pop();
  }

  IconData _getQuestTypeIcon(QuestType type) {
    switch (type) {
      case QuestType.brainstorm:
        return Icons.lightbulb_outline;
      case QuestType.build:
        return Icons.build;
      case QuestType.promote:
        return Icons.campaign;
      case QuestType.research:
        return Icons.search;
      case QuestType.test:
        return Icons.bug_report;
      case QuestType.review:
        return Icons.rate_review;
      case QuestType.learn:
        return Icons.school;
    }
  }

  Color _getQuestTypeColor(QuestType type) {
    switch (type) {
      case QuestType.brainstorm:
        return AppColors.brainstorm;
      case QuestType.build:
        return AppColors.build;
      case QuestType.promote:
        return AppColors.promote;
      case QuestType.research:
        return AppColors.research;
      case QuestType.test:
        return AppColors.test;
      case QuestType.review:
        return AppColors.review;
      case QuestType.learn:
        return AppColors.learn;
    }
  }

  String _formatQuestType(QuestType type) {
    return type.name[0].toUpperCase() + type.name.substring(1);
  }

  IconData _getDifficultyIcon(QuestDifficulty difficulty) {
    switch (difficulty) {
      case QuestDifficulty.easy:
        return Icons.sentiment_satisfied;
      case QuestDifficulty.medium:
        return Icons.sentiment_neutral;
      case QuestDifficulty.hard:
        return Icons.sentiment_dissatisfied;
      case QuestDifficulty.epic:
        return Icons.whatshot;
    }
  }

  Color _getDifficultyColor(QuestDifficulty difficulty) {
    switch (difficulty) {
      case QuestDifficulty.easy:
        return AppColors.success;
      case QuestDifficulty.medium:
        return AppColors.warning;
      case QuestDifficulty.hard:
        return AppColors.error;
      case QuestDifficulty.epic:
        return AppColors.promote;
    }
  }

  String _formatDifficulty(QuestDifficulty difficulty) {
    return difficulty.name[0].toUpperCase() + difficulty.name.substring(1);
  }

  @override
  void dispose() {
    _titleController.dispose();
    _descriptionController.dispose();
    super.dispose();
  }
}