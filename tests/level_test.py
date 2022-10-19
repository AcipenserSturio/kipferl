import unittest

import numpy

from src.level import Level

class LevelGeneratorTest(unittest.TestCase):
    def test_basic_generation(self):
        level = Level(self)
        assert level.board is not None
