"""
Contains the Level class, which represents a 2d grid of Cells.
"""

import random

from .cell import Cell
from .island import Island
from ..level_gen.level_gen import LevelGenerator
from .player import Player

class Level:
    """
    Contains the Level class, which represents a 2d grid of Cells.
    Controls the coordinate system, including communicating between neighboring Cells.
    Keeps track of Cells modified each turn.
    """
    # pylint: disable=too-many-instance-attributes
    # This class (obviously) holds many elements of a Level,
    # so the many instances are justified.
    def __init__(self, game, seed=None):
        self.game = game
        self.board = []
        self.islands = []
        self.ticked = set()
        self.player = None
        self.enemies = set()
        self.seed = random.randint(0, 100000) if not seed else seed

        self.from_array(LevelGenerator(self.seed).generate())
        self.detect_islands()
        self.spawn_player()

    def from_array(self, array):
        """
        Build the Cells of the Level from a numpy array.
        """
        self.lines, self.cols = array.shape
        for y, line in enumerate(array):
            for x, index in enumerate(line):

                cell = Cell(self, index, y, x)
                self.board.append(cell)

    def spawn_player(self):
        """
        Add Player on the Cell.
        """
        # add a check for enemies in cell?
        # *if* they are already spawned in at this point
        # add a check for repeated use?
        cell = random.choice(random.choice(self.islands).cells)
        self.player = Player(cell, "µ")
        cell.character = self.player

    def detect_islands(self):
        """
        Segment the Level into individual Islands.
        """
        land = set(cell for cell in self.board if cell.terrain.land)
        islands = []

        while land:
            queue = []
            queue.append(land.pop())
            islands.append([])

            while queue:
                seed = queue.pop(0)
                islands[-1].append(seed)
                neighbors = {seed.neighbor("u"),
                             seed.neighbor("d"),
                             seed.neighbor("l"),
                             seed.neighbor("r")
                             }
                land_neighbors = land & neighbors
                land.difference_update(land_neighbors)
                queue.extend(land_neighbors)

        for index, island in enumerate(islands):
            self.islands.append(Island(self, island, index))

    def get_cell(self, y, x):
        """
        Return Cell corresponding to the given 2d coordinate.
        Return None if the coordinate is out of bounds.
        """
        if y < 0 or y >= self.lines:
            return None
        if x < 0 or x >= self.cols:
            return None
        return self.board[y * self.cols + x]
