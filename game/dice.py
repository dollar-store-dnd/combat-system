from game.equipment import Damage

from random import randint


def roll_dice(damage: Damage) -> int:
    return sum(map(lambda x: randint(1, damage.die_type), range(damage.dice)))
