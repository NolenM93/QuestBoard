# API Reference

Complete reference for QuestBoard classes, methods, and utilities.

## Models

### Quest

Represents a task or goal in the QuestBoard system.

#### Constructor
```python
Quest(
    title: str,
    description: str,
    difficulty: QuestDifficulty,
    quest_type: QuestType,
    xp_reward: int,
    status: QuestStatus = QuestStatus.CREATED,
    assigned_to: Optional[str] = None,
    tags: List[str] = []
)
```

#### Methods

##### `assign_to(username: str)`
Assign the quest to a team member.

##### `start()`
Mark the quest as in progress.

##### `complete() -> int`
Mark the quest as completed and return XP reward.

##### `abandon()`
Mark the quest as abandoned.

##### `get_icon() -> str`
Get the emoji icon for this quest type.

##### `to_dict() -> dict`
Convert quest to dictionary representation.

#### Enums

**QuestType**
- `BRAINSTORM`: Ideation and planning
- `BUILD`: Implementation tasks
- `PROMOTE`: Marketing and communication
- `DEBUG`: Bug fixing
- `LEARN`: Research and learning
- `REVIEW`: Code review and QA
- `DOCUMENTATION`: Writing docs

**QuestDifficulty**
- `EASY`: 25 base XP
- `MEDIUM`: 50 base XP
- `HARD`: 100 base XP
- `EPIC`: 200 base XP

**QuestStatus**
- `CREATED`: Just created
- `ASSIGNED`: Assigned to member
- `IN_PROGRESS`: Being worked on
- `COMPLETED`: Finished
- `ABANDONED`: Not completed

---

### Achievement

Represents a badge or achievement in the QuestBoard system.

#### Constructor
```python
Achievement(
    name: str,
    description: str,
    tier: AchievementTier,
    category: AchievementCategory,
    xp_requirement: int,
    icon: str = "🏆",
    progress: int = 0
)
```

#### Methods

##### `unlock()`
Mark the achievement as unlocked.

##### `is_unlocked() -> bool`
Check if the achievement is unlocked.

##### `update_progress(current_xp: int)`
Update progress towards unlocking.

##### `get_tier_color() -> str`
Get the color code for this tier.

##### `to_dict() -> dict`
Convert achievement to dictionary.

#### Enums

**AchievementTier**
- `BRONZE`: 10 XP threshold
- `SILVER`: 50 XP threshold
- `GOLD`: 100 XP threshold
- `PLATINUM`: 250 XP threshold
- `DIAMOND`: 500 XP threshold

**AchievementCategory**
- `CONTRIBUTIONS`: Quest completions
- `LEADERSHIP`: Quest creation
- `CREATIVITY`: Innovative solutions
- `CONSISTENCY`: Regular activity
- `COLLABORATION`: Teamwork
- `SPEED`: Quick completions
- `QUALITY`: High-quality work

#### Functions

##### `create_default_achievements() -> List[Achievement]`
Create a set of default achievements for a new team.

---

### Mascot

Represents a team mascot that evolves with team progress.

#### Constructor
```python
Mascot(
    name: str,
    mascot_type: MascotType,
    evolution_stage: MascotEvolutionStage = MascotEvolutionStage.EGG,
    total_xp: int = 0,
    personality_traits: List[str] = [],
    skin: str = "default"
)
```

#### Methods

##### `add_xp(xp: int) -> bool`
Add XP to the mascot and check for evolution. Returns True if mascot evolved.

##### `change_skin(skin: str)`
Change the mascot's appearance skin.

##### `add_personality_trait(trait: str)`
Add a personality trait to the mascot.

##### `get_emoji() -> str`
Get the emoji representation of the mascot.

##### `get_xp_to_next_stage() -> Optional[int]`
Calculate XP needed to reach the next evolution stage.

##### `to_dict() -> dict`
Convert mascot to dictionary.

#### Enums

**MascotType**
- `CYBER_SLOTH`: 🦥 Efficient coding companion
- `PIXEL_PHOENIX`: 🐦 Rises from failures
- `CODE_DRAGON`: 🐉 Guardian of clean code
- `NINJA_TURTLE`: 🐢 Steady progress master
- `SPACE_CAT`: 🐱 Code explorer
- `RETRO_ROBOT`: 🤖 Nostalgic automator
- `QUANTUM_QUOKKA`: 🦘 Quantum productivity

