"""
Contains the Level class, which represents a 2d grid of Cells.
"""

import random

from .cell import Cell
from .character import Character
from .level_gen import generate_level

class Level:
    """
    Contains the Level class, which represents a 2d grid of Cells.
    Controls the coordinate system, including communicating between neighboring Cells.
    Processes turns.
    Keeps track of Cells modified each turn.
    """
    def __init__(self):
        self.board = []
        self.ticked = set()
        self.player = None
        self.enemies = set()

        # self.load("assets/levels/huge")
        # self.build()
        self.seed = random.randint(0, 100000)
        self.from_array(generate_level(seed=self.seed))
        self.detect_islands()

    def enemy_turn(self):
        """
        Process the turn for each non-player Character.
        """
        for enemy in self.enemies:
            enemy.wander()

    def from_array(self, array):
        """
        Build the Cells of the Level from a numpy array.
        """
        self.lines, self.cols = array.shape
        for y, line in enumerate(array):
            for x, index in enumerate(line):

                cell = Cell(self, index, y, x)
                # temporary
                if x == self.cols // 2 and y == self.lines // 2:
                    self.spawn_player(cell)
                self.board.append(cell)

    def spawn_player(self, cell):
        """
        Add a player-controlled Character on the Cell.
        """
        # add a check for enemies in cell?
        # *if* they are already spawned in at this point
        # add a check for repeated use?
        self.player = Character(cell, "µ", player=True)
        cell.character = self.player

    def detect_islands(self):
        """
        Segment the Level into individual Islands.
        """
        land = set(cell for cell in self.board if cell.land)
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
            for cell in island:
                cell.island = index

    def flat(self, y, x):
        """
        Converts a 2d coordinate into a 1d coordinate.
        """
        return y * self.cols + x

    def coord(self, coord):
        """
        Converts a 1d coordinate into a 2d coordinate.
        """
        return (coord // self.cols, coord % self.cols)

    def get_cell(self, y, x):
        """
        Return Cell corresponding to the given 2d coordinate.
        Return None if the coordinate is out of bounds.
        """
        if y < 0 or y >= self.lines:
            return None
        if x < 0 or x >= self.cols:
            return None
        return self.board[self.flat(y, x)]
