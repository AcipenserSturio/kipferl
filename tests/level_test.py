import unittest

from src.engine.level import Level

class LevelTest(unittest.TestCase):

    def setUp(self):
        self.level = Level(self)

    def test_basic_generation(self):
        assert self.level.board is not None

    def test_island_detection(self):
        assert self.level.islands is not None
        assert len(self.level.islands) > 0
