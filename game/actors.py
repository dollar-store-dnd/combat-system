from game import AbilityScore, Skill, Alignment

from dataclasses import dataclass, field
from typing import Dict, Set


class GameMaster:
    # FUTURE
    pass


@dataclass
class PlayableCharacter:
    player_name: str
    name: str
    ability_scores: Dict[AbilityScore, int]
    skills: Set[Skill]
    alignment: Alignment

    def get_modifier(self, ability_score: AbilityScore):
        return (self.ability_scores[ability_score] // 2) - 5


@dataclass
class NonPlayableCharacter:
    pass
