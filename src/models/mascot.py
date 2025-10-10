"""
Mascot model - Represents team mascots in the QuestBoard system
"""

from datetime import datetime
from enum import Enum
from typing import Optional
from dataclasses import dataclass, field


class MascotType(Enum):
    """Types of mascots available"""
    CYBER_SLOTH = "Cyber Sloth"
    PIXEL_PHOENIX = "Pixel Phoenix"
    CODE_DRAGON = "Code Dragon"
    NINJA_TURTLE = "Ninja Turtle"
    SPACE_CAT = "Space Cat"
    RETRO_ROBOT = "Retro Robot"
    QUANTUM_QUOKKA = "Quantum Quokka"


class MascotEvolutionStage(Enum):
    """Evolution stages of mascots based on team XP"""
    EGG = "Egg"
    HATCHLING = "Hatchling"
    JUVENILE = "Juvenile"
    ADULT = "Adult"
    ELDER = "Elder"
    LEGENDARY = "Legendary"


@dataclass
class Mascot:
    """
    Represents a team mascot that evolves with team progress.
    
    Attributes:
        name: Custom name given to the mascot
        mascot_type: Type of mascot
        evolution_stage: Current evolution stage
        total_xp: Total XP accumulated
        personality_traits: List of personality traits
        skin: Current seasonal or special skin
        created_at: When the mascot was created
    """
    name: str
    mascot_type: MascotType
    evolution_stage: MascotEvolutionStage = field(default=MascotEvolutionStage.EGG)
    total_xp: int = 0
    personality_traits: list[str] = field(default_factory=list)
    skin: str = "default"
    created_at: datetime = field(default_factory=datetime.now)
    mascot_id: str = field(default_factory=lambda: f"mascot_{datetime.now().timestamp()}")
    
    def __post_init__(self):
        """Validate mascot data after initialization"""
        if not self.name or len(self.name.strip()) == 0:
            raise ValueError("Mascot name cannot be empty")
        
        if self.total_xp < 0:
            raise ValueError("Total XP must be non-negative")
        
        # Convert string enums to proper enum types if needed
        if isinstance(self.mascot_type, str):
            # Handle spaces in enum names
            enum_name = self.mascot_type.upper().replace(" ", "_")
            self.mascot_type = MascotType[enum_name]
        
        if isinstance(self.evolution_stage, str):
            self.evolution_stage = MascotEvolutionStage[self.evolution_stage.upper()]
        
        # Update evolution stage based on XP if needed
        self._update_evolution_stage()
    
    def add_xp(self, xp: int) -> bool:
        """
        Add XP to the mascot and check for evolution.
        
        Args:
            xp: Amount of XP to add
            
        Returns:
            True if mascot evolved, False otherwise
        """
        if xp < 0:
            raise ValueError("Cannot add negative XP")
        
        old_stage = self.evolution_stage
        self.total_xp += xp
        self._update_evolution_stage()
        
        return old_stage != self.evolution_stage
    
    def _update_evolution_stage(self) -> None:
        """Update evolution stage based on total XP"""
        if self.total_xp >= 5000:
            self.evolution_stage = MascotEvolutionStage.LEGENDARY
        elif self.total_xp >= 2000:
            self.evolution_stage = MascotEvolutionStage.ELDER
        elif self.total_xp >= 1000:
            self.evolution_stage = MascotEvolutionStage.ADULT
        elif self.total_xp >= 500:
            self.evolution_stage = MascotEvolutionStage.JUVENILE
        elif self.total_xp >= 100:
            self.evolution_stage = MascotEvolutionStage.HATCHLING
        else:
            self.evolution_stage = MascotEvolutionStage.EGG
    
    def change_skin(self, skin: str) -> None:
        """
        Change the mascot's appearance skin.
        
        Args:
            skin: Name of the skin to apply
        """
        if not skin or len(skin.strip()) == 0:
            raise ValueError("Skin name cannot be empty")
        
        self.skin = skin
    
    def add_personality_trait(self, trait: str) -> None:
        """
        Add a personality trait to the mascot.
        
        Args:
            trait: Personality trait to add
        """
        if trait and trait not in self.personality_traits:
            self.personality_traits.append(trait)
    
    def get_emoji(self) -> str:
        """Get the emoji representation of the mascot"""
        emojis = {
            MascotType.CYBER_SLOTH: "🦥",
            MascotType.PIXEL_PHOENIX: "🐦",
            MascotType.CODE_DRAGON: "🐉",
            MascotType.NINJA_TURTLE: "🐢",
            MascotType.SPACE_CAT: "🐱",
            MascotType.RETRO_ROBOT: "🤖",
            MascotType.QUANTUM_QUOKKA: "🦘",
        }
        return emojis.get(self.mascot_type, "🎭")
    
    def get_xp_to_next_stage(self) -> Optional[int]:
        """
        Calculate XP needed to reach the next evolution stage.
        
        Returns:
            XP needed for next stage, or None if at max stage
        """
        stage_requirements = {
            MascotEvolutionStage.EGG: 100,
            MascotEvolutionStage.HATCHLING: 500,
            MascotEvolutionStage.JUVENILE: 1000,
            MascotEvolutionStage.ADULT: 2000,
            MascotEvolutionStage.ELDER: 5000,
            MascotEvolutionStage.LEGENDARY: None,
        }
        
        next_requirement = stage_requirements.get(self.evolution_stage)
        if next_requirement is None:
            return None
        
        return max(0, next_requirement - self.total_xp)
    
    def to_dict(self) -> dict:
        """Convert mascot to dictionary representation"""
        return {
            'mascot_id': self.mascot_id,
            'name': self.name,
            'mascot_type': self.mascot_type.value,
            'evolution_stage': self.evolution_stage.value,
            'total_xp': self.total_xp,
            'xp_to_next_stage': self.get_xp_to_next_stage(),
            'personality_traits': self.personality_traits,
            'skin': self.skin,
            'created_at': self.created_at.isoformat(),
            'emoji': self.get_emoji(),
        }
    
    def __str__(self) -> str:
        """String representation of the mascot"""
        return f"{self.get_emoji()} {self.name} ({self.evolution_stage.value}) - {self.total_xp} XP"


def get_seasonal_skins() -> dict[str, list[str]]:
    """
    Get available seasonal skins for mascots.
    
    Returns:
        Dictionary mapping seasons to available skins
    """
    return {
        "spring": ["Blooming Garden", "Cherry Blossom", "Rainbow"],
        "summer": ["Beach Party", "Tropical", "Sunset"],
        "fall": ["Harvest", "Autumn Leaves", "Pumpkin Spice"],
        "winter": ["Ice Kingdom", "Snowflake", "Northern Lights"],
        "special": ["Cyber Neon", "Retro 8-bit", "Holographic", "Galaxy"],
    }
