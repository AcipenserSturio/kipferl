"""
Contains the Drop class, which represents an immovable object in a Cell.
"""

from dataclasses import dataclass

from .cell import Cell

@dataclass
class Drop:
    """
    An immovable object in a Cell.
    Can be picked up by a player Character.
    """
    cell: Cell
    char: int
