# Quest Management Guide

A comprehensive guide to creating, managing, and optimizing quests in QuestBoard.

## Quest Lifecycle

Every quest goes through a lifecycle:

```
Created → Assigned → In Progress → Completed
                               ↓
                          Abandoned
```

### 1. Creating Quests

```python
from src.services.quest_service import QuestService
from src.models.quest import QuestType, QuestDifficulty

quest = QuestService.create_quest(
    title="Implement feature X",
    description="Detailed description of what needs to be done",
    difficulty=QuestDifficulty.MEDIUM,
    quest_type=QuestType.BUILD,
    tags=["feature", "backend"]
)
```

### 2. Assigning Quests

```python
# Manual assignment
member = team.get_member("alice")
QuestService.assign_quest(quest, member)

# AI-assisted suggestion
from src.utils.ai_assistant import AIAssistant
suggested_quests = AIAssistant.suggest_next_quest(team, member)
```

### 3. Working on Quests

```python
# Start the quest
quest.start()

# Quest is now in "In Progress" status
print(quest.status)  # QuestStatus.IN_PROGRESS
```

### 4. Completing Quests

```python
# Complete and earn XP
xp_earned = QuestService.complete_quest(quest, team)

# XP is automatically distributed to:
# - The assigned team member
# - The team mascot
```

### 5. Abandoning Quests

```python
# If a quest can't be completed
quest.abandon()

# Note: Abandoned quests don't award XP
# Consider breaking down or reassigning instead
```

## Quest Types in Detail

### 🧠 Brainstorm Quests
**Purpose**: Ideation, planning, and creative thinking

**Best For**:
- Project planning and roadmapping
- Feature ideation sessions
- Problem-solving discussions
- Strategy development

**Examples**:
```python
QuestService.create_quest(
    title="Sprint planning session",
    description="Define goals and tasks for the upcoming sprint",
    difficulty=QuestDifficulty.MEDIUM,
    quest_type=QuestType.BRAINSTORM
)
```

### 🔧 Build Quests
**Purpose**: Implementation and construction tasks

**Best For**:
- Feature development
- Infrastructure setup
- Tool creation
- System configuration

**Examples**:
```python
QuestService.create_quest(
    title="Build REST API endpoints",
    description="Create CRUD endpoints for user management",
    difficulty=QuestDifficulty.HARD,
    quest_type=QuestType.BUILD
)
```

### 📣 Promote Quests
**Purpose**: Marketing, communication, and outreach

**Best For**:
- Content creation
- Social media posts
- Presentations
- User engagement

**Examples**:
```python
QuestService.create_quest(
    title="Write release announcement",
    description="Create blog post announcing new features",
    difficulty=QuestDifficulty.EASY,
    quest_type=QuestType.PROMOTE
)
```

### 🐛 Debug Quests
**Purpose**: Bug fixing and troubleshooting

**Best For**:
- Bug resolution
- Performance optimization
- Error investigation
- System diagnostics

**Examples**:
```python
QuestService.create_quest(
    title="Fix memory leak in authentication",
    description="Investigate and resolve memory leak reported in production",
    difficulty=QuestDifficulty.HARD,
    quest_type=QuestType.DEBUG
)
```

### 📚 Learn Quests
**Purpose**: Research, learning, and skill development

**Best For**:
- Technology research
- Training and education
- Best practices study
- Competitive analysis

**Examples**:
```python
QuestService.create_quest(
    title="Research GraphQL alternatives to REST",
    description="Evaluate GraphQL for our API layer",
    difficulty=QuestDifficulty.MEDIUM,
    quest_type=QuestType.LEARN
)
```

### 👀 Review Quests
**Purpose**: Code review and quality assurance

**Best For**:
- Pull request reviews
- Testing and QA
- Code audits
- Security reviews

**Examples**:
```python
QuestService.create_quest(
    title="Review authentication PR",
    description="Review and provide feedback on PR #123",
    difficulty=QuestDifficulty.EASY,
    quest_type=QuestType.REVIEW
)
```

### 📝 Documentation Quests
**Purpose**: Writing documentation and guides

**Best For**:
- API documentation
- User guides
- Technical specs
- README updates

**Examples**:
```python
QuestService.create_quest(
    title="Document deployment process",
    description="Create step-by-step deployment guide",
    difficulty=QuestDifficulty.MEDIUM,
    quest_type=QuestType.DOCUMENTATION
)
```

## XP and Difficulty

### XP Calculation

XP is calculated based on:
1. **Base Difficulty**: Easy (25), Medium (50), Hard (100), Epic (200)
2. **Type Multiplier**: Different quest types have different multipliers
3. **Bonus Multipliers**: Team size, streaks, etc.

