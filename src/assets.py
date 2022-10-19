"""
Holds text-based assets imported from the assets folder.
"""

import json

from .nature import Nature
from .terrain import Terrain

def read_terrains():
    """
    Return list of Terrains loaded from game assets.
    """
    with open("assets/terrains.json", encoding="utf8") as json_file:
        terrain_qualities = json.load(json_file)
        return {index: Terrain(**terrain)
                for index, terrain in enumerate(terrain_qualities)}

def read_natures():
    """
    Return list of Natures loaded from game assets.
    """
    with open("assets/natures.json", encoding="utf8") as json_file:
        nature_qualities = json.load(json_file)
        return {index: Nature(**nature)
                for index, nature in enumerate(nature_qualities)}

# Invoking functions multiple times would result in duplicate objects in memory.
# Wrapping this in a class would result in a singleton, which does not feel justified.
# Therefore, this stays until there is a reason to change it.

terrains = read_terrains()
natures = read_natures()
