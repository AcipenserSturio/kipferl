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
        self.max_health = 100
        self.health = self.max_health

    def walk(self, direction, avoid_water=False):
        """
        Attempt to move from the current position to a neighboring Cell in the given direction.
        """
        # direction = "u"
        # direction = "d"
        # direction = "l"
        # direction = "r"
        origin = self.cell
        destination = origin.neighbor(direction)
        if not destination:
            return
        if avoid_water and not destination.terrain.land:
            return
        if self.player:
            play(destination.terrain.sound)
        if not destination.terrain.walkable:
            return
        if destination.character:
            return

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
        play("coin.wav")
        drop.cell.drop = None
        if drop.char == curses.ACS_DIAMOND:
            self.coins += random.randrange(2,7)

    def wander(self):
        """
        Choose a random direction to walk in, and attempt to walk.
        Prefer to continue moving in the same direction as last turn.
        Avoid water.
        """
        direction = random.choice(["u", "d", "l", "r"] + [self.facing]*3)
        self.walk(direction, avoid_water=True)

    def heal(self):
        """Add health, up to a maximum value."""
        self.health += 5
        if self.health > self.max_health:
            self.health = self.max_health

    def hunt(self):
        """
        Look for the player.
        If nearby, approach the player.
        If next to the player, attack.
        """
        if self.player:
            return
        player = self.cell.level.player
        distance_x, distance_y = self.cell.x - player.cell.x, self.cell.y - player.cell.y
        if abs(distance_x) + abs(distance_y) > 25:
            return
        if abs(distance_x) + abs(distance_y) < 3:
            self.attack(player)
            return
        if abs(distance_x) > abs(distance_y):
            if distance_x > 0:
                return "l"
            return "r"
        if distance_y > 0:
            return "u"
        return "d"

    def attack(self, character):
        """
        Deal damage to the Character's health.
        """
        damage = random.randrange(1, 5)
        if self.player:
            damage *= 10
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
        if self.player:
            self.cell.level.quick_end_turn = True
            self.cell.level.game.over()
            return
        self.cell.level.enemies.remove(self)
        self.cell.character = None
        self.cell.tick()

    def attack_nearby(self):
        """
        Find closest Character in a radius, attack.
        """
        enemies = sorted(self.cell.level.enemies, key=self.euclidean, reverse=True)
        if not enemies:
            return
        closest_enemy = enemies.pop()
        if self.euclidean(closest_enemy) > 3:
            return
        self.attack(closest_enemy)

    def euclidean(self, character):
        """
        Return Euclidean distance between self and Character.
        """
        return (self.cell.x - character.cell.x) ** 2 +(self.cell.y - character.cell.y) ** 2
