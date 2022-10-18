"""
Contains the Island class, which represents a contiguous landmass of Cells.
"""

import curses
import random

from .assets import natures
from .character import Character
from .drop import Drop

class Island:
    """
    A contiguous landmass of Cells.
    Responsible for spawning enemies of a certain class.
    """

    def __init__(self, level, cells, index):
        self.level = level
        self.cells = cells
        self.index = index

        for cell in self.cells:
            cell.island = self

        if self.index < len(natures):
            self.nature = natures[self.index]
            self.spawn_artifact()
        else:
            self.nature = random.choice(natures)

        self.spawn_enemies()

    def spawn_enemies(self):
        for cell in self.cells:
            if not cell.terrain.walkable or not cell.terrain.spawnable:
                continue
            if cell.character:
                continue
            if random.random() < 0.03:
                cell.drop = Drop(cell, curses.ACS_DIAMOND)
            if random.random() < 0.01:
                self.character = Character(cell, self.nature.char)
                self.level.enemies.add(self.character)

    def spawn_artifact(self):
        artifact_cell = random.choice(self.cells)
        artifact_cell.drop = Drop(artifact_cell, "@")