from game.equipment import register_object

from typing import Dict
from pathlib import Path
from zipfile import ZipFile, Path as ZipPath

import toml


def _locate_available_datastore():
    """"""
    cwd = Path.cwd()
    potential_files = cwd.glob("*.zip")

    # TODO: Add simple zipfile config.toml detection algo

    return list(potential_files)[0]


def _load_package_config(zip: ZipFile):
    """"""
    config_information: Dict
    with zip.open("config.toml", "r") as f:
        data = f.read().decode("utf-8")
        config_information = toml.loads(s=data)

    return config_information


def load_game_assets():
    """"""
    zip = ZipFile(_locate_available_datastore())
    config = _load_package_config(zip=zip)

    print("#" * 64)
    print("Assets loading...")
    print("Package:", config["package"]["name"], "| V", config["package"]["version"])

    def recursive_object_registration(base_path: ZipPath):
        for path in base_path.iterdir():
            if path.is_file():
                register_object(path)
            else:
                recursive_object_registration(path)

    simple_melee_weapons = ZipPath(zip) / "weapons" / "simple" / "melee"
    armor = ZipPath(zip) / "armor"

    recursive_object_registration(simple_melee_weapons)
    recursive_object_registration(armor)

    print("Assets Loaded.")
    print("#" * 64)
