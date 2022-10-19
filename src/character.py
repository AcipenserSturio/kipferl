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

    def __init__(self, cell, char):
        self.cell = cell
        self.char = char
        self.facing = "d"
        self.max_health = 100
        self.health = self.max_health
        self.death_causes_game_over = False
        self.damage_modifier = 1

    def can_walk_on(self, cell):
        if not cell:
            return False
        if cell.character:
            return False
        if not cell.terrain.walkable:
            return False
        return True

    def walk(self, direction, passively=False):
        """
        Attempt to move from the current position to a neighboring Cell in the given direction.
        Implemented by derived classes.
        """
        pass

    def move(self, direction):
        """
        Move Character from origin to destination.
        Do not check for validity.
        """
        origin = self.cell
        destination = origin.neighbor(direction)

        origin.character = None
        destination.character = self

        self.cell = destination
        self.facing = direction

        origin.tick()
        destination.tick()

    def heal(self):
        """Add health, up to a maximum value."""
        self.health += 5
        if self.health > self.max_health:
            self.health = self.max_health

    def attack(self, character):
        """
        Deal damage to the Character's health.
        """
        damage = random.randrange(1, 5) * self.damage_modifier
        character.health -= damage
        if character.health < 0:
            character.die()

    def die(self):
        """
        Triggered by health == 0.
        Remove Character from Cell.
        Trigger Game Over if player.
        """
        play("death.wav")
        if self.death_causes_game_over:
            self.cell.level.quick_end_turn = True
            self.cell.level.game.over()
            return
        self.cell.level.enemies.remove(self)
        self.cell.character = None
        self.cell.tick()

    def euclidean(self, character):
        """
        Return Euclidean distance between self and Character.
        """
        return (self.cell.x - character.cell.x) ** 2 +(self.cell.y - character.cell.y) ** 2
