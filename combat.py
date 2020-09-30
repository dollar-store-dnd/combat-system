from collections import deque, defaultdict
from random import shuffle

from game.actors import Combatable
from game.dice import roll_dice, D20_DICE


class CombatSession:
    def __init__(self):
        raise NotImplementedError

    def print_characters(self, character: 'PlayerCharacter', enemy: 'Enemy'):
        # TODO: How could we extend this to multiple enemies
        print("#" * 64)
        print("PLAYER:\n", character.name, "HP:", character.current_hp)
        print("ENEMY:\n", enemy.name, "HP:", enemy.current_hp)
        print("#" * 64)


class TurnManager:
    def __init__(self):
        self.queue = deque()
        self.combatants = []

    def add_combatant(self, combatant: Combatable, is_enemy: bool = True) -> None:
        self.combatants.append((combatant, is_enemy))
        # print(".")

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
