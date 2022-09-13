from .cell import Cell

class Level:
    def __init__(self):
        self.board = []
        self.player = None

    def load(self, filepath):
        with open(filepath) as f:
            self.raw_level = [line[:-1] for line in f.readlines()]
            self.lines = len(self.raw_level)
            self.cols = len(self.raw_level[0])

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
