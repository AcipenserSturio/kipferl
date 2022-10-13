"""
Contains the Cell class, which represents a single spacial unit of a level.
"""

import random

import curses

from .assets import cell_qualities
from .character import Character
from .drop import Drop

ENEMIES = [chr(i+97) for i in range(26)]

class Cell:
    """
    A single spacial unit of a level.
    Corresponds to a square pixel in the curses display.
    Includes terrain data.
    May contain a Character and/or a Drop.
    """
    def __init__(self, level, index, y, x):
        self.level = level
        self.y = y
        self.x = x
        self.character = None
        self.drop = None
        self.walkable = False
        self.island = None
        self.init_qualities(index)

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

    def init_qualities(self, index):
        """
        Import available Cell types from game assets.
        Initialise various qualities based on game assets.
        """
        if index not in cell_qualities:
            # panic
            self.color = 2
            self.char = "F"
            # add more qualities later if needed

        qualities = cell_qualities[index]
        self.color = qualities["color"]
        self.char = qualities["char"][0]
        self.name = qualities["name"]
        self.land = qualities["land"]
        self.sound = qualities["sound"] if "sound" in qualities else None
        self.walkable = qualities["walkable"]
        self.spawnable = qualities["spawnable"]

        if self.spawnable:
            if random.random() < 0.03:
                self.drop = Drop(self, curses.ACS_DIAMOND)
            elif random.random() < 0.004:
                self.character = Character(self, random.choice(ENEMIES))
                self.level.enemies.add(self.character)

    def drawn_char(self):
        """
        Return symbol which represents the Cell on the Display.
        Prioritise displaying Character > Drop > cell terrain.
        """
        if self.character:
            return self.character.char
        if self.drop:
            return self.drop.char
        return " "

    def tick(self):
        """
        Inform the Level that the contents of the Cell have been changed,
        requiring a Display update.
        """
        self.level.ticked.add(self)
