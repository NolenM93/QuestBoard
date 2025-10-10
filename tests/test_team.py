"""
Tests for Team model
"""

import pytest
from src.models.team import Team, TeamMember
from src.models.mascot import Mascot, MascotType
from src.models.quest import Quest, QuestType, QuestDifficulty


def test_team_creation():
    """Test basic team creation"""
    mascot = Mascot(name="Buddy", mascot_type=MascotType.CODE_DRAGON)
    team = Team(name="Test Team", mascot=mascot)
    
    assert team.name == "Test Team"
    assert team.mascot.name == "Buddy"
    assert len(team.members) == 0
    assert len(team.quests) == 0


def test_team_factory_creation():
    """Test team creation using factory method"""
    team = Team.create(
        name="Test Team",
        mascot_name="Buddy",
        mascot_type=MascotType.CODE_DRAGON
    )
    
    assert team.name == "Test Team"
    assert team.mascot.name == "Buddy"
    assert team.mascot.mascot_type == MascotType.CODE_DRAGON


def test_add_member():
    """Test adding team members"""
    team = Team.create(
        name="Test Team",
        mascot_name="Buddy",
        mascot_type=MascotType.CODE_DRAGON
    )
    
    member = TeamMember(username="alice", display_name="Alice")
    team.add_member(member)
    
    assert len(team.members) == 1
    assert team.get_member("alice") == member


def test_add_duplicate_member_error():
    """Test that adding duplicate member raises error"""
    team = Team.create(
        name="Test Team",
        mascot_name="Buddy",
        mascot_type=MascotType.CODE_DRAGON
    )
    
    member1 = TeamMember(username="alice", display_name="Alice")
    team.add_member(member1)
    
    member2 = TeamMember(username="alice", display_name="Alice 2")
    
    with pytest.raises(ValueError, match="Member with username 'alice' already exists"):
        team.add_member(member2)


def test_get_member_not_found():
    """Test getting non-existent member returns None"""
    team = Team.create(
        name="Test Team",
        mascot_name="Buddy",
        mascot_type=MascotType.CODE_DRAGON
    )
    
    assert team.get_member("nonexistent") is None


def test_add_quest():
    """Test adding quests to team"""
    team = Team.create(
        name="Test Team",
        mascot_name="Buddy",
        mascot_type=MascotType.CODE_DRAGON
    )
    
    quest = Quest(
        title="Test Quest",
        description="A test",
        difficulty=QuestDifficulty.EASY,
        quest_type=QuestType.BUILD,
        xp_reward=25
    )
    
    team.add_quest(quest)
    
    assert len(team.quests) == 1
    assert team.get_quest(quest.quest_id) == quest


def test_get_total_xp():
    """Test calculating total team XP"""
    team = Team.create(
        name="Test Team",
        mascot_name="Buddy",
        mascot_type=MascotType.CODE_DRAGON
    )
    
    member1 = TeamMember(username="alice", display_name="Alice", total_xp=100)
    member2 = TeamMember(username="bob", display_name="Bob", total_xp=150)
    
    team.add_member(member1)
    team.add_member(member2)
    
    assert team.get_total_xp() == 250


def test_get_leaderboard():
    """Test leaderboard sorting"""
    team = Team.create(
        name="Test Team",
        mascot_name="Buddy",
        mascot_type=MascotType.CODE_DRAGON
    )
    
    member1 = TeamMember(username="alice", display_name="Alice", total_xp=50)
    member2 = TeamMember(username="bob", display_name="Bob", total_xp=150)
    member3 = TeamMember(username="charlie", display_name="Charlie", total_xp=100)
    
    team.add_member(member1)
    team.add_member(member2)
    team.add_member(member3)
    
    leaderboard = team.get_leaderboard()
    
    assert len(leaderboard) == 3
    assert leaderboard[0].username == "bob"
    assert leaderboard[1].username == "charlie"
    assert leaderboard[2].username == "alice"


def test_team_member_level_calculation():
    """Test team member level calculation"""
    member = TeamMember(username="alice", display_name="Alice", total_xp=400)
    
    # Level = floor(sqrt(400 / 100)) = floor(sqrt(4)) = 2
    assert member.get_level() == 2


def test_team_member_complete_quest():
    """Test completing a quest as team member"""
    member = TeamMember(username="alice", display_name="Alice")
    
    assert member.quests_completed == 0
    assert member.total_xp == 0
    
    member.complete_quest(50)
    
    assert member.quests_completed == 1
    assert member.total_xp == 50
