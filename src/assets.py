"""
Holds text-based assets imported from the assets folder.
"""

import json

from .nature import Nature
from .terrain import Terrain

with open("assets/terrains.json", encoding="utf8") as f:
    terrain_qualities = json.load(f)
    terrains = {index: Terrain(
            name=terrain.get("name", None),
            char=terrain.get("char", None),
            color=terrain.get("color", None),
            land=terrain.get("land", None),
            elevation=terrain.get("elevation", None),
            walkable=terrain.get("walkable", None),
            spawnable=terrain.get("spawnable", None),
            sound=terrain.get("sound", None),
        ) for index, terrain in enumerate(terrain_qualities)}


with open("assets/natures.json", encoding="utf8") as f:
    nature_qualities = json.load(f)
    natures = {index: Nature(
            name=nature.get("name", None),
            char=nature.get("char", None),
            color=nature.get("color", None),
            active=nature.get("active", None),
            passive=nature.get("passive", None),
        ) for index, nature in enumerate(nature_qualities)}
