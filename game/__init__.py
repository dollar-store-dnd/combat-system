"""
Game Services Module
- Registers objects into the world
- Brings in classes, background, and races
- Brings in spellcasting (or equivalent)
"""

from enum import Enum, auto
from typing import NamedTuple, Optional, List


class Alignment(str, Enum):
    LawfulGood = "LG"
    LawfulNeutral = "LN"
    LawfulEvil = "LE"
    NeutralGood = "NG"
    Neutral = "NN"
    NeutralEvil = "NE"
    ChaoticGood = "CG"
    ChaoticNeutral = "CN"
    ChaoticEvil = "CE"


class AbilityScore(Enum):
    Strength = 0
    Dexterity = 1
    Constitution = 2
    Intelligence = 3
    Wisdom = 4
    Charisma = 5


class Skill(Enum):
    Acrobatics = auto()
    AnimalHandling = auto()
    Arcana = auto()
    Athletics = auto()
    Deception = auto()
    History = auto()
    Insight = auto()
    Intimidation = auto()
    Investigation = auto()
    Medicine = auto()
    Nature = auto()
    Perception = auto()
    Performance = auto()
    Persuasion = auto()
    Religion = auto()
    SleightOfHand = auto()
    Stealth = auto()
    Survival = auto()


ABILITY_SHORTNAME_ENUM_MAP = {
    "STR": AbilityScore.Strength,
    "DEX": AbilityScore.Dexterity,
    "CON": AbilityScore.Constitution,
    "INT": AbilityScore.Intelligence,
    "WIS": AbilityScore.Wisdom,
    "CHA": AbilityScore.Charisma,
}

SKILLS_ABILITY_MAP = {
    Skill.Acrobatics: AbilityScore.Dexterity,
    Skill.AnimalHandling: AbilityScore.Wisdom,
    Skill.Arcana: AbilityScore.Intelligence,
    Skill.Athletics: AbilityScore.Strength,
    Skill.Deception: AbilityScore.Charisma,
    Skill.History: AbilityScore.Intelligence,
    Skill.Insight: AbilityScore.Wisdom,
    Skill.Intimidation: AbilityScore.Charisma,
    Skill.Investigation: AbilityScore.Intelligence,
    Skill.Medicine: AbilityScore.Wisdom,
    Skill.Nature: AbilityScore.Intelligence,
    Skill.Perception: AbilityScore.Wisdom,
    Skill.Performance: AbilityScore.Charisma,
    Skill.Persuasion: AbilityScore.Charisma,
    Skill.Religion: AbilityScore.Intelligence,
    Skill.SleightOfHand: AbilityScore.Dexterity,
    Skill.Stealth: AbilityScore.Dexterity,
    Skill.Survival: AbilityScore.Wisdom,
}


class PackageMetadata(NamedTuple):
    name: str
    shortname: str
    version: str


armor: List = []
spells: List = []
weapons: List = []

_package: Optional[PackageMetadata] = None


def get_package_meta_data() -> PackageMetadata:
    global _package
    return _package


def register_package_metadata(**kwargs) -> None:
    global _package
    package = PackageMetadata(**kwargs)
