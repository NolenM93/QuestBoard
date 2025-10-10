"""
Tests for Quest model
"""

import pytest
from datetime import datetime
from src.models.quest import Quest, QuestType, QuestDifficulty, QuestStatus


def test_quest_creation():
    """Test basic quest creation"""
    quest = Quest(
        title="Test Quest",
        description="A test quest",
        difficulty=QuestDifficulty.EASY,
        quest_type=QuestType.BUILD,
        xp_reward=25
    )
    
    assert quest.title == "Test Quest"
    assert quest.difficulty == QuestDifficulty.EASY
    assert quest.quest_type == QuestType.BUILD
    assert quest.xp_reward == 25
    assert quest.status == QuestStatus.CREATED


def test_quest_assignment():
    """Test quest assignment"""
    quest = Quest(
        title="Test Quest",
        description="A test quest",
        difficulty=QuestDifficulty.EASY,
        quest_type=QuestType.BUILD,
        xp_reward=25
    )
    
    quest.assign_to("alice")
    
    assert quest.assigned_to == "alice"
    assert quest.status == QuestStatus.ASSIGNED


def test_quest_start():
    """Test starting a quest"""
    quest = Quest(
        title="Test Quest",
        description="A test quest",
        difficulty=QuestDifficulty.EASY,
        quest_type=QuestType.BUILD,
        xp_reward=25
    )
    
    quest.assign_to("alice")
    quest.start()
    
    assert quest.status == QuestStatus.IN_PROGRESS


def test_quest_completion():
    """Test completing a quest"""
    quest = Quest(
        title="Test Quest",
        description="A test quest",
        difficulty=QuestDifficulty.EASY,
        quest_type=QuestType.BUILD,
        xp_reward=25
    )
    
    quest.assign_to("alice")
    quest.start()
    xp = quest.complete()
    
    assert quest.status == QuestStatus.COMPLETED
    assert xp == 25
    assert quest.completed_at is not None


def test_quest_empty_title_error():
    """Test that empty title raises error"""
    with pytest.raises(ValueError, match="Quest title cannot be empty"):
        Quest(
            title="",
            description="A test quest",
            difficulty=QuestDifficulty.EASY,
            quest_type=QuestType.BUILD,
            xp_reward=25
        )


def test_quest_negative_xp_error():
    """Test that negative XP raises error"""
    with pytest.raises(ValueError, match="XP reward must be non-negative"):
        Quest(
            title="Test Quest",
            description="A test quest",
            difficulty=QuestDifficulty.EASY,
            quest_type=QuestType.BUILD,
            xp_reward=-10
        )


def test_quest_get_icon():
    """Test quest icon retrieval"""
    quest = Quest(
        title="Test Quest",
        description="A test quest",
        difficulty=QuestDifficulty.EASY,
        quest_type=QuestType.BUILD,
        xp_reward=25
    )
    
    icon = quest.get_icon()
    assert icon == "🔧"


def test_quest_to_dict():
    """Test quest dictionary conversion"""
    quest = Quest(
        title="Test Quest",
        description="A test quest",
        difficulty=QuestDifficulty.EASY,
        quest_type=QuestType.BUILD,
        xp_reward=25,
        tags=["test", "example"]
    )
    
    quest_dict = quest.to_dict()
    
    assert quest_dict['title'] == "Test Quest"
    assert quest_dict['difficulty'] == "Easy"
    assert quest_dict['quest_type'] == "Build"
    assert quest_dict['xp_reward'] == 25
    assert quest_dict['status'] == "Created"
    assert quest_dict['tags'] == ["test", "example"]
    assert quest_dict['icon'] == "🔧"
