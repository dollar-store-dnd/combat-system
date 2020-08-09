from game.equipment import Damage

from random import randint
D20_DICE = Damage(die_type=20, dice=1, type="")


def roll_dice(damage: Damage) -> int:
    return sum(map(lambda x: randint(1, damage.die_type), range(damage.dice)))
