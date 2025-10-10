"""
Quest service - Business logic for quest management
"""

from typing import List, Optional
from datetime import datetime, timedelta

from ..models.quest import Quest, QuestType, QuestDifficulty, QuestStatus
from ..models.team import Team, TeamMember


class QuestService:
    """Service for managing quests and quest-related operations"""
    
    @staticmethod
    def create_quest(title: str, description: str, difficulty: QuestDifficulty,
                    quest_type: QuestType, xp_reward: Optional[int] = None,
                    tags: Optional[List[str]] = None) -> Quest:
        """
        Create a new quest with optional auto-calculated XP.
        
        Args:
            title: Quest title
            description: Quest description
            difficulty: Quest difficulty level
            quest_type: Quest type
            xp_reward: Optional XP reward (auto-calculated if not provided)
            tags: Optional tags for categorization
            
        Returns:
            New Quest instance
        """
        # Auto-calculate XP if not provided
        if xp_reward is None:
            xp_reward = QuestService.calculate_xp_reward(difficulty, quest_type)
        
        return Quest(
            title=title,
            description=description,
            difficulty=difficulty,
            quest_type=quest_type,
            xp_reward=xp_reward,
            tags=tags or []
        )
    
    @staticmethod
    def calculate_xp_reward(difficulty: QuestDifficulty, quest_type: QuestType) -> int:
        """
        Calculate XP reward based on difficulty and quest type.
        
        Args:
            difficulty: Quest difficulty
            quest_type: Quest type
            
        Returns:
            Calculated XP reward
        """
        # Base XP by difficulty
        base_xp = {
            QuestDifficulty.EASY: 25,
            QuestDifficulty.MEDIUM: 50,
            QuestDifficulty.HARD: 100,
            QuestDifficulty.EPIC: 200,
        }
        
        # Multiplier by quest type
        multipliers = {
            QuestType.BRAINSTORM: 1.0,
            QuestType.BUILD: 1.2,
            QuestType.PROMOTE: 0.9,
            QuestType.DEBUG: 1.3,
            QuestType.LEARN: 1.1,
            QuestType.REVIEW: 0.8,
            QuestType.DOCUMENTATION: 0.9,
        }
        
        xp = base_xp.get(difficulty, 50)
        multiplier = multipliers.get(quest_type, 1.0)
        
        return int(xp * multiplier)
    
    @staticmethod
    def assign_quest(quest: Quest, team_member: TeamMember) -> None:
        """
        Assign a quest to a team member.
        
        Args:
            quest: Quest to assign
            team_member: Member to assign to
        """
        quest.assign_to(team_member.username)
    
    @staticmethod
    def complete_quest(quest: Quest, team: Team) -> int:
        """
        Complete a quest and award XP to the assigned member.
        
        Args:
            quest: Quest to complete
            team: Team the quest belongs to
            
        Returns:
            XP awarded
        """
        if not quest.assigned_to:
            raise ValueError("Quest must be assigned before completion")
        
        # Mark quest as completed
        xp_reward = quest.complete()
        
        # Award XP to team member
        member = team.get_member(quest.assigned_to)
        if member:
            member.complete_quest(xp_reward)
            
            # Add XP to mascot as well
            evolved = team.mascot.add_xp(xp_reward)
            if evolved:
                print(f"🎉 {team.mascot.name} evolved to {team.mascot.evolution_stage.value}!")
        
        return xp_reward
    
    @staticmethod
    def get_quests_by_status(team: Team, status: QuestStatus) -> List[Quest]:
        """
        Get all quests with a specific status.
        
        Args:
            team: Team to search in
            status: Quest status to filter by
            
        Returns:
            List of quests with the given status
        """
        return [q for q in team.quests if q.status == status]
    
    @staticmethod
    def get_quests_by_member(team: Team, username: str) -> List[Quest]:
        """
        Get all quests assigned to a specific member.
        
        Args:
            team: Team to search in
            username: Username to filter by
            
        Returns:
            List of quests assigned to the member
        """
        return [q for q in team.quests if q.assigned_to == username]
    
    @staticmethod
    def get_quests_by_type(team: Team, quest_type: QuestType) -> List[Quest]:
        """
        Get all quests of a specific type.
        
        Args:
            team: Team to search in
            quest_type: Quest type to filter by
            
        Returns:
            List of quests of the given type
        """
        return [q for q in team.quests if q.quest_type == quest_type]
    
    @staticmethod
    def get_overdue_quests(team: Team, days_threshold: int = 7) -> List[Quest]:
        """
        Get quests that have been in progress for too long.
        
        Args:
            team: Team to search in
            days_threshold: Number of days before considering a quest overdue
            
        Returns:
            List of overdue quests
        """
        cutoff_date = datetime.now() - timedelta(days=days_threshold)
        
        return [
            q for q in team.quests
            if q.status == QuestStatus.IN_PROGRESS
            and q.created_at < cutoff_date
        ]
    
    @staticmethod
    def suggest_quest_breakdown(quest_title: str) -> List[dict]:
        """
        AI-assisted suggestion for breaking down a large quest into smaller ones.
        This is a simplified version; in production, this could use an LLM.
        
        Args:
            quest_title: Title of the large quest
            
        Returns:
            List of suggested sub-quests
        """
        # Common patterns for quest breakdown
        if "implement" in quest_title.lower() or "build" in quest_title.lower():
            return [
                {
                    "title": f"Design architecture for {quest_title}",
                    "difficulty": QuestDifficulty.MEDIUM,
                    "quest_type": QuestType.BRAINSTORM,
                },
                {
                    "title": f"Implement core functionality for {quest_title}",
                    "difficulty": QuestDifficulty.HARD,
                    "quest_type": QuestType.BUILD,
                },
                {
                    "title": f"Write tests for {quest_title}",
                    "difficulty": QuestDifficulty.MEDIUM,
                    "quest_type": QuestType.BUILD,
                },
                {
                    "title": f"Document {quest_title}",
                    "difficulty": QuestDifficulty.EASY,
                    "quest_type": QuestType.DOCUMENTATION,
                },
            ]
        
        # Default breakdown
        return [
            {
                "title": f"Research: {quest_title}",
                "difficulty": QuestDifficulty.EASY,
                "quest_type": QuestType.LEARN,
            },
            {
                "title": f"Execute: {quest_title}",
                "difficulty": QuestDifficulty.MEDIUM,
                "quest_type": QuestType.BUILD,
            },
            {
                "title": f"Review: {quest_title}",
                "difficulty": QuestDifficulty.EASY,
                "quest_type": QuestType.REVIEW,
            },
        ]
