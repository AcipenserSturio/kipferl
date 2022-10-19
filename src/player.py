import curses
import random

from .character import Character
from .sound import play

class Player(Character):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.coins = 0
        self.death_causes_game_over = True
        self.damage_modifier = 5

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
        enemies = sorted(self.cell.level.enemies, key=self.euclidean, reverse=True)
        if not enemies:
            return
        closest_enemy = enemies.pop()
        if self.euclidean(closest_enemy) > 3:
            return
        self.attack(closest_enemy)

    def collect(self, drop):
        """Collect a Drop."""
        play("coin.wav")
        drop.cell.drop = None
        if drop.char == curses.ACS_DIAMOND:
            self.coins += random.randrange(2,7)

