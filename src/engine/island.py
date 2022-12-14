"""
Contains the Island class, which represents a contiguous landmass of Cells.
"""

import random

from ..assets.assets import read_natures
from .drop import Drop
from .enemy import Enemy

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

        natures = read_natures()
        if self.index < len(natures):
            self.nature = natures[self.index]
            self.spawn_artifact()
        else:
            self.nature = random.choice(natures)

        self.spawn_enemies()

    def spawn_enemies(self):
        """
        Try to add Enemy characters to Cells.
        """
        for cell in self.cells:
            if not cell.terrain.walkable:
                continue
            if cell.character:
                continue
            if random.random() < 0.03:
                cell.drop = Drop(cell,  "o") # alternate: curses.ACS_DIAMOND
            elif random.random() < 0.05:
                cell.drop = Drop(cell, "a")
            if random.random() < 0.01:
                cell.character = Enemy(self.nature, cell, self.nature.char)
                self.level.enemies.add(cell.character)


    def spawn_artifact(self):
        """
        Add Artifact to a random Cell.
        """
        artifact_cell = random.choice(self.cells)
        artifact_cell.drop = Drop(artifact_cell, "@")
