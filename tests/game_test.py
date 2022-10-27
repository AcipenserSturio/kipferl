import unittest

from src.game import Game

class GameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game(seed=0)

    def test_basic_generation(self):
        self.game.run_headless()
        assert self.game.level is not None

    # def test_player_movement(self):
    #    self.game.run_headless("w")
    #    assert (self.game.level.player.cell.y,
    #            self.game.level.player.cell.x) == (127, 128)
