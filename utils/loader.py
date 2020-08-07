from pathlib import Path
from zipfile import ZipFile

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
    