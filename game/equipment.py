from game import armor, weapons, AbilityScore

from json import loads
from typing import NamedTuple, Dict, List
from zipfile import Path as ZipPath


class Damage(NamedTuple):
    die_type: int
    dice: int
    type: str


class ArmorClass(NamedTuple):
    base: int
    modifier: AbilityScore


class Armor(NamedTuple):
    name: str
    ac: int
    class_: str


class Weapon(NamedTuple):
    name: str
    damage: Damage
    class_: List[str]
    properties: List[str]


def _register_weapon(data: Dict) -> None:
    new_weapon = Weapon(
        name=data["name"],
        damage=Damage(**data["damage"]),
        class_=data["class"],
        properties=data["properties"],
    )
    weapons.append(new_weapon)


def _register_armor(data: Dict):
    new_armor = Armor(name=data["name"], ac=data["ac"]["base"], class_=data["class"])
    armor.append(new_armor)


register_map = {"armor": _register_armor, "weapon": _register_weapon}


def register_object(zip_path: ZipPath):
    data = loads(zip_path.read_text())
    register_map[data["type"]](data)
