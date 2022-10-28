"""
Contains the Enemy class, which represents a Character
which tries to move every turn and attacks Player.
"""

import random

from .character import Character
from .sound import play

class Enemy(Character):
    """
    A Character which tries to move every turn and attacks Player.
    Has "hunt" and "wander" ai behaviours.
    """
    def __init__(self, nature, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nature = nature

    def do_turn(self):
        """
        Choose between hunting and wandering behaviours.
        """
        hunt = self.hunt()
        if not hunt or random.random() < 0.3:
            self.wander()
        elif hunt:
            self.walk(hunt)
        # enemy.heal()

    def walk(self, direction, passively=False):
        """
        Attempt to move in a direction.
        """
        origin = self.cell
        destination = origin.neighbor(direction)

        if not self.can_walk_on(destination):
            return
        if passively and not destination.terrain.land:
            return
        self.move(direction)

    def wander(self):
        """
        Choose a random direction to walk in, and attempt to walk.
        Prefer to continue moving in the same direction as last turn.
        Avoid water.
        """
        direction = random.choice(["u", "d", "l", "r"] + [self.facing]*3)
        self.walk(direction, passively=True)

    def hunt(self):
        """
        Look for the player.
        If nearby, approach the player.
        If next to the player, attack.
        Return direction of movement, or None if wandering.
        """
        player = self.level.player
        distance_x, distance_y = self.cell.x - player.cell.x, self.cell.y - player.cell.y
        if abs(distance_x) + abs(distance_y) > 25:
            return None
        if abs(distance_x) + abs(distance_y) < 3:
            play(self.nature.sound)
            self.attack(player)
            return None
        if abs(distance_x) > abs(distance_y):
            if distance_x > 0:
                return "l"
            return "r"
        if distance_y > 0:
            return "u"
        return "d"
