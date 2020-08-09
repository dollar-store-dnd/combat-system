from collections import deque

from dataclasses import dataclass, field
from game import armor, weapons
from game.dice import roll_dice
from game.loader import load_game_assets
from game.dice import D20_DICE
from pprint import pprint
from game.equipment import Damage
from time import sleep

load_game_assets()


@dataclass
class Enemy:
    health = 20
    weapon = weapons[0]
    name = "Steven Seagal"


@dataclass
class PlayerCharacter:
    player_name: str = "Joe Malone"
    name: str = "Moe Jalone"
    health: int = 20
    weapon = weapons[0]


def print_characters(character: PlayerCharacter, enemy: Enemy):
    print("#" * 64)
    print("PLAYER:\n", character.name, "HP:", character.health)
    print("ENEMY:\n", enemy.name, "HP:", enemy.health)
    print("#" * 64)


def print_roll(roll: int):
    print("Rolled:", roll)


def start_combat() -> None:
    """Basic combat loop"""
    turn_queue = deque()

    main_char = PlayerCharacter()
    enemy_char = Enemy()

    player_roll = roll_dice(damage=D20_DICE)
    enemy_roll = roll_dice(damage=D20_DICE)

    while player_roll == enemy_roll:
        player_roll = roll_dice(damage=D20_DICE)
        enemy_roll = roll_dice(damage=D20_DICE)

    if player_roll > enemy_roll:
        turn_queue.appendleft(main_char)
        turn_queue.appendleft(enemy_char)
    else:
        turn_queue.appendleft(enemy_char)
        turn_queue.appendleft(main_char)

    while True:
        character = turn_queue[-1]
        turn_queue.rotate()

        if isinstance(character, PlayerCharacter):
            print_characters(main_char, enemy_char)
            print("Your turn:")
            action = input("- Attack   - Heal \n")

            if action == "Attack":
                hit = roll_dice(damage=D20_DICE)
                print_roll(hit)

                if hit >= 15:
                    damage = roll_dice(character.weapon.damage)
                    enemy_char.health -= damage
                    print("Enemy took:", damage, "damage!")
                    print("End turn!")
                    if enemy_char.health <= 0:
                        print(main_char.name, "WINS!!!")
                        break

                else:
                    print(main_char.name, "MISSED!")

            elif action == "Heal":
                heal = roll_dice(damage=Damage(die_type=10, dice=1, type=""))
                main_char.health += heal
                print("Healed for:", heal)

        else:
            hit = roll_dice(damage=D20_DICE)

            if hit >= 15:
                damage = roll_dice(character.weapon.damage)
                main_char.health -= damage
                print("You took:", damage, "damage!")

                if main_char.health <= 0:
                    print("YOU LOSE!!!")
                    break
            else:
                print(enemy_char.name, "MISSED!")

        sleep(1)

    # TODO(TravisZehring): Write code here


if __name__ == "__main__":
    start_combat()
