import random

from .cell import Cell
from .character import Character
from .level_gen import generate_level

class Level:
    def __init__(self):
        self.board = []
        self.ticked = set()
        self.player = None
        self.enemies = set()

        # self.load("assets/levels/huge")
        # self.build()
        self.seed = random.randint(0, 100000)
        self.from_array(generate_level(seed=self.seed))

    def enemy_turn(self):
        for enemy in self.enemies:
            enemy.wander()

    def load(self, filepath):
        with open(filepath) as f:
            self.raw_level = [line[:-1] for line in f.readlines()]
            self.lines = len(self.raw_level)
            self.cols = len(self.raw_level[0])

    def from_array(self, array):
        self.lines, self.cols = array.shape
        for y, line in enumerate(array):
            for x, index in enumerate(line):

                cell = Cell(self, index, y, x)
                # temporary
                if x == self.cols // 2 and y == self.lines // 2:
                    self.spawn_player(cell)
                self.board.append(cell)

    def spawn_player(self, cell):
        # add a check for enemies in cell?
        # *if* they are already spawned in at this point
        # add a check for repeated use?
        self.player = Character(cell, "µ", player=True)
        cell.character = self.player

    def flat(self, y, x):
        return y * self.cols + x

    def coord(self, coord):
        return (coord // self.cols, coord % self.cols)

    def build(self):
        for y, line in enumerate(self.raw_level):
            for x, char in enumerate(line):
                self.board.append(Cell(self, char, y, x))

    def get_cell(self, y, x):
        if y < 0 or y >= self.lines:
            return None
        if x < 0 or x >= self.cols:
            return None
        return self.board[self.flat(y, x)]

    def set_player(self, character):
        self.player = character
