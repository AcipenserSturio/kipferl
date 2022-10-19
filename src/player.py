from .character import Character

class Player(Character):

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
