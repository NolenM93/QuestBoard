"""
XP Calculator - Utility for calculating XP rewards and requirements
"""

from ..models.quest import QuestDifficulty, QuestType


class XPCalculator:
    """Utility class for XP-related calculations"""
    
    # Base XP values by difficulty
    BASE_XP = {
        QuestDifficulty.EASY: 25,
        QuestDifficulty.MEDIUM: 50,
        QuestDifficulty.HARD: 100,
        QuestDifficulty.EPIC: 200,
    }
    
    # Type multipliers
    TYPE_MULTIPLIERS = {
        QuestType.BRAINSTORM: 1.0,
        QuestType.BUILD: 1.2,
        QuestType.PROMOTE: 0.9,
        QuestType.DEBUG: 1.3,
        QuestType.LEARN: 1.1,
        QuestType.REVIEW: 0.8,
        QuestType.DOCUMENTATION: 0.9,
    }
    
    @staticmethod
    def calculate_quest_xp(difficulty: QuestDifficulty, quest_type: QuestType,
                          bonus_multiplier: float = 1.0) -> int:
        """
        Calculate XP reward for a quest.
        
        Args:
            difficulty: Quest difficulty
            quest_type: Quest type
            bonus_multiplier: Optional bonus multiplier (e.g., 1.5 for urgent quests)
            
        Returns:
            Calculated XP value
        """
        base = XPCalculator.BASE_XP.get(difficulty, 50)
        type_mult = XPCalculator.TYPE_MULTIPLIERS.get(quest_type, 1.0)
        
        return int(base * type_mult * bonus_multiplier)
    
    @staticmethod
    def calculate_level_from_xp(xp: int) -> int:
        """
        Calculate level from total XP.
        Uses square root formula: Level = floor(sqrt(xp / 100))
        
        Args:
            xp: Total XP
            
        Returns:
            Calculated level
        """
        if xp < 0:
            return 0
        return int((xp / 100) ** 0.5)
    
    @staticmethod
    def calculate_xp_for_level(level: int) -> int:
        """
        Calculate total XP needed to reach a specific level.
        
        Args:
            level: Target level
            
        Returns:
            Total XP needed
        """
        if level < 0:
            return 0
        return (level ** 2) * 100
    
    @staticmethod
    def calculate_xp_to_next_level(current_xp: int) -> int:
        """
        Calculate XP needed to reach the next level.
        
        Args:
            current_xp: Current total XP
            
        Returns:
            XP needed for next level
        """
        current_level = XPCalculator.calculate_level_from_xp(current_xp)
        next_level_xp = XPCalculator.calculate_xp_for_level(current_level + 1)
        return next_level_xp - current_xp
    
    @staticmethod
    def calculate_progress_to_next_level(current_xp: int) -> float:
        """
        Calculate progress percentage to next level.
        
        Args:
            current_xp: Current total XP
            
        Returns:
            Progress percentage (0-100)
        """
        current_level = XPCalculator.calculate_level_from_xp(current_xp)
        current_level_xp = XPCalculator.calculate_xp_for_level(current_level)
        next_level_xp = XPCalculator.calculate_xp_for_level(current_level + 1)
        
        if next_level_xp == current_level_xp:
            return 100.0
        
        xp_into_level = current_xp - current_level_xp
        xp_needed = next_level_xp - current_level_xp
        
        return (xp_into_level / xp_needed) * 100
    
    @staticmethod
    def calculate_team_xp_multiplier(team_size: int) -> float:
        """
        Calculate XP multiplier based on team size.
        Encourages larger teams with slight bonus.
        
        Args:
            team_size: Number of team members
            
        Returns:
            Multiplier value
        """
        if team_size <= 0:
            return 1.0
        
        # Small bonus for larger teams (max 1.2x at 10+ members)
        return min(1.2, 1.0 + (team_size - 1) * 0.02)
    
    @staticmethod
    def calculate_streak_bonus(streak_days: int) -> float:
        """
        Calculate XP bonus multiplier based on consecutive activity streak.
        
        Args:
            streak_days: Number of consecutive days with activity
            
        Returns:
            Bonus multiplier
        """
        if streak_days <= 0:
            return 1.0
        
        # Bonus increases with streak, max 2x at 30 days
        bonus = 1.0 + min(streak_days * 0.033, 1.0)
        return round(bonus, 2)
