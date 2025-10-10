"""
Team model - Represents teams and team members in the QuestBoard system
"""

from datetime import datetime
from typing import Optional, List
from dataclasses import dataclass, field

from .quest import Quest
from .achievement import Achievement
from .mascot import Mascot, MascotType


@dataclass
class TeamMember:
    """
    Represents a member of a team.
    
    Attributes:
        username: Unique username
        display_name: Display name
        role: Team role (e.g., Developer, Designer, Manager)
        total_xp: Total XP earned
        quests_completed: Number of quests completed
        joined_at: When the member joined
    """
    username: str
    display_name: str
    role: str = "Member"
    total_xp: int = 0
    quests_completed: int = 0
    joined_at: datetime = field(default_factory=datetime.now)
    avatar: str = "👤"
    
    def __post_init__(self):
        """Validate team member data after initialization"""
        if not self.username or len(self.username.strip()) == 0:
            raise ValueError("Username cannot be empty")
        
        if self.total_xp < 0:
            raise ValueError("Total XP must be non-negative")
        
        if self.quests_completed < 0:
            raise ValueError("Quests completed must be non-negative")
    
    def add_xp(self, xp: int) -> None:
        """
        Add XP to the team member.
        
        Args:
            xp: Amount of XP to add
        """
        if xp < 0:
            raise ValueError("Cannot add negative XP")
        
        self.total_xp += xp
    
    def complete_quest(self, xp_reward: int) -> None:
        """
        Mark a quest as completed for this member.
        
        Args:
            xp_reward: XP reward from the quest
        """
        self.quests_completed += 1
        self.add_xp(xp_reward)
    
    def get_level(self) -> int:
        """
        Calculate member level based on total XP.
        
        Returns:
            Current level
        """
        # Level = floor(sqrt(total_xp / 100))
        return int((self.total_xp / 100) ** 0.5)
    
    def to_dict(self) -> dict:
        """Convert team member to dictionary representation"""
        return {
            'username': self.username,
            'display_name': self.display_name,
            'role': self.role,
            'total_xp': self.total_xp,
            'quests_completed': self.quests_completed,
            'level': self.get_level(),
            'joined_at': self.joined_at.isoformat(),
            'avatar': self.avatar,
        }
    
    def __str__(self) -> str:
        """String representation of the team member"""
        return f"{self.avatar} {self.display_name} (Level {self.get_level()}) - {self.total_xp} XP"


@dataclass
class Team:
    """
    Represents a team using QuestBoard.
    
    Attributes:
        name: Team name
        mascot: Team mascot
        members: List of team members
        quests: List of all quests
        achievements: List of team achievements
        created_at: When the team was created
        description: Team description
    """
    name: str
    mascot: Mascot
    members: List[TeamMember] = field(default_factory=list)
    quests: List[Quest] = field(default_factory=list)
    achievements: List[Achievement] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    description: str = ""
    team_id: str = field(default_factory=lambda: f"team_{datetime.now().timestamp()}")
    
    def __post_init__(self):
        """Validate team data after initialization"""
        if not self.name or len(self.name.strip()) == 0:
            raise ValueError("Team name cannot be empty")
    
    @classmethod
    def create(cls, name: str, mascot_name: str, mascot_type: MascotType, 
               description: str = "") -> 'Team':
        """
        Factory method to create a new team with a mascot.
        
        Args:
            name: Team name
            mascot_name: Name for the mascot
            mascot_type: Type of mascot
            description: Team description
            
        Returns:
            New Team instance
        """
        mascot = Mascot(name=mascot_name, mascot_type=mascot_type)
        return cls(name=name, mascot=mascot, description=description)
    
    def add_member(self, member: TeamMember) -> None:
        """
        Add a member to the team.
        
        Args:
            member: TeamMember to add
        """
        if any(m.username == member.username for m in self.members):
            raise ValueError(f"Member with username '{member.username}' already exists")
        
        self.members.append(member)
    
    def get_member(self, username: str) -> Optional[TeamMember]:
        """
        Get a team member by username.
        
        Args:
            username: Username to search for
            
        Returns:
            TeamMember if found, None otherwise
        """
        for member in self.members:
            if member.username == username:
                return member
        return None
    
    def add_quest(self, quest: Quest) -> None:
        """
        Add a quest to the team.
        
        Args:
            quest: Quest to add
        """
        self.quests.append(quest)
    
    def get_quest(self, quest_id: str) -> Optional[Quest]:
        """
        Get a quest by ID.
        
        Args:
            quest_id: Quest ID to search for
            
        Returns:
            Quest if found, None otherwise
        """
        for quest in self.quests:
            if quest.quest_id == quest_id:
                return quest
        return None
    
    def get_total_xp(self) -> int:
        """
        Calculate total XP earned by the team.
        
        Returns:
            Total team XP
        """
        return sum(member.total_xp for member in self.members)
    
    def get_total_quests_completed(self) -> int:
        """
        Calculate total quests completed by the team.
        
        Returns:
            Total completed quests
        """
        return sum(member.quests_completed for member in self.members)
    
    def get_active_quests(self) -> List[Quest]:
        """
        Get all active (non-completed, non-abandoned) quests.
        
        Returns:
            List of active quests
        """
        from .quest import QuestStatus
        return [q for q in self.quests if q.status not in 
                [QuestStatus.COMPLETED, QuestStatus.ABANDONED]]
    
    def get_leaderboard(self) -> List[TeamMember]:
        """
        Get team members sorted by XP (leaderboard).
        
        Returns:
            List of members sorted by XP (highest first)
        """
        return sorted(self.members, key=lambda m: m.total_xp, reverse=True)
    
    def to_dict(self) -> dict:
        """Convert team to dictionary representation"""
        return {
            'team_id': self.team_id,
            'name': self.name,
            'description': self.description,
            'mascot': self.mascot.to_dict(),
            'members': [m.to_dict() for m in self.members],
            'total_xp': self.get_total_xp(),
            'total_quests_completed': self.get_total_quests_completed(),
            'active_quests': len(self.get_active_quests()),
            'created_at': self.created_at.isoformat(),
        }
    
    def __str__(self) -> str:
        """String representation of the team"""
        return f"Team '{self.name}' with {self.mascot.name} - {len(self.members)} members, {self.get_total_xp()} XP"
