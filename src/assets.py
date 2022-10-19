"""
Holds text-based assets imported from the assets folder.
"""

import json

from .nature import Nature
from .terrain import Terrain

with open("assets/terrains.json", encoding="utf8") as f:
    terrain_qualities = json.load(f)
    terrains = {index: Terrain(**terrain)
                for index, terrain in enumerate(terrain_qualities)}


with open("assets/natures.json", encoding="utf8") as f:
    nature_qualities = json.load(f)
    natures = {index: Nature(**nature)
               for index, nature in enumerate(nature_qualities)}
