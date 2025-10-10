"""
Achievement service - Business logic for achievement management
"""

from typing import List
from datetime import datetime, timedelta

from ..models.achievement import Achievement, AchievementTier, AchievementCategory, create_default_achievements
from ..models.team import Team, TeamMember
from ..models.quest import QuestStatus


class AchievementService:
    """Service for managing achievements and tracking progress"""
    
    @staticmethod
    def initialize_team_achievements(team: Team) -> None:
        """
        Initialize a team with default achievements.
        
        Args:
            team: Team to initialize
        """
        team.achievements = create_default_achievements()
    
    @staticmethod
    def check_achievements(team: Team, member: TeamMember) -> List[Achievement]:
        """
        Check and unlock achievements for a team member.
        
        Args:
            team: Team the member belongs to
            member: Team member to check achievements for
            
        Returns:
            List of newly unlocked achievements
        """
        newly_unlocked = []
        
        for achievement in team.achievements:
            if achievement.is_unlocked():
                continue
            
            # Check if achievement should be unlocked
            should_unlock = False
            
            if achievement.category == AchievementCategory.CONTRIBUTIONS:
                # Check based on XP
                if member.total_xp >= achievement.xp_requirement:
                    should_unlock = True
                else:
                    achievement.update_progress(member.total_xp)
            
            elif achievement.category == AchievementCategory.LEADERSHIP:
                # Check based on quests created
                quests_created = AchievementService._count_quests_created_by_member(team, member)
                if quests_created >= achievement.xp_requirement / 10:  # Simplified logic
                    should_unlock = True
            
            elif achievement.category == AchievementCategory.CONSISTENCY:
                # Check based on streak
                streak = AchievementService._calculate_streak(team, member)
                required_days = {
                    "Steady Pace": 3,
                    "Dedicated": 7,
                    "Unstoppable": 30,
                }.get(achievement.name, 3)
                
                if streak >= required_days:
                    should_unlock = True
            
            elif achievement.category == AchievementCategory.SPEED:
                # Check based on quest completion speed
                if AchievementService._check_speed_achievement(team, member, achievement.name):
                    should_unlock = True
            
            elif achievement.category == AchievementCategory.COLLABORATION:
                # Check based on team collaboration
                if member.quests_completed >= achievement.xp_requirement / 10:
                    should_unlock = True
            
            if should_unlock:
                achievement.unlock()
                newly_unlocked.append(achievement)
        
        return newly_unlocked
    
    @staticmethod
    def _count_quests_created_by_member(team: Team, member: TeamMember) -> int:
        """Count quests created by a specific member (simplified)"""
        # In a full implementation, Quest would have a 'created_by' field
        return 0
    
    @staticmethod
    def _calculate_streak(team: Team, member: TeamMember) -> int:
        """
        Calculate the current streak of consecutive days with quest completions.
        
        Args:
            team: Team to check
            member: Team member to check
            
        Returns:
            Number of consecutive days with completions
        """
        # Get completed quests by this member
        member_quests = [
            q for q in team.quests
            if q.assigned_to == member.username and q.status == QuestStatus.COMPLETED
        ]
        
        if not member_quests:
            return 0
        
        # Sort by completion date
        sorted_quests = sorted(member_quests, key=lambda q: q.completed_at or datetime.min, reverse=True)
        
        streak = 0
        current_date = datetime.now().date()
        
        for quest in sorted_quests:
            if quest.completed_at is None:
                continue
            
            quest_date = quest.completed_at.date()
            
            if quest_date == current_date or quest_date == current_date - timedelta(days=1):
                streak += 1
                current_date = quest_date
            else:
                break
        
        return streak
    
    @staticmethod
    def _check_speed_achievement(team: Team, member: TeamMember, achievement_name: str) -> bool:
        """
        Check if member qualifies for a speed-based achievement.
        
        Args:
            team: Team to check
            member: Team member to check
            achievement_name: Name of the achievement
            
        Returns:
            True if member qualifies
        """
        member_quests = [
            q for q in team.quests
            if q.assigned_to == member.username and q.status == QuestStatus.COMPLETED
        ]
        
        if achievement_name == "Quick Draw":
            # Complete a quest within 1 hour
            for quest in member_quests:
                if quest.completed_at and quest.created_at:
                    duration = quest.completed_at - quest.created_at
                    if duration <= timedelta(hours=1):
                        return True
        
        elif achievement_name == "Speed Demon":
            # Complete 5 quests in one day
            from collections import defaultdict
            quests_by_date = defaultdict(int)
            
            for quest in member_quests:
                if quest.completed_at:
                    date = quest.completed_at.date()
                    quests_by_date[date] += 1
            
            return any(count >= 5 for count in quests_by_date.values())
        
        return False
    
    @staticmethod
    def get_achievements_by_tier(team: Team, tier: AchievementTier) -> List[Achievement]:
        """
        Get all achievements of a specific tier.
        
        Args:
            team: Team to search in
            tier: Achievement tier
            
        Returns:
            List of achievements with the given tier
        """
        return [a for a in team.achievements if a.tier == tier]
    
    @staticmethod
    def get_achievements_by_category(team: Team, category: AchievementCategory) -> List[Achievement]:
        """
        Get all achievements of a specific category.
        
        Args:
            team: Team to search in
            category: Achievement category
            
        Returns:
            List of achievements with the given category
        """
        return [a for a in team.achievements if a.category == category]
    
    @staticmethod
    def get_unlocked_achievements(team: Team) -> List[Achievement]:
        """
        Get all unlocked achievements for the team.
        
        Args:
            team: Team to check
            
        Returns:
            List of unlocked achievements
        """
        return [a for a in team.achievements if a.is_unlocked()]
    
    @staticmethod
    def get_progress_summary(team: Team) -> dict:
        """
        Get a summary of achievement progress for the team.
        
        Args:
            team: Team to summarize
            
        Returns:
            Dictionary with progress statistics
        """
        total_achievements = len(team.achievements)
        unlocked = len(AchievementService.get_unlocked_achievements(team))
        
        by_tier = {}
        for tier in AchievementTier:
            tier_achievements = AchievementService.get_achievements_by_tier(team, tier)
            unlocked_tier = [a for a in tier_achievements if a.is_unlocked()]
            by_tier[tier.value] = {
                'total': len(tier_achievements),
                'unlocked': len(unlocked_tier),
            }
        
        return {
            'total_achievements': total_achievements,
            'unlocked': unlocked,
            'locked': total_achievements - unlocked,
            'completion_percentage': (unlocked / total_achievements * 100) if total_achievements > 0 else 0,
            'by_tier': by_tier,
        }
