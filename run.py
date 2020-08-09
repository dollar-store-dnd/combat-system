from collections import deque

from dataclasses import dataclass, field
from game import armor, weapons
from game.dice import roll_dice
from game.loader import load_game_assets
from game.dice import D20_DICE
from pprint import pprint
from game.equipment import Damage
from time import sleep
from combat import TurnManager

load_game_assets()


@dataclass
class Enemy:
    health = 20
    weapon = weapons[0]
    armor = armor[2]
    name = "Steven Seagal"


@dataclass
class PlayerCharacter:
    player_name: str = "Joe Malone"
    name: str = "Moe Jalone"
    max_health: int = 20
    current_hp: int = 20
    weapon = weapons[0]
    armor = armor[0]

    def heal(self, add_hp):
        max_add = self.max_health - self.current_hp
        self.current_hp += min(max_add, add_hp)
        if max_add == 0:
            print("You're already healthy")

        print("You healed for: ", min(max_add, add_hp))


def print_characters(character: PlayerCharacter, enemy: Enemy):
    print("#" * 64)
    print("PLAYER:\n", character.name, "HP:", character.current_hp)
    print("ENEMY:\n", enemy.name, "HP:", enemy.health)
    print("#" * 64)


def print_roll(roll: int):
    print("Rolled:", roll)


def start_combat() -> None:
    """Basic combat loop"""
    turn_manager = TurnManager()

    main_char = PlayerCharacter()
    enemy_char = Enemy()

    turn_manager.add_combatant(main_char, False)



    turn_manager.initiative()
    exit()

    sleep(1)

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
                multiplier = 1
                if hit == 20:
                    multiplier = 2

                if hit >= enemy_char.armor.ac:
                    damage = roll_dice(character.weapon.damage) * multiplier
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
                character.heal(heal)

            else:
                print("Inteligance check failed: skip your turn!")

        else:
            hit = roll_dice(damage=D20_DICE)
            print_roll(hit)

            if hit == 1:
                print(enemy_char.name, "collapses from a heart attack and dies!")
                enemy_char.health = 0
                break

            elif hit >= main_char.armor.ac:
                damage = roll_dice(character.weapon.damage)
                main_char.current_hp -= damage
                print("You took:", damage, "damage!")

                if main_char.current_hp <= 0:
                    print("YOU LOSE!!!")
                    break
            else:
                print(enemy_char.name, "MISSED!")

        sleep(1)

    # TODO(TravisZehring): Write code here


if __name__ == "__main__":
    start_combat()
