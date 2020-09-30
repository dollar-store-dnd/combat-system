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
    def perform_action(self, allies: List[Combatable], enemies: List[Combatable]):
        hit = roll_dice(damage=D20_DICE)
        print_roll(hit)

        if hit == 1:
            print(self.name, "collapses from a heart attack and dies!")
            self.current_hp = 0

        elif hit >= allies[0].armor.ac:
            damage = roll_dice(self.weapon.damage)
            allies[0].current_hp -= damage
            print("You took:", damage, "damage!")

            if allies[0].current_hp <= 0:
                print(allies[0].name, " DIED!!")

        else:
            print(self.name, "MISSED!")


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

    # TODO: Make a player stat display method
    def perform_action(self, allies: List[Combatable], enemies: List[Combatable]):
        print("Your turn:")
        action = input("- Attack   - Heal \n")

        if action == "Attack":
            print("Who do you want to attack?\n")
            print("Enemies:  ")
            for x in enemies:
                print(x.name, "  ")

            print("\nAllies:  ")
            found = False
            for x in allies:
                print(x.name, "  ")
            victim = input()

            for x in enemies:
                if victim == x.name:
                    victim = x
                    found = True
                    break
            for x in allies:
                if victim == x.name:
                    victim = x
                    found = True
                    break
            if not found:
                return print(self.name, " stumbled in confusion")

            hit = roll_dice(damage=D20_DICE)
            print_roll(hit)
            multiplier = 1
            if hit == 20:
                multiplier = 2

            if hit >= victim.armor.ac:
                damage = roll_dice(self.weapon.damage) * multiplier
                victim.current_hp -= damage
                print(victim.name, " took:", damage, "damage!")
                print("End turn!")

                if victim.current_hp <= 0:
                    print(victim.name, "DIED!")
                    enemies.remove(victim)

            else:
                print(self.name, "MISSED!")

        elif action == "Heal":
            found = False
            print("Who do you want to heal?\n")
            print("Allies:")
            for x in allies:
                print(x.name, "  ")
            healed = input()
            for x in allies:
                if healed == x.name:
                    healed = x
                    found = True
                    break

            if not found:
                return print(self.name, " stumbled in confusion")
            heal = roll_dice(damage=Damage(die_type=10, dice=1, type=""))
            x.heal(heal)

        else:
            print("Inteligance check failed: skip your turn!")


def print_roll(roll: int):
    print("Rolled:", roll)


def start_combat() -> None:
    """Basic combat loop"""
    turn_manager = TurnManager()

    friends = int(input("How many Joe's will fight? \n"))
    allies = []
    for x in range(0, friends):
        allies.append(PlayerCharacter())
        turn_manager.add_combatant(allies[x], is_enemy=False)

    bad_guys = int(input("How many enemies will be fought? \n"))
    enemies = []
    for x in range(0, bad_guys):
        enemies.append(Enemy())
        turn_manager.add_combatant(enemies[x])



    # TODO: How to prevent adding the same combatant twice such as
    # turn_manager.add_combatant(enemy_char, True)
    # turn_manager.add_combatant(enemy_char, True)

    turn_manager.initiative()

    # sleep(1)

    while True:
        # TODO: How can we use our new turn manager to manage this?
        combatant, is_enemy = turn_manager.next_turn()

        if is_enemy:
            print("Enemy Turn:  ", combatant.name)
            combatant.perform_action(enemies, allies)
            if len(allies) == 0:
                print("YOU LOST!!!")
                break

        else:
            print("Your Turn:  ", combatant.name)
            combatant.perform_action(allies, enemies)
            if len(enemies) == 0:
                print("YOU WON!!!")
                break
        # TODO: This is a future thought, but how could be move this into a combat session object?
        # if not is_enemy:
        # print_characters(main_char, enemy_char)

        sleep(1)


if __name__ == "__main__":
    start_combat()
