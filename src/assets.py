"""
Holds text-based assets imported from the assets folder.
"""

import json

with open("assets/cells.json", encoding="utf8") as f:
    cell_qualities = json.load(f)
