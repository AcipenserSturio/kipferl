"""
Contains the Cell class, which represents a single spacial unit of a level.
"""

from ..assets.assets import read_terrains

class Cell:
    """
    A single spacial unit of a level.
    Corresponds to a square pixel in the curses display.
    Contains Terrain.
    May contain a Character and/or a Drop.
    """
    def __init__(self, level, index, y, x):
        self.level = level
        self.island = None
        self.y = y
        self.x = x
        self.character = None
        self.drop = None
        self.terrain = read_terrains()[index]

    def neighbor(self, direction):
        """
        Return the cell's immediate neighbor.
        Return None if the neighbor does not exist.
        """
        # direction = "u"
        # direction = "d"
        # direction = "l"
        # direction = "r"
        x_offset = 0
        y_offset = 0
        if direction == "u":
            y_offset -= 1
        elif direction == "d":
            y_offset += 1
        elif direction == "l":
            x_offset -= 1
        elif direction == "r":
            x_offset += 1
        return self.level.get_cell(self.y+y_offset, self.x+x_offset)

    def drawn_char(self):
        """
        Return symbol which represents the Cell on the Display.
        Prioritise displaying Character > Drop > cell terrain.
        """
        if self.character:
            return self.character.char
        if self.drop:
            return self.drop.char
        return self.terrain.char

    def tick(self):
        """
        Inform the Level that the contents of the Cell have been changed,
        requiring a Display update.
        """
        self.level.ticked.add(self)
