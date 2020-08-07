from collections import deque

from game import armor, weapons
from game.dice import roll_dice
from game.loader import load_game_assets


def start_combat() -> None:
    """Basic combat loop"""
    turn_queue = deque()

    # TODO(TravisZehring): Write code here
    pass


if __name__ == "__main__":
    load_game_assets()
    from pprint import pprint

    pprint(armor)
    pprint(weapons)
    print(roll_dice(weapons[0].damage))

    start_combat()
