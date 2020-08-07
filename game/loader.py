from game import register_package_metadata
from game.equipment import register_object

from typing import Dict
from pathlib import Path
from zipfile import ZipFile, Path as ZipPath

import toml


def _locate_available_datastore() -> ZipFile:
    """Searches through the current working directory
    for zip files that contain config.toml
    """
    cwd = Path.cwd()
    potential_files = cwd.glob("*.zip")

    for file in potential_files:
        zip_file = ZipFile(file)
        if "config.toml" in zip_file.namelist():
            return zip_file
        zip_file.close()

    raise RuntimeError("Unable to find available game datastore.")


def _load_package_config(zip_file: ZipFile):
    """Extracts the configuration information from datastore"""
    config_information: Dict
    with zip_file.open("config.toml", "r") as f:
        data = f.read().decode("utf-8")
        config_information = toml.loads(s=data)
    return config_information


def _recursive_object_registration(base_path: ZipPath):
    for path in base_path.iterdir():
        if path.is_file() and path.name != "meta.json":
            register_object(path)
        elif path.is_dir():
            _recursive_object_registration(path)


def load_game_assets():
    """Loads game assets globally"""
    zip_file = _locate_available_datastore()
    config = _load_package_config(zip_file=zip_file)

    register_package_metadata(**config["package"])

    print("#" * 64)
    print("Assets loading...")
    print("Package:", config["package"]["name"], "| V", config["package"]["version"])

    armor = ZipPath(zip_file) / "armor"
    weapons = ZipPath(zip_file) / "weapons"

    _recursive_object_registration(armor)
    _recursive_object_registration(weapons)

    print("Assets Loaded.")
    print("#" * 64)
