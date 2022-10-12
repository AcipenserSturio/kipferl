import random

import curses

from .assets import cell_qualities
from .character import Character
from .drop import Drop

ENEMIES = [chr(i+97) for i in range(26)]

class Cell:
    def __init__(self, level, index, y, x):
        self.level = level
        self.index = index
        self.y = y
        self.x = x
        self.character = None
        self.drop = None
        self.walkable = False
        self.init_qualities()

    def neighbor(self, direction):
        # direction = "u"
        # direction = "d"
        # direction = "l"
        # direction = "r"
        x_offset = 0
        y_offset = 0
        match direction:
            case "u":
                y_offset -= 1
            case "d":
                y_offset += 1
            case "l":
                x_offset -= 1
            case "r":
                x_offset += 1
        return self.level.get_cell(self.y+y_offset, self.x+x_offset)

    def init_qualities(self):
        if self.index not in cell_qualities:
            # panic
            self.color = 2
            self.char = "F"
            # add more qualities later if needed

        qualities = cell_qualities[self.index]
        self.color = qualities["color"]
        self.walkable = qualities["land"]
        self.char = qualities["char"][0]
        self.name = qualities["name"]
        self.sound = qualities["sound"] if "sound" in qualities else None

        if self.walkable:
            if random.random() < 0.03:
                self.drop = Drop(self, curses.ACS_DIAMOND)
            elif random.random() < 0.004:
                self.character = Character(self, random.choice(ENEMIES))
                self.level.enemies.add(self.character)

    def drawn_char(self):
        if self.character:
            return self.character.char
        if self.drop:
            return self.drop.char
        return " "

    def tick(self):
        self.level.ticked.add(self)