**MascotEvolutionStage**
- `EGG`: 0 XP
- `HATCHLING`: 100 XP
- `JUVENILE`: 500 XP
- `ADULT`: 1,000 XP
- `ELDER`: 2,000 XP
- `LEGENDARY`: 5,000 XP

#### Functions

##### `get_seasonal_skins() -> Dict[str, List[str]]`
Get available seasonal skins for mascots.

---

### Team

Represents a team using QuestBoard.

#### Constructor
```python
Team(
    name: str,
    mascot: Mascot,
    members: List[TeamMember] = [],
    quests: List[Quest] = [],
    achievements: List[Achievement] = [],
    description: str = ""
)
```

#### Class Methods

##### `create(name, mascot_name, mascot_type, description="") -> Team`
Factory method to create a new team with a mascot.

#### Methods

##### `add_member(member: TeamMember)`
Add a member to the team.

##### `get_member(username: str) -> Optional[TeamMember]`
Get a team member by username.

##### `add_quest(quest: Quest)`
Add a quest to the team.

##### `get_quest(quest_id: str) -> Optional[Quest]`
Get a quest by ID.

##### `get_total_xp() -> int`
Calculate total XP earned by the team.

##### `get_total_quests_completed() -> int`
Calculate total quests completed by the team.

##### `get_active_quests() -> List[Quest]`
Get all active (non-completed, non-abandoned) quests.

##### `get_leaderboard() -> List[TeamMember]`
Get team members sorted by XP (highest first).

##### `to_dict() -> dict`
Convert team to dictionary.

---

### TeamMember

Represents a member of a team.

#### Constructor
```python
TeamMember(
    username: str,
    display_name: str,
    role: str = "Member",
    total_xp: int = 0,
    quests_completed: int = 0,
    avatar: str = "👤"
)
```

#### Methods

##### `add_xp(xp: int)`
Add XP to the team member.

##### `complete_quest(xp_reward: int)`
Mark a quest as completed for this member.

##### `get_level() -> int`
Calculate member level based on total XP.

##### `to_dict() -> dict`
Convert team member to dictionary.

---

## Services

### QuestService

Business logic for quest management.

#### Static Methods

##### `create_quest(...) -> Quest`
Create a new quest with optional auto-calculated XP.

```python
QuestService.create_quest(
    title="Task title",
    description="Task description",
    difficulty=QuestDifficulty.MEDIUM,
    quest_type=QuestType.BUILD,
    xp_reward=None,  # Auto-calculated if None
    tags=["tag1", "tag2"]
)
```

##### `calculate_xp_reward(difficulty, quest_type) -> int`
Calculate XP reward based on difficulty and quest type.

##### `assign_quest(quest, team_member)`
Assign a quest to a team member.

##### `complete_quest(quest, team) -> int`
Complete a quest and award XP. Returns XP awarded.

##### `get_quests_by_status(team, status) -> List[Quest]`
Get all quests with a specific status.

##### `get_quests_by_member(team, username) -> List[Quest]`
Get all quests assigned to a specific member.

##### `get_quests_by_type(team, quest_type) -> List[Quest]`
Get all quests of a specific type.

##### `get_overdue_quests(team, days_threshold=7) -> List[Quest]`
Get quests that have been in progress for too long.

##### `suggest_quest_breakdown(quest_title) -> List[dict]`
AI-assisted suggestion for breaking down a large quest.

---

### AchievementService

Business logic for achievement management.

#### Static Methods

##### `initialize_team_achievements(team)`
Initialize a team with default achievements.

##### `check_achievements(team, member) -> List[Achievement]`
Check and unlock achievements for a team member. Returns newly unlocked achievements.

##### `get_achievements_by_tier(team, tier) -> List[Achievement]`
Get all achievements of a specific tier.

##### `get_achievements_by_category(team, category) -> List[Achievement]`
Get all achievements of a specific category.

##### `get_unlocked_achievements(team) -> List[Achievement]`
Get all unlocked achievements for the team.

##### `get_progress_summary(team) -> dict`
Get a summary of achievement progress.

