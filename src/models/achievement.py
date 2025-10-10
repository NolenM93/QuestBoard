"""
Achievement model - Represents badges and achievements in the QuestBoard system
"""

from datetime import datetime
from enum import Enum
from typing import Optional
from dataclasses import dataclass, field


class AchievementTier(Enum):
    """Achievement tiers from basic to legendary"""
    BRONZE = "Bronze"
    SILVER = "Silver"
    GOLD = "Gold"
    PLATINUM = "Platinum"
    DIAMOND = "Diamond"


class AchievementCategory(Enum):
    """Categories of achievements"""
    CONTRIBUTIONS = "Contributions"
    LEADERSHIP = "Leadership"
    CREATIVITY = "Creativity"
    CONSISTENCY = "Consistency"
    COLLABORATION = "Collaboration"
    SPEED = "Speed"
    QUALITY = "Quality"


@dataclass
class Achievement:
    """
    Represents an achievement or badge in the QuestBoard system.
    
    Attributes:
        name: Achievement name
        description: What the achievement represents
        tier: Achievement tier (Bronze to Diamond)
        category: Achievement category
        xp_requirement: XP needed to unlock
        icon: Emoji or icon representing the achievement
        unlocked_at: When the achievement was unlocked
        progress: Current progress towards unlocking (0-100)
    """
    name: str
    description: str
    tier: AchievementTier
    category: AchievementCategory
    xp_requirement: int
    icon: str = "🏆"
    unlocked_at: Optional[datetime] = None
    progress: int = 0
    achievement_id: str = field(default_factory=lambda: f"achievement_{datetime.now().timestamp()}")
    
    def __post_init__(self):
        """Validate achievement data after initialization"""
        if not self.name or len(self.name.strip()) == 0:
            raise ValueError("Achievement name cannot be empty")
        
        if self.xp_requirement < 0:
            raise ValueError("XP requirement must be non-negative")
        
        if not 0 <= self.progress <= 100:
            raise ValueError("Progress must be between 0 and 100")
        
        # Convert string enums to proper enum types if needed
        if isinstance(self.tier, str):
            self.tier = AchievementTier[self.tier.upper()]
        
        if isinstance(self.category, str):
            self.category = AchievementCategory[self.category.upper()]
    
    def unlock(self) -> None:
        """Mark the achievement as unlocked"""
        if self.is_unlocked():
            raise ValueError("Achievement is already unlocked")
        
        self.unlocked_at = datetime.now()
        self.progress = 100
    
    def is_unlocked(self) -> bool:
        """Check if the achievement is unlocked"""
        return self.unlocked_at is not None
    
    def update_progress(self, current_xp: int) -> None:
        """
        Update progress towards unlocking this achievement.
        
        Args:
            current_xp: Current XP amount
        """
        if self.is_unlocked():
            return
        
        if current_xp >= self.xp_requirement:
            self.unlock()
        else:
            self.progress = min(100, int((current_xp / self.xp_requirement) * 100))
    
    def get_tier_color(self) -> str:
        """Get the color code for this achievement tier"""
        colors = {
            AchievementTier.BRONZE: "#CD7F32",
            AchievementTier.SILVER: "#C0C0C0",
            AchievementTier.GOLD: "#FFD700",
            AchievementTier.PLATINUM: "#E5E4E2",
            AchievementTier.DIAMOND: "#B9F2FF",
        }
        return colors.get(self.tier, "#808080")
    
    def to_dict(self) -> dict:
        """Convert achievement to dictionary representation"""
        return {
            'achievement_id': self.achievement_id,
            'name': self.name,
            'description': self.description,
            'tier': self.tier.value,
            'category': self.category.value,
            'xp_requirement': self.xp_requirement,
            'icon': self.icon,
            'unlocked_at': self.unlocked_at.isoformat() if self.unlocked_at else None,
            'progress': self.progress,
            'is_unlocked': self.is_unlocked(),
            'tier_color': self.get_tier_color(),
        }
    
    def __str__(self) -> str:
        """String representation of the achievement"""
        status = "✓" if self.is_unlocked() else f"{self.progress}%"
        return f"{self.icon} [{self.tier.value}] {self.name} - {status}"


def create_default_achievements() -> list[Achievement]:
    """
    Create a set of default achievements for a new team.
    
    Returns:
        List of default Achievement objects
    """
    achievements = [
        # Contributions
        Achievement("First Steps", "Complete your first quest", 
                   AchievementTier.BRONZE, AchievementCategory.CONTRIBUTIONS, 10, "🎯"),
        Achievement("Quest Warrior", "Complete 10 quests", 
                   AchievementTier.SILVER, AchievementCategory.CONTRIBUTIONS, 50, "⚔️"),
        Achievement("Quest Master", "Complete 50 quests", 
                   AchievementTier.GOLD, AchievementCategory.CONTRIBUTIONS, 100, "👑"),
        Achievement("Legend", "Complete 100 quests", 
                   AchievementTier.PLATINUM, AchievementCategory.CONTRIBUTIONS, 250, "🌟"),
        Achievement("Mythical", "Complete 250 quests", 
                   AchievementTier.DIAMOND, AchievementCategory.CONTRIBUTIONS, 500, "💎"),
        
        # Leadership
        Achievement("Team Player", "Create your first quest", 
                   AchievementTier.BRONZE, AchievementCategory.LEADERSHIP, 10, "🤝"),
        Achievement("Quest Giver", "Create 10 quests for the team", 
                   AchievementTier.SILVER, AchievementCategory.LEADERSHIP, 50, "📋"),
        Achievement("Visionary", "Create 25 quests", 
                   AchievementTier.GOLD, AchievementCategory.LEADERSHIP, 100, "🔮"),
        
        # Consistency
        Achievement("Steady Pace", "Complete quests for 3 days in a row", 
                   AchievementTier.BRONZE, AchievementCategory.CONSISTENCY, 10, "📅"),
        Achievement("Dedicated", "Complete quests for 7 days in a row", 
                   AchievementTier.SILVER, AchievementCategory.CONSISTENCY, 50, "🔥"),
        Achievement("Unstoppable", "Complete quests for 30 days in a row", 
                   AchievementTier.GOLD, AchievementCategory.CONSISTENCY, 100, "⚡"),
        
        # Speed
        Achievement("Quick Draw", "Complete a quest within 1 hour", 
                   AchievementTier.BRONZE, AchievementCategory.SPEED, 10, "⏱️"),
        Achievement("Speed Demon", "Complete 5 quests in one day", 
                   AchievementTier.SILVER, AchievementCategory.SPEED, 50, "🚀"),
        
        # Collaboration
        Achievement("Helper", "Assist a teammate on a quest", 
                   AchievementTier.BRONZE, AchievementCategory.COLLABORATION, 10, "🤗"),
        Achievement("Team Spirit", "Collaborate on 10 quests", 
                   AchievementTier.SILVER, AchievementCategory.COLLABORATION, 50, "💪"),
    ]
    
    return achievements
