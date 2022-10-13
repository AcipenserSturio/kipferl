"""
Contains the Drop class, which represents an immovable object in a Cell.
"""

class Drop:
    """
    An immovable object in a Cell.
    Can be picked up by a player Character.
    """

    def __init__(self, cell, char):
        self.cell = cell
        self.char = char
