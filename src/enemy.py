import random

from .character import Character

class Enemy(Character):

    def wander(self):
        """
        Choose a random direction to walk in, and attempt to walk.
        Prefer to continue moving in the same direction as last turn.
        Avoid water.
        """
        direction = random.choice(["u", "d", "l", "r"] + [self.facing]*3)
        self.walk(direction, avoid_water=True)

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
