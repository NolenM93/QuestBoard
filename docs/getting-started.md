# Getting Started with QuestBoard

Welcome to QuestBoard! This guide will help you set up and start using QuestBoard for your team.

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/NolenM93/QuestBoard.git
   cd QuestBoard
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the demo**
   ```bash
   python -m src.main
   ```

## Quick Start

### Creating Your First Team

```python
from src.models.team import Team, TeamMember
from src.models.mascot import MascotType

# Create a team with a mascot
team = Team.create(
    name="My Awesome Team",
    mascot_name="Buddy",
    mascot_type=MascotType.CYBER_SLOTH,
    description="Building amazing things together"
)

# Add team members
team.add_member(TeamMember(
    username="john",
    display_name="John Doe",
    role="Developer"
))
```

### Creating Your First Quest

```python
from src.models.quest import QuestType, QuestDifficulty
from src.services.quest_service import QuestService

# Create a quest
quest = QuestService.create_quest(
    title="Set up development environment",
    description="Install all necessary tools and dependencies",
    difficulty=QuestDifficulty.EASY,
    quest_type=QuestType.BUILD,
    tags=["setup", "onboarding"]
)

# Add quest to team
team.add_quest(quest)
```

### Assigning and Completing Quests

```python
# Assign quest to a member
member = team.get_member("john")
QuestService.assign_quest(quest, member)

# Start working on the quest
quest.start()

# Complete the quest
xp_earned = QuestService.complete_quest(quest, team)
print(f"Earned {xp_earned} XP!")
```

### Tracking Achievements

```python
from src.services.achievement_service import AchievementService

# Initialize team achievements
AchievementService.initialize_team_achievements(team)

# Check for new achievements after completing quests
new_achievements = AchievementService.check_achievements(team, member)

for achievement in new_achievements:
    print(f"🏆 Unlocked: {achievement.name}")
```

## Understanding Core Concepts

### Quest Types

QuestBoard supports 7 quest types:

- 🧠 **Brainstorm**: Ideation and planning
- 🔧 **Build**: Implementation and construction
- 📣 **Promote**: Marketing and communication
- 🐛 **Debug**: Bug fixing and troubleshooting
- 📚 **Learn**: Research and skill development
- 👀 **Review**: Code review and QA
- 📝 **Documentation**: Writing docs and guides

### Difficulty Levels

- **Easy** (25 XP): Quick tasks, 1-2 hours
- **Medium** (50 XP): Moderate tasks, half-day
- **Hard** (100 XP): Complex tasks, 1-2 days
- **Epic** (200 XP): Major undertakings, 3+ days

### Achievement Tiers

- 🥉 **Bronze**: First steps (10 XP)
- 🥈 **Silver**: Growing skills (50 XP)
- 🥇 **Gold**: Mastery (100 XP)
- 💎 **Platinum**: Elite (250 XP)
- 💠 **Diamond**: Legendary (500 XP)

### Mascot Evolution

Your team mascot evolves as you earn XP:

1. **Egg** (0 XP): Just starting
2. **Hatchling** (100 XP): First steps
3. **Juvenile** (500 XP): Growing strong
4. **Adult** (1,000 XP): Fully developed
5. **Elder** (2,000 XP): Wise and experienced
6. **Legendary** (5,000 XP): Ultimate form

## Using the AI Assistant

```python
from src.utils.ai_assistant import AIAssistant

# Get quest breakdown suggestions
breakdown = AIAssistant.suggest_quest_breakdown(
    "Implement user authentication",
    "Build secure login system"
)

# Get motivational message
message = AIAssistant.generate_motivational_message(team)

# Analyze team health
health = AIAssistant.analyze_team_health(team)
print(f"Health Score: {health['health_score']}/100")
```

## Best Practices

### 1. Break Down Large Tasks
- Use the AI assistant to break epic quests into smaller ones
- Each quest should be completable within a reasonable timeframe
- Smaller quests = more frequent wins and motivation

### 2. Regular Check-ins
- Review team progress weekly
- Celebrate completed quests and achievements
- Adjust quest difficulty based on team capacity

### 3. Balance Quest Types
- Mix different quest types for variety
- Include learning and documentation quests
- Don't neglect review and debugging tasks

### 4. Engage the Whole Team
- Ensure everyone has assigned quests
- Use the leaderboard to recognize top contributors
- Create collaborative quests for team bonding

### 5. Customize Your Experience
- Choose a mascot that represents your team
- Apply seasonal skins to keep things fresh
- Create custom achievements for team-specific goals

## Next Steps

- Read the [Quest Guide](quest-guide.md) for detailed quest management
- Check out the [Example Configurations](../examples/) for team templates
- Explore the codebase to extend QuestBoard for your needs

## Getting Help

- **Issues**: Report bugs on GitHub Issues
- **Discussions**: Ask questions in GitHub Discussions
- **Documentation**: Full API reference in [api-reference.md](api-reference.md)

Happy questing! 🎮✨
