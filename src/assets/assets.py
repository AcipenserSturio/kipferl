"""
Holds text-based assets imported from the assets folder.
"""

import json
from functools import cache

from .nature import Nature
from .terrain import Terrain


@cache
def read_terrains():
    """
    Return list of Terrains loaded from game assets.
    """
    with open("assets/terrains.json", encoding="utf8") as json_file:
        terrain_qualities = json.load(json_file)
        return {index: Terrain(**terrain)
                for index, terrain in enumerate(terrain_qualities)}


@cache
def read_natures():
    """
    Return list of Natures loaded from game assets.
    """
    with open("assets/natures.json", encoding="utf8") as json_file:
        nature_qualities = json.load(json_file)
        return {index: Nature(**nature)
                for index, nature in enumerate(nature_qualities)}

@cache
def read_defines():
    """
    Return list of defines loaded from game assets.
    """
    with open("assets/defines.json", encoding="utf8") as json_file:
        defines = json.load(json_file)
        return defines
