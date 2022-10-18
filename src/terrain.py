"""
Contains the Terrain class, which represents immutable features present in a Cell.
"""

class Terrain:
    """
    Immutable features present in a Cell.
    """

    def __init__(self,
            name,
            char,
            color,
            land,
            elevation,
            walkable,
            spawnable,
            sound,
        ):

        self.name = name
        self.char = char
        self.color = color
        self.land = land
        self.elevation = elevation
        self.walkable = walkable
        self.spawnable = spawnable
        self.sound = sound
