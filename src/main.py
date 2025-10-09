"""
QuestBoard - Main application entry point
"""

from src.models.team import Team, TeamMember
from src.models.quest import Quest, QuestType, QuestDifficulty
from src.models.mascot import MascotType
from src.services.quest_service import QuestService
from src.services.achievement_service import AchievementService
from src.services.mascot_service import MascotService
from src.utils.ai_assistant import AIAssistant


def create_demo_team():
    """Create a demo team to showcase QuestBoard functionality"""
    
    print("🎮 Welcome to QuestBoard - Gamified Team Progress Tracker!\n")
    
    # Create a team with mascot
    print("Creating team...")
    team = Team.create(
        name="Demo Squad",
        mascot_name="Codey",
        mascot_type=MascotType.CODE_DRAGON,
        description="A demo team showcasing QuestBoard features"
    )
    print(f"✓ Team created: {team}\n")
    
    # Initialize achievements
    print("Initializing achievements...")
    AchievementService.initialize_team_achievements(team)
    print(f"✓ {len(team.achievements)} achievements initialized\n")
    
    # Add team members
    print("Adding team members...")
    members = [
        TeamMember(username="alice", display_name="Alice", role="Developer", avatar="👩‍💻"),
        TeamMember(username="bob", display_name="Bob", role="Designer", avatar="👨‍🎨"),
        TeamMember(username="charlie", display_name="Charlie", role="Manager", avatar="👨‍💼"),
    ]
    
    for member in members:
        team.add_member(member)
        print(f"  ✓ Added {member}")
    print()
    
    # Create some quests
    print("Creating quests...")
    quests = [
        QuestService.create_quest(
            title="Set up project repository",
            description="Initialize Git repo, add README and .gitignore",
            difficulty=QuestDifficulty.EASY,
            quest_type=QuestType.BUILD,
            tags=["setup", "git"]
        ),
        QuestService.create_quest(
            title="Design system architecture",
            description="Create high-level architecture diagram",
            difficulty=QuestDifficulty.MEDIUM,
            quest_type=QuestType.BRAINSTORM,
            tags=["architecture", "planning"]
        ),
        QuestService.create_quest(
            title="Implement user authentication",
            description="Build secure OAuth2 authentication flow",
            difficulty=QuestDifficulty.HARD,
            quest_type=QuestType.BUILD,
            tags=["security", "backend"]
        ),
    ]
    
    for quest in quests:
        team.add_quest(quest)
        print(f"  ✓ Created: {quest}")
    print()
    
    # Assign and complete some quests
    print("Assigning and completing quests...")
    
    # Quest 1: Alice
    quest1 = quests[0]
    QuestService.assign_quest(quest1, members[0])
    quest1.start()
    print(f"  ✓ Assigned '{quest1.title}' to {members[0].display_name}")
    
    xp_earned = QuestService.complete_quest(quest1, team)
    print(f"  ✓ {members[0].display_name} completed quest and earned {xp_earned} XP!")
    
    # Check for new achievements
    new_achievements = AchievementService.check_achievements(team, members[0])
    if new_achievements:
        print(f"  🏆 New achievements unlocked:")
        for achievement in new_achievements:
            print(f"     {achievement}")
    print()
    
    # Quest 2: Bob
    quest2 = quests[1]
    QuestService.assign_quest(quest2, members[1])
    quest2.start()
    print(f"  ✓ Assigned '{quest2.title}' to {members[1].display_name}")
    
    xp_earned = QuestService.complete_quest(quest2, team)
    print(f"  ✓ {members[1].display_name} completed quest and earned {xp_earned} XP!")
    print()
    
    # Show team stats
    print("=" * 60)
    print("📊 TEAM STATISTICS")
    print("=" * 60)
    print(f"Team Name: {team.name}")
    print(f"Mascot: {team.mascot}")
    print(f"Total Team XP: {team.get_total_xp()}")
    print(f"Quests Completed: {team.get_total_quests_completed()}/{len(team.quests)}")
    print(f"Active Members: {len(team.members)}")
    print()
    
    # Show leaderboard
    print("🏆 LEADERBOARD")
    print("-" * 60)
    for i, member in enumerate(team.get_leaderboard(), 1):
        print(f"{i}. {member}")
    print()
    
    # Show mascot evolution
    print("🦉 MASCOT STATUS")
    print("-" * 60)
    mascot_stats = MascotService.get_mascot_stats(team.mascot)
    print(f"Name: {mascot_stats['name']}")
    print(f"Type: {mascot_stats['type']} {mascot_stats['emoji']}")
    print(f"Evolution Stage: {mascot_stats['evolution_stage']}")
    print(f"Total XP: {mascot_stats['total_xp']}")
    print(f"XP to Next Stage: {mascot_stats['xp_to_next_stage']}")
    print()
    
    # Show AI suggestions
    print("🤖 AI ASSISTANT SUGGESTIONS")
    print("-" * 60)
    print(AIAssistant.generate_motivational_message(team))
    print()
    
    # Suggest quest breakdown
    print("Quest breakdown suggestion for 'Build mobile app':")
    breakdown = AIAssistant.suggest_quest_breakdown("Build mobile app", "Create iOS and Android app")
    for i, sub_quest in enumerate(breakdown, 1):
        print(f"  {i}. {sub_quest['title']} [{sub_quest['difficulty'].value}] {sub_quest['quest_type'].value}")
    print()
    
    # Team health analysis
    print("Team Health Analysis:")
    health = AIAssistant.analyze_team_health(team)
    print(f"  Health Score: {health['health_score']}/100")
    print(f"  Completion Rate: {health['completion_rate']}%")
    print(f"  Recommendations:")
    for rec in health['recommendations']:
        print(f"    • {rec}")
    print()
    
    # Show achievement progress
    achievement_progress = AchievementService.get_progress_summary(team)
    print("🏅 ACHIEVEMENT PROGRESS")
    print("-" * 60)
    print(f"Unlocked: {achievement_progress['unlocked']}/{achievement_progress['total_achievements']}")
    print(f"Completion: {achievement_progress['completion_percentage']:.1f}%")
    print()
    
    print("=" * 60)
    print("✨ Demo complete! Start using QuestBoard for your team!")
    print("=" * 60)


def main():
    """Main application entry point"""
    try:
        create_demo_team()
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
