import unittest

from src.game import Game

class CharacterTest(unittest.TestCase):

    def setUp(self):
        self.game = Game(self)

    def test_types(self):
        assert isinstance(self.game.level.enemies, set)
