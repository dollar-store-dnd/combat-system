from game import weapons

from json import loads
from typing import NamedTuple, Dict
from zipfile import Path as ZipPath


class Armor(NamedTuple):
    pass


class Weapon(NamedTuple):
    name: str
    damage: Dict


def register_weapon(zip_path: ZipPath) -> None:
    weapon_data = loads(zip_path.read_text())
    weapon = Weapon(name=weapon_data["name"], damage=weapon_data["damage"])
    weapons.append(weapon)


def register_object():
    pass
