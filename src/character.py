"""
Contains the Character class, which represents an entity which occupies one cell and can move.
"""

import random

import curses

from .sound import play

class Character:
    """
    An entity, which occupies one cell and can move.
    May be controlled by the player.
    """

    def __init__(self, cell, char, player=False):
        self.cell = cell
        self.char = char
        self.player = player
        self.coins = 0
        self.facing = "d"

    def walk(self, direction):
        """
        Attempt to move from the current position to a neighboring Cell in the given direction.
        """
        # direction = "u"
        # direction = "d"
        # direction = "l"
        # direction = "r"
        origin = self.cell
        destination = origin.neighbor(direction)
        if destination:
            if self.player:
                play(destination.sound)
            if destination.walkable and not destination.character:
                origin.character = None
                destination.character = self

                self.cell = destination
                self.facing = direction

                if destination.drop and self.player:
                    self.collect(destination.drop)

                origin.tick()
                destination.tick()

    def collect(self, drop):
        """Collect a Drop."""
        drop.cell.drop = None
        match drop.char:
            case curses.ACS_DIAMOND:
                self.coins += random.randrange(2,7)

    def wander(self):
        """
        Choose a random direction to walk in, and attempt to walk.
        Prefer to continue moving in the same direction as last turn.
        """
        direction = random.choice(["u", "d", "l", "r"] + [self.facing]*3)
        self.walk(direction)
