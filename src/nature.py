"""
Contains the Nature class, which represents a thematic grouping of spells.
"""

class Nature:
    """
    A thematic grouping of spells.
    """

    def __init__(self, *_, **kwargs):
        self.__dict__.update(kwargs)
