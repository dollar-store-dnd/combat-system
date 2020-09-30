from dataclasses import dataclass
from pprint import pprint
from typing import List
from time import sleep

from combat import TurnManager
from game import armor, weapons
from game.actors import Combatable
from game.dice import roll_dice, D20_DICE
from game.loader import load_game_assets
from game.equipment import Damage, Weapon, Armor

load_game_assets()


@dataclass
class Enemy(Combatable):
    name: str = "Steven Seagull"
    current_hp: int = 20
    weapon: Weapon = weapons[0]
    armor: Armor = armor[2]

    # TODO: Make a sort of enemy stat display method
    # TODO: What if combatable makes it so that we have to create methods for fighting
    # Such as in essences performing a new action
    def perform_action(allies: List[Combatable], enemies: List[Combatable]):
        raise NotImplementedError

@dataclass
class PlayerCharacter(Combatable):
    player_name: str = "Joe Malone"
    name: str = "Moe Jalone"
    max_health: int = 20
    current_hp: int = 20
    weapon: Weapon = weapons[0]
    armor: Armor = armor[0]

    def heal(self, add_hp):
        max_add = self.max_health - self.current_hp
        self.current_hp += min(max_add, add_hp)
        if max_add == 0:
            print("You're already healthy")

        print("You healed for: ", min(max_add, add_hp))

    # TODO: Make a sort of player stat display method
    def perform_action(allies: List[Combatable], enemies: List[Combatable]):
        raise NotImplementedError


def print_characters(character: PlayerCharacter, enemy: Enemy):
    # TODO: How could we extend this to multiple enemies
    print("#" * 64)
    print("PLAYER:\n", character.name, "HP:", character.current_hp)
    print("ENEMY:\n", enemy.name, "HP:", enemy.current_hp)
    print("#" * 64)


def print_roll(roll: int):
    print("Rolled:", roll)


def start_combat() -> None:
    """Basic combat loop"""
    turn_manager = TurnManager()

    main_char = PlayerCharacter()
    enemy_char = Enemy()

    turn_manager.add_combatant(main_char, is_enemy=False)
    turn_manager.add_combatant(enemy_char)

    # TODO: How to prevent adding the same combatant twice such as
    # turn_manager.add_combatant(enemy_char, True)
    # turn_manager.add_combatant(enemy_char, True)

    turn_manager.initiative()
    exit()  # TODO: Remove this

    sleep(1)

    while True:
        # TODO: How can we use our new turn manager to manage this?
        character = turn_queue[-1]
        turn_queue.rotate()

        # TODO: This is a future thought, but how could be move this into a combat session object?
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
                    enemy_char.current_hp -= damage
                    print("Enemy took:", damage, "damage!")
                    print("End turn!")

                    if enemy_char.current_hp <= 0:
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
                enemy_char.current_hp = 0
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


if __name__ == "__main__":
    start_combat()
