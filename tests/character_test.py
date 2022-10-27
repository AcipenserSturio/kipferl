import unittest

from src.game import Game
from src.enemy import Enemy
from src.character import Character
from src.player import Player


class CharacterTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_types(self):
        assert isinstance(self.game.level.enemies, set)
        for enemy in self.game.level.enemies:
            assert isinstance(enemy, Character)
            assert isinstance(enemy, Enemy)
            assert not isinstance(enemy, Player)
