from abc import ABC
from dataclasses import dataclass
from typing import Dict, Set, List

from game import AbilityScore, Skill, Alignment
from game.equipment import Armor, Weapon


class GameMaster:
    # FUTURE
    pass


class Combatable(ABC):
    pass


@dataclass
class PlayableCharacter(Combatable):
    player_name: str
    name: str
    ability_scores: Dict[AbilityScore, int]
    skills: Set[Skill]
    alignment: Alignment
    weapons: List[Weapon]
    armor: Armor

    def get_modifier(self, ability_score: AbilityScore):
        return (self.ability_scores[ability_score] // 2) - 5


@dataclass
class NonPlayableCharacter:
    pass


@dataclass
class EnemyCharacter(Combatable):
    pass
