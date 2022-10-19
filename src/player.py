"""
Contains the Player class, which represents a Character which is controlled by the player.
"""

import curses
import random

from .character import Character
from .sound import play

class Player(Character):
    """
    A Character which is controlled by the player.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.coins = 0
        self.artifacts = 0
        self.death_causes_game_over = True
        self.damage_modifier = 5

    def heal(self):
        """Add health, up to a maximum value."""
        play("heal.wav")
        self.health += 5
        if self.health > self.max_health:
            self.health = self.max_health

    def walk(self, direction):
        """
        Attempt to move in a direction.
        """
        origin = self.cell
        destination = origin.neighbor(direction)

        if not self.can_walk_on(destination):
            return

        play(destination.terrain.sound)
        if destination.drop:
            self.collect(destination.drop)

        self.move(direction)

    def attack_nearby(self):
        """
        Find closest Character in a radius, attack.
        """
        enemies = sorted(self.level.enemies, key=self.distance, reverse=True)
        if not enemies:
            return
        closest_enemy = enemies.pop()
        if self.distance(closest_enemy) > 3:
            return
        play("player_attack.wav")
        self.attack(closest_enemy)

    def collect(self, drop):
        """Collect a Drop."""
        drop.cell.drop = None
        if drop.char == curses.ACS_DIAMOND:
            play("coin.wav")
            self.coins += random.randrange(2,7)
        if drop.char == "@":
            play("artifact.wav")
            self.artifacts += 1
