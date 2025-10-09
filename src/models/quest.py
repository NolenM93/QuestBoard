"""
Quest model - Represents a task or goal in the QuestBoard system
"""

from datetime import datetime
from enum import Enum
from typing import Optional, List
from dataclasses import dataclass, field


class QuestType(Enum):
    """Types of quests available"""
    BRAINSTORM = "Brainstorm"
    BUILD = "Build"
    PROMOTE = "Promote"
    DEBUG = "Debug"
    LEARN = "Learn"
    REVIEW = "Review"
    DOCUMENTATION = "Documentation"


class QuestDifficulty(Enum):
    """Quest difficulty levels"""
    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"
    EPIC = "Epic"


class QuestStatus(Enum):
    """Quest status lifecycle"""
    CREATED = "Created"
    ASSIGNED = "Assigned"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    ABANDONED = "Abandoned"


@dataclass
class Quest:
    """
    Represents a quest (task/goal) in the QuestBoard system.
    
    Attributes:
        title: Short, descriptive quest name
        description: Detailed quest information
        difficulty: Quest difficulty level
        quest_type: Category of quest
        xp_reward: Experience points awarded upon completion
        status: Current quest status
        assigned_to: Username of assigned team member
        created_at: Timestamp of quest creation
        completed_at: Timestamp of quest completion
        tags: Optional tags for categorization
    """
    title: str
    description: str
    difficulty: QuestDifficulty
    quest_type: QuestType
    xp_reward: int
    status: QuestStatus = field(default=QuestStatus.CREATED)
    assigned_to: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
    completed_at: Optional[datetime] = None
    tags: List[str] = field(default_factory=list)
    quest_id: str = field(default_factory=lambda: f"quest_{datetime.now().timestamp()}")
    
    def __post_init__(self):
        """Validate quest data after initialization"""
        if not self.title or len(self.title.strip()) == 0:
            raise ValueError("Quest title cannot be empty")
        
        if self.xp_reward < 0:
            raise ValueError("XP reward must be non-negative")
        
        # Convert string enums to proper enum types if needed
        if isinstance(self.difficulty, str):
            self.difficulty = QuestDifficulty[self.difficulty.upper()]
        
        if isinstance(self.quest_type, str):
            self.quest_type = QuestType[self.quest_type.upper().replace(" ", "_")]
        
        if isinstance(self.status, str):
            self.status = QuestStatus[self.status.upper().replace(" ", "_")]
    
    def assign_to(self, username: str) -> None:
        """
        Assign the quest to a team member.
        
        Args:
            username: Username of the team member
        """
        if not username or len(username.strip()) == 0:
            raise ValueError("Username cannot be empty")
        
        self.assigned_to = username
        if self.status == QuestStatus.CREATED:
            self.status = QuestStatus.ASSIGNED
    
    def start(self) -> None:
        """Mark the quest as in progress"""
        if self.status not in [QuestStatus.ASSIGNED, QuestStatus.CREATED]:
            raise ValueError(f"Cannot start quest with status: {self.status.value}")
        
        self.status = QuestStatus.IN_PROGRESS
    
    def complete(self) -> int:
        """
        Mark the quest as completed and return XP reward.
        
        Returns:
            XP reward amount
        """
        if self.status == QuestStatus.COMPLETED:
            raise ValueError("Quest is already completed")
        
        self.status = QuestStatus.COMPLETED
        self.completed_at = datetime.now()
        return self.xp_reward
    
    def abandon(self) -> None:
        """Mark the quest as abandoned"""
        if self.status == QuestStatus.COMPLETED:
            raise ValueError("Cannot abandon a completed quest")
        
        self.status = QuestStatus.ABANDONED
    
    def get_icon(self) -> str:
        """Get the emoji icon for this quest type"""
        icons = {
            QuestType.BRAINSTORM: "🧠",
            QuestType.BUILD: "🔧",
            QuestType.PROMOTE: "📣",
            QuestType.DEBUG: "🐛",
            QuestType.LEARN: "📚",
            QuestType.REVIEW: "👀",
            QuestType.DOCUMENTATION: "📝",
        }
        return icons.get(self.quest_type, "⭐")
    
    def to_dict(self) -> dict:
        """Convert quest to dictionary representation"""
        return {
            'quest_id': self.quest_id,
            'title': self.title,
            'description': self.description,
            'difficulty': self.difficulty.value,
            'quest_type': self.quest_type.value,
            'xp_reward': self.xp_reward,
            'status': self.status.value,
            'assigned_to': self.assigned_to,
            'created_at': self.created_at.isoformat(),
            'completed_at': self.completed_at.isoformat() if self.completed_at else None,
            'tags': self.tags,
            'icon': self.get_icon(),
        }
    
    def __str__(self) -> str:
        """String representation of the quest"""
        return f"{self.get_icon()} [{self.difficulty.value}] {self.title} ({self.xp_reward} XP)"
