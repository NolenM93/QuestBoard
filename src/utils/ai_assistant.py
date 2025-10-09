"""
AI Assistant - Provides intelligent suggestions and guidance
"""

from typing import List, Dict
from datetime import datetime, timedelta

from ..models.quest import Quest, QuestType, QuestDifficulty
from ..models.team import Team, TeamMember


class AIAssistant:
    """AI-powered assistant for team guidance and suggestions"""
    
    @staticmethod
    def suggest_quest_breakdown(title: str, description: str = "") -> List[Dict]:
        """
        Suggest how to break down a large quest into smaller ones.
        
        Args:
            title: Quest title
            description: Quest description
            
        Returns:
            List of suggested sub-quests
        """
        suggestions = []
        title_lower = title.lower()
        desc_lower = description.lower()
        
        # Detect project type
        if any(word in title_lower for word in ["implement", "build", "create", "develop"]):
            suggestions.extend([
                {
                    "title": f"Design: {title}",
                    "description": "Create architecture and design documents",
                    "difficulty": QuestDifficulty.MEDIUM,
                    "quest_type": QuestType.BRAINSTORM,
                },
                {
                    "title": f"Core Implementation: {title}",
                    "description": "Implement main functionality",
                    "difficulty": QuestDifficulty.HARD,
                    "quest_type": QuestType.BUILD,
                },
                {
                    "title": f"Testing: {title}",
                    "description": "Write and run tests",
                    "difficulty": QuestDifficulty.MEDIUM,
                    "quest_type": QuestType.BUILD,
                },
                {
                    "title": f"Documentation: {title}",
                    "description": "Write documentation and examples",
                    "difficulty": QuestDifficulty.EASY,
                    "quest_type": QuestType.DOCUMENTATION,
                },
            ])
        
        elif any(word in title_lower for word in ["fix", "debug", "resolve"]):
            suggestions.extend([
                {
                    "title": f"Investigate: {title}",
                    "description": "Reproduce and diagnose the issue",
                    "difficulty": QuestDifficulty.MEDIUM,
                    "quest_type": QuestType.DEBUG,
                },
                {
                    "title": f"Fix: {title}",
                    "description": "Implement the fix",
                    "difficulty": QuestDifficulty.HARD,
                    "quest_type": QuestType.BUILD,
                },
                {
                    "title": f"Verify: {title}",
                    "description": "Test the fix and ensure no regressions",
                    "difficulty": QuestDifficulty.EASY,
                    "quest_type": QuestType.REVIEW,
                },
            ])
        
        elif any(word in title_lower for word in ["research", "learn", "explore"]):
            suggestions.extend([
                {
                    "title": f"Research: {title}",
                    "description": "Gather information and resources",
                    "difficulty": QuestDifficulty.EASY,
                    "quest_type": QuestType.LEARN,
                },
                {
                    "title": f"Summarize findings: {title}",
                    "description": "Create summary document",
                    "difficulty": QuestDifficulty.EASY,
                    "quest_type": QuestType.DOCUMENTATION,
                },
                {
                    "title": f"Present: {title}",
                    "description": "Share findings with team",
                    "difficulty": QuestDifficulty.EASY,
                    "quest_type": QuestType.PROMOTE,
                },
            ])
        
        else:
            # Default breakdown
            suggestions.extend([
                {
                    "title": f"Plan: {title}",
                    "description": "Define approach and requirements",
                    "difficulty": QuestDifficulty.EASY,
                    "quest_type": QuestType.BRAINSTORM,
                },
                {
                    "title": f"Execute: {title}",
                    "description": "Complete the main work",
                    "difficulty": QuestDifficulty.MEDIUM,
                    "quest_type": QuestType.BUILD,
                },
                {
                    "title": f"Review: {title}",
                    "description": "Review and finalize",
                    "difficulty": QuestDifficulty.EASY,
                    "quest_type": QuestType.REVIEW,
                },
            ])
        
        return suggestions
    
    @staticmethod
    def suggest_next_quest(team: Team, member: TeamMember) -> List[Quest]:
        """
        Suggest next quests for a team member based on their history.
        
        Args:
            team: Team the member belongs to
            member: Team member to suggest for
            
        Returns:
            List of suggested quests
        """
        from ..models.quest import QuestStatus
        
        # Get available quests (not completed or abandoned)
        available_quests = [
            q for q in team.quests
            if q.status not in [QuestStatus.COMPLETED, QuestStatus.ABANDONED]
            and q.assigned_to is None
        ]
        
        if not available_quests:
            return []
        
        # Sort by difficulty (easier first if new member)
        if member.quests_completed < 5:
            available_quests.sort(key=lambda q: q.difficulty.value)
        
        return available_quests[:3]
    
    @staticmethod
    def generate_motivational_message(team: Team) -> str:
        """
        Generate a motivational message based on team performance.
        
        Args:
            team: Team to generate message for
            
        Returns:
            Motivational message
        """
        total_xp = team.get_total_xp()
        completed = team.get_total_quests_completed()
        
        if total_xp == 0:
            return f"🎯 Welcome to QuestBoard, {team.name}! Your adventure begins now!"
        
        if completed < 5:
            return f"💪 Keep going, {team.name}! You've completed {completed} quests. Great start!"
        
        if completed < 20:
            return f"🔥 {team.name} is on fire! {completed} quests completed and counting!"
        
        if completed < 50:
            return f"⭐ Amazing progress, {team.name}! You're a quest-crushing machine!"
        
        return f"🏆 Legendary team alert! {team.name} has completed {completed} quests. Unstoppable!"
    
    @staticmethod
    def suggest_onboarding_quests(team_name: str) -> List[Dict]:
        """
        Generate onboarding quests for a new team or member.
        
        Args:
            team_name: Name of the team
            
        Returns:
            List of onboarding quest suggestions
        """
        return [
            {
                "title": f"Welcome to {team_name}!",
                "description": "Complete this quest to get started with QuestBoard",
                "difficulty": QuestDifficulty.EASY,
                "quest_type": QuestType.LEARN,
                "xp_reward": 10,
            },
            {
                "title": "Meet the team",
                "description": "Introduce yourself to all team members",
                "difficulty": QuestDifficulty.EASY,
                "quest_type": QuestType.BRAINSTORM,
                "xp_reward": 15,
            },
            {
                "title": "Complete your first real quest",
                "description": "Pick and complete your first team quest",
                "difficulty": QuestDifficulty.MEDIUM,
                "quest_type": QuestType.BUILD,
                "xp_reward": 50,
            },
            {
                "title": "Help a teammate",
                "description": "Collaborate on a quest with another team member",
                "difficulty": QuestDifficulty.EASY,
                "quest_type": QuestType.REVIEW,
                "xp_reward": 25,
            },
        ]
    
    @staticmethod
    def analyze_team_health(team: Team) -> Dict:
        """
        Analyze team health and provide insights.
        
        Args:
            team: Team to analyze
            
        Returns:
            Dictionary with health metrics and recommendations
        """
        from ..models.quest import QuestStatus
        
        total_quests = len(team.quests)
        completed = len([q for q in team.quests if q.status == QuestStatus.COMPLETED])
        in_progress = len([q for q in team.quests if q.status == QuestStatus.IN_PROGRESS])
        abandoned = len([q for q in team.quests if q.status == QuestStatus.ABANDONED])
        
        completion_rate = (completed / total_quests * 100) if total_quests > 0 else 0
        abandonment_rate = (abandoned / total_quests * 100) if total_quests > 0 else 0
        
        health_score = 0
        recommendations = []
        
        # Calculate health score
        if completion_rate > 70:
            health_score += 40
        elif completion_rate > 50:
            health_score += 30
        else:
            health_score += 10
            recommendations.append("Try to complete more quests to improve team momentum")
        
        if abandonment_rate < 10:
            health_score += 30
        elif abandonment_rate < 20:
            health_score += 20
        else:
            health_score += 5
            recommendations.append("High abandonment rate detected. Consider breaking down quests into smaller tasks")
        
        if len(team.members) > 0:
            active_members = len([m for m in team.members if m.quests_completed > 0])
            participation_rate = (active_members / len(team.members)) * 100
            
            if participation_rate > 80:
                health_score += 30
            elif participation_rate > 50:
                health_score += 20
            else:
                health_score += 10
                recommendations.append("Low team participation. Engage inactive members with easier quests")
        
        if not recommendations:
            recommendations.append("Team is performing well! Keep up the great work!")
        
        return {
            'health_score': min(health_score, 100),
            'total_quests': total_quests,
            'completed': completed,
            'in_progress': in_progress,
            'abandoned': abandoned,
            'completion_rate': round(completion_rate, 1),
            'abandonment_rate': round(abandonment_rate, 1),
            'recommendations': recommendations,
        }
