from collections import deque, defaultdict
from game.dice import D20_DICE, roll_dice
from random import shuffle


class CombatSession:
    pass


class TurnManager:
    def __init__(self):
        self.queue = deque()

        self.combatants = []

    def add_combatant(self, combatant, is_enemy):
        self.combatants.append((combatant, is_enemy))

    def initiative(self):
        order = defaultdict(list)

        for c in self.combatants:
            init_roll = roll_dice(damage=D20_DICE)
            order[init_roll].append(c)

        for roll in sorted(order.keys(), reverse=True):
            shuffle(order[roll])
            for c in order[roll]:
                self.queue.appendleft(c)
        print(self.queue)
        print(order)