from collections import deque, defaultdict
from random import shuffle

from game.actors import Combatable
from game.dice import roll_dice, D20_DICE


class CombatSession:
    def __init__(self):
        raise NotImplementedError


class TurnManager:
    def __init__(self):
        self.queue = deque()
        self.combatants = []

    def add_combatant(self, combatant: Combatable, is_enemy: bool = True) -> None:
        self.combatants.append((combatant, is_enemy))

    def remove_combatant(self, combatant: Combatable) -> None:
        raise NotImplementedError

    def initiative(self) -> None:
        order = defaultdict(list)

        for combatant in self.combatants:
            init_roll = roll_dice(damage=D20_DICE)
            order[init_roll].append(combatant)

        for roll in sorted(order.keys(), reverse=True):
            shuffle(order[roll])
            for combatant in order[roll]:
                self.queue.appendleft(combatant)

    def next_turn(self):
        character = self.queue[-1]
        self.queue.rotate()
        return character
