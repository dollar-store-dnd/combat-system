from game import armor, weapons

from json import loads
from typing import NamedTuple, Dict
from zipfile import Path as ZipPath


class Armor(NamedTuple):
    name: str
    ac: int


class Damage(NamedTuple):
    die_type: int
    dice: int
    type: str


class Weapon(NamedTuple):
    name: str
    damage: Damage


def _register_weapon(data: Dict) -> None:
    new_weapon = Weapon(name=data["name"], damage=Damage(**data["damage"]))
    weapons.append(new_weapon)


def _register_armor(data: Dict):
    new_armor = Armor(name=data["name"], ac=data["ac"]["base"])
    armor.append(new_armor)


register_map = {"armor": _register_armor, "weapon": _register_weapon}


def register_object(zip_path: ZipPath):
    data = loads(zip_path.read_text())
    register_map[data["type"]](data)
