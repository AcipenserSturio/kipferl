"""
Contains the Terrain class, which represents immutable features present in a Cell.
"""

class Terrain:
    """
    Immutable features present in a Cell.
    """

    def __init__(self, *_, **kwargs):
        self.__dict__.update(kwargs)
