import unittest

from src.game import Game
from src.engine.enemy import Enemy
from src.engine.character import Character
from src.engine.player import Player


class CharacterTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_enemies_types(self):
        assert isinstance(self.game.level.enemies, set)

    def test_enemy_types(self):
        for enemy in self.game.level.enemies:
            assert isinstance(enemy, Character)
            assert isinstance(enemy, Enemy)
            assert not isinstance(enemy, Player)

    def test_player_types(self):
        assert isinstance(self.game.level.player, Player)

    def test_player_death_causes_game_over(self):
        assert self.game.level.player.death_causes_game_over is True

