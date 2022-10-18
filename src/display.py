"""
Contains the Display class, which represents the game's frontend,
powered by the curses library.
"""

import curses

from .sidebar import Sidebar

class Display:
    """
    The game's frontend, powered by the curses library.
    Subdivides the available screen space into the map and the Sidebar.
    Processes screen updates.
    """
    def __init__(self, level, lines, cols):
        self.sidebar = Sidebar(lines, cols)
        self.level = level
        self.lines = lines
        self.cols = cols - self.sidebar.cols
        self.window = curses.newpad(self.level.lines, self.level.cols*2)
        self.draw()
        self.refresh()

    def draw(self):
        """
        Queue up an screen update for the entire Level.
        """
        for cell in self.level.board:
            self.put(cell)

    def update(self):
        """
        Queue up an screen update only for the Cells
        that have been modified this turn.
        """
        for cell in self.level.ticked:
            self.put(cell)

    def put(self, cell):
        """
        Queue up a screen update for a single Cell.
        """
        # Skip updating if last character. todo: fix
        if (cell.y == self.level.lines-1) and (cell.x == self.level.cols-1):
            return
        color = curses.color_pair(cell.terrain.color)
        char = cell.drawn_char()
        self.window.move(cell.y, cell.x*2)
        self.window.addch(char, color)
        self.window.addch(" ", color)

    def refresh(self):
        """
        If possible, center the "camera" on the player Character.
        Refresh the screen, showing all queued updates simultaneously.
        """
        self.update()
        y_offset = clamp(self.level.player.cell.y - self.lines // 2,
                         minimum = 0,
                         maximum = self.level.lines - self.lines)
        x_offset = clamp(self.level.player.cell.x*2 - self.cols // 2,
                         minimum = 0,
                         maximum = self.level.cols*2 - self.cols)
        self.window.refresh(y_offset, x_offset, 0, 0, self.lines, self.cols)
        self.sidebar.refresh(self.level.player)
        self.window.timeout(10)


def clamp(value, minimum, maximum):
    """Return the value, clamping it into the given range."""
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value
