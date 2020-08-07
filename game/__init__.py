"""
Game Services Module
- Registers objects into the world
- Brings in classes, background, and races
- Brings in spellcasting (or equivalent)
"""

from enum import Enum, auto
from typing import NamedTuple, Optional, List


class AbilityScore(Enum):
    Strength = auto()
    Dexterity = auto()
    Constitution = auto()
    Intelligence = auto()
    Wisdom = auto()
    Charisma = auto()


class PackageMetadata(NamedTuple):
    name: str
    shortname: str
    version: str


armor: List = []
spells: List = []
weapons: List = []

package: Optional[PackageMetadata] = None


def register_package_metadata(**kwargs):
    global package
    package = PackageMetadata(**kwargs)
