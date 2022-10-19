"""
Contains the Nature class, which represents a thematic grouping of spells.
"""
from dataclasses import dataclass

@dataclass
class Nature:
    """
    A thematic grouping of spells.
    """
    name: str
    char: str
    color: int
    active: str
    passive: str