Returns:
```python
{
    'total_achievements': int,
    'unlocked': int,
    'locked': int,
    'completion_percentage': float,
    'by_tier': {...}
}
```

---

### MascotService

Business logic for mascot management.

#### Static Methods

##### `create_mascot(name, mascot_type) -> Mascot`
Create a new mascot.

##### `evolve_mascot(mascot, xp) -> bool`
Add XP to mascot and check for evolution. Returns True if evolved.

##### `get_evolution_message(mascot) -> str`
Get a celebratory message for mascot evolution.

##### `apply_seasonal_skin(mascot, season)`
Apply a seasonal skin to the mascot.

Seasons: "spring", "summer", "fall", "winter", "special"

##### `get_available_skins(season=None) -> dict`
Get available skins, optionally filtered by season.

##### `add_personality_trait(mascot, trait)`
Add a personality trait to the mascot.

##### `suggest_personality_traits(team) -> List[str]`
Suggest personality traits based on team behavior.

##### `get_mascot_stats(mascot) -> dict`
Get comprehensive stats for a mascot.

##### `get_evolution_timeline(mascot) -> List[dict]`
Get the evolution timeline for a mascot.

---

## Utilities

### XPCalculator

Utility class for XP-related calculations.

#### Static Methods

##### `calculate_quest_xp(difficulty, quest_type, bonus_multiplier=1.0) -> int`
Calculate XP reward for a quest.

##### `calculate_level_from_xp(xp) -> int`
Calculate level from total XP using formula: Level = floor(sqrt(xp / 100))

##### `calculate_xp_for_level(level) -> int`
Calculate total XP needed to reach a specific level.

##### `calculate_xp_to_next_level(current_xp) -> int`
Calculate XP needed to reach the next level.

##### `calculate_progress_to_next_level(current_xp) -> float`
Calculate progress percentage to next level (0-100).

##### `calculate_team_xp_multiplier(team_size) -> float`
Calculate XP multiplier based on team size.

##### `calculate_streak_bonus(streak_days) -> float`
Calculate XP bonus multiplier based on consecutive activity streak.

---

### AIAssistant

AI-powered assistant for team guidance.

#### Static Methods

##### `suggest_quest_breakdown(title, description="") -> List[Dict]`
Suggest how to break down a large quest into smaller ones.

Returns list of quest suggestions with keys:
- `title`: Suggested title
- `description`: Suggested description
- `difficulty`: Quest difficulty
- `quest_type`: Quest type

##### `suggest_next_quest(team, member) -> List[Quest]`
Suggest next quests for a team member based on their history.

##### `generate_motivational_message(team) -> str`
Generate a motivational message based on team performance.

##### `suggest_onboarding_quests(team_name) -> List[Dict]`
Generate onboarding quests for a new team or member.

##### `analyze_team_health(team) -> Dict`
Analyze team health and provide insights.

Returns:
```python
{
    'health_score': int,  # 0-100
    'total_quests': int,
    'completed': int,
    'in_progress': int,
    'abandoned': int,
    'completion_rate': float,
    'abandonment_rate': float,
    'recommendations': List[str]
}
```

---

## Usage Examples

### Complete Workflow Example

```python
from src.models.team import Team, TeamMember
from src.models.mascot import MascotType
from src.models.quest import QuestType, QuestDifficulty
from src.services.quest_service import QuestService
from src.services.achievement_service import AchievementService

# Create team
team = Team.create(
    name="Dev Squad",
    mascot_name="Sparky",
    mascot_type=MascotType.CODE_DRAGON
)

# Initialize achievements
AchievementService.initialize_team_achievements(team)

# Add members
alice = TeamMember(username="alice", display_name="Alice", role="Developer")
team.add_member(alice)

# Create and complete quest
quest = QuestService.create_quest(
    title="Fix login bug",
    description="Resolve authentication issue",
    difficulty=QuestDifficulty.MEDIUM,
    quest_type=QuestType.DEBUG
)

team.add_quest(quest)
QuestService.assign_quest(quest, alice)
quest.start()
xp = QuestService.complete_quest(quest, team)

# Check achievements
new_achievements = AchievementService.check_achievements(team, alice)
for achievement in new_achievements:
    print(f"Unlocked: {achievement.name}")
```

---

For more examples, see the [examples](../examples/) directory.
