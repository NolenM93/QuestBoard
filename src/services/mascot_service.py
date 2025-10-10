"""
Mascot service - Business logic for mascot management
"""

from typing import List
from datetime import datetime

from ..models.mascot import Mascot, MascotType, MascotEvolutionStage, get_seasonal_skins
from ..models.team import Team


class MascotService:
    """Service for managing mascots and evolution"""
    
    @staticmethod
    def create_mascot(name: str, mascot_type: MascotType) -> Mascot:
        """
        Create a new mascot.
        
        Args:
            name: Mascot name
            mascot_type: Type of mascot
            
        Returns:
            New Mascot instance
        """
        return Mascot(name=name, mascot_type=mascot_type)
    
    @staticmethod
    def evolve_mascot(mascot: Mascot, xp: int) -> bool:
        """
        Add XP to mascot and check for evolution.
        
        Args:
            mascot: Mascot to evolve
            xp: Amount of XP to add
            
        Returns:
            True if mascot evolved, False otherwise
        """
        return mascot.add_xp(xp)
    
    @staticmethod
    def get_evolution_message(mascot: Mascot) -> str:
        """
        Get a celebratory message for mascot evolution.
        
        Args:
            mascot: Mascot that evolved
            
        Returns:
            Evolution message
        """
        messages = {
            MascotEvolutionStage.HATCHLING: f"🥚 {mascot.name} has hatched! Welcome to the team!",
            MascotEvolutionStage.JUVENILE: f"🌱 {mascot.name} is growing strong! Keep up the good work!",
            MascotEvolutionStage.ADULT: f"💪 {mascot.name} has reached maturity! Your team is thriving!",
            MascotEvolutionStage.ELDER: f"🧙 {mascot.name} is now a wise elder! Legendary status awaits!",
            MascotEvolutionStage.LEGENDARY: f"⭐ {mascot.name} has become LEGENDARY! Your team is unstoppable!",
        }
        
        return messages.get(mascot.evolution_stage, f"{mascot.name} has evolved!")
    
    @staticmethod
    def apply_seasonal_skin(mascot: Mascot, season: str) -> None:
        """
        Apply a seasonal skin to the mascot.
        
        Args:
            mascot: Mascot to apply skin to
            season: Season name (spring, summer, fall, winter, special)
        """
        available_skins = get_seasonal_skins()
        
        if season not in available_skins:
            raise ValueError(f"Invalid season: {season}")
        
        # Apply the first skin from the season
        skins = available_skins[season]
        if skins:
            mascot.change_skin(skins[0])
    
    @staticmethod
    def get_available_skins(season: str = None) -> dict:
        """
        Get available skins, optionally filtered by season.
        
        Args:
            season: Optional season to filter by
            
        Returns:
            Dictionary of available skins
        """
        all_skins = get_seasonal_skins()
        
        if season:
            return {season: all_skins.get(season, [])}
        
        return all_skins
    
    @staticmethod
    def add_personality_trait(mascot: Mascot, trait: str) -> None:
        """
        Add a personality trait to the mascot based on team behavior.
        
        Args:
            mascot: Mascot to add trait to
            trait: Personality trait to add
        """
        valid_traits = [
            "Curious", "Brave", "Wise", "Playful", "Determined",
            "Creative", "Strategic", "Supportive", "Energetic", "Patient"
        ]
        
        if trait in valid_traits:
            mascot.add_personality_trait(trait)
    
    @staticmethod
    def suggest_personality_traits(team: Team) -> List[str]:
        """
        Suggest personality traits based on team behavior.
        
        Args:
            team: Team to analyze
            
        Returns:
            List of suggested traits
        """
        suggestions = []
        
        # High XP teams are determined
        if team.get_total_xp() > 1000:
            suggestions.append("Determined")
        
        # Teams with many members are supportive
        if len(team.members) > 5:
            suggestions.append("Supportive")
        
        # Teams with diverse quest types are creative
        from ..models.quest import QuestType
        quest_types = set(q.quest_type for q in team.quests)
        if len(quest_types) >= 4:
            suggestions.append("Creative")
        
        # Teams with consistent activity are patient
        if len(team.quests) > 20:
            suggestions.append("Patient")
        
        return suggestions
    
    @staticmethod
    def get_mascot_stats(mascot: Mascot) -> dict:
        """
        Get comprehensive stats for a mascot.
        
        Args:
            mascot: Mascot to get stats for
            
        Returns:
            Dictionary of mascot statistics
        """
        xp_to_next = mascot.get_xp_to_next_stage()
        
        return {
            'name': mascot.name,
            'type': mascot.mascot_type.value,
            'emoji': mascot.get_emoji(),
            'evolution_stage': mascot.evolution_stage.value,
            'total_xp': mascot.total_xp,
            'xp_to_next_stage': xp_to_next if xp_to_next is not None else "MAX LEVEL",
            'skin': mascot.skin,
            'personality_traits': mascot.personality_traits,
            'age_days': (datetime.now() - mascot.created_at).days,
        }
    
    @staticmethod
    def get_evolution_timeline(mascot: Mascot) -> List[dict]:
        """
        Get the evolution timeline for a mascot.
        
        Args:
            mascot: Mascot to get timeline for
            
        Returns:
            List of evolution milestones
        """
        timeline = []
        
        stages = [
            (MascotEvolutionStage.EGG, 0),
            (MascotEvolutionStage.HATCHLING, 100),
            (MascotEvolutionStage.JUVENILE, 500),
            (MascotEvolutionStage.ADULT, 1000),
            (MascotEvolutionStage.ELDER, 2000),
            (MascotEvolutionStage.LEGENDARY, 5000),
        ]
        
        for stage, xp_required in stages:
            is_reached = mascot.total_xp >= xp_required
            is_current = mascot.evolution_stage == stage
            
            timeline.append({
                'stage': stage.value,
                'xp_required': xp_required,
                'is_reached': is_reached,
                'is_current': is_current,
            })
        
        return timeline
