import unittest

import numpy

from src.level_gen import LevelGenerator

class LevelGeneratorTest(unittest.TestCase):
    def test_basic_generation(self):
        generator = LevelGenerator(seed=0)
        board = generator.generate()
        assert board is not None
        assert isinstance(board, numpy.ndarray)
