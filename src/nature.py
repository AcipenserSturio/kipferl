"""
Contains the Nature class, which represents a thematic grouping of spells.
"""

class Nature:
    """
    A thematic grouping of spells.
    """

    def __init__(self,
            name,
            char,
            color,
            active,
            passive
        ):

        self.name = name
        self.char = char
        self.color = color
        self.active = active
        self.passive = passive