```python
from src.utils.xp_calculator import XPCalculator

# Calculate XP for a quest
xp = XPCalculator.calculate_quest_xp(
    difficulty=QuestDifficulty.HARD,
    quest_type=QuestType.DEBUG,
    bonus_multiplier=1.5  # 1.5x for urgent tasks
)
```

### Choosing Difficulty

#### Easy (25 XP)
- **Time**: 1-2 hours
- **Complexity**: Straightforward, clear path
- **Dependencies**: Minimal
- **Examples**: Update README, fix typo, create mockup

#### Medium (50 XP)
- **Time**: Half-day to full day
- **Complexity**: Some problem-solving required
- **Dependencies**: Some coordination needed
- **Examples**: Implement small feature, write unit tests, create design

#### Hard (100 XP)
- **Time**: 1-2 days
- **Complexity**: Significant problem-solving
- **Dependencies**: Multiple team coordination
- **Examples**: Build new system component, major refactor, integration

#### Epic (200 XP)
- **Time**: 3+ days
- **Complexity**: Major undertaking
- **Dependencies**: Cross-team effort
- **Examples**: Complete feature launch, system migration, major release

## Quest Management Tips

### 1. Quest Breakdown Strategy

Use the AI assistant to break down epic quests:

```python
from src.utils.ai_assistant import AIAssistant

breakdown = AIAssistant.suggest_quest_breakdown(
    "Build mobile app",
    "Create iOS and Android applications"
)

for sub_quest in breakdown:
    quest = QuestService.create_quest(**sub_quest)
    team.add_quest(quest)
```

### 2. Prioritization

Use tags to prioritize:

```python
# High priority quest
quest = QuestService.create_quest(
    title="Fix production bug",
    description="Critical bug affecting users",
    difficulty=QuestDifficulty.HARD,
    quest_type=QuestType.DEBUG,
    tags=["urgent", "production", "bug"]
)
```

### 3. Team Load Balancing

Check member workload before assigning:

```python
# Get active quests per member
for member in team.members:
    active = QuestService.get_quests_by_member(team, member.username)
    in_progress = [q for q in active if q.status == QuestStatus.IN_PROGRESS]
    print(f"{member.display_name}: {len(in_progress)} active quests")
```

### 4. Quest Templates

Create templates for common quest types:

```python
def create_pr_review_quest(pr_number, assignee):
    return QuestService.create_quest(
        title=f"Review PR #{pr_number}",
        description=f"Review and provide feedback on pull request #{pr_number}",
        difficulty=QuestDifficulty.EASY,
        quest_type=QuestType.REVIEW,
        tags=["code-review", f"pr-{pr_number}"]
    )
```

### 5. Tracking Overdue Quests

```python
# Get quests that have been open too long
overdue = QuestService.get_overdue_quests(team, days_threshold=7)

for quest in overdue:
    print(f"⚠️ Overdue: {quest.title} (assigned to {quest.assigned_to})")
```

## Best Practices

1. **Clear Titles**: Use action verbs ("Implement", "Fix", "Create")
2. **Detailed Descriptions**: Include acceptance criteria
3. **Appropriate Difficulty**: Be realistic about effort
4. **Useful Tags**: Make quests searchable and filterable
5. **Regular Updates**: Keep quest status current
6. **Celebrate Completions**: Acknowledge wins in team feed

## Quest Analytics

Track quest metrics:

```python
# Completion rate by quest type
from collections import defaultdict

completed_by_type = defaultdict(int)
total_by_type = defaultdict(int)

for quest in team.quests:
    total_by_type[quest.quest_type] += 1
    if quest.status == QuestStatus.COMPLETED:
        completed_by_type[quest.quest_type] += 1

for quest_type in QuestType:
    total = total_by_type[quest_type]
    completed = completed_by_type[quest_type]
    rate = (completed / total * 100) if total > 0 else 0
    print(f"{quest_type.value}: {rate:.1f}% completion")
```

## Advanced Features

### Custom XP Rewards

```python
# Override automatic XP calculation
quest = QuestService.create_quest(
    title="Win hackathon",
    description="Compete and win first place",
    difficulty=QuestDifficulty.EPIC,
    quest_type=QuestType.BUILD,
    xp_reward=500  # Custom XP reward
)
```

### Quest Dependencies

While not built-in, you can track dependencies with tags:

```python
quest1 = QuestService.create_quest(
    title="Design database schema",
    difficulty=QuestDifficulty.MEDIUM,
    quest_type=QuestType.BRAINSTORM,
    tags=["database", "prerequisite-001"]
)

quest2 = QuestService.create_quest(
    title="Implement database models",
    difficulty=QuestDifficulty.HARD,
    quest_type=QuestType.BUILD,
    tags=["database", "depends-on-001"]
)
```

---

Need more help? Check out the [API Reference](api-reference.md) or our [example configurations](../examples/).
