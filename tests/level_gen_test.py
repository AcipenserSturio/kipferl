import unittest

import numpy

from src.level_gen import LevelGenerator

class LevelGeneratorTest(unittest.TestCase):

    def setUp(self):
        self.generator = LevelGenerator(seed=0)
        self.board = self.generator.generate()

    def test_generation(self):
        assert self.board is not None

    def test_types(self):
        assert isinstance(self.board, numpy.ndarray)
