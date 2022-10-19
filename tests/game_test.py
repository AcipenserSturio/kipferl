import unittest

from src.game import Game

class GameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_basic_generation(self):
        self.game.run_headless()
        assert self.game.level is not None
