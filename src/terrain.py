"""
Contains the Terrain class, which represents immutable features present in a Cell.
"""

from dataclasses import dataclass

@dataclass
class Terrain:
    """
    Immutable features present in a Cell.
    """
    name: str
    char: str
    color: int
    land: bool
    elevation: float
    walkable: bool
    sound: str
