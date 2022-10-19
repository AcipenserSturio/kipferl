"""
Contains the Sidebar class, which represents a UI field with player data.
"""

import curses

SIDEBAR_WIDTH = 40

class Sidebar:
    """
    A UI field with player data.
    Includes keyboard hints.
    """
    def __init__(self, display_lines, display_cols):
        self.lines = display_lines + 1
        self.cols = SIDEBAR_WIDTH
        self.y = 0
        self.x = display_cols - self.cols + 1
        self.window = curses.newwin(self.lines, self.cols, self.y, self.x)
        # self.window.bkgd(" ", curses.color_pair(188))
        self.draw_border()

    def refresh(self, player):
        """
        Fill Sidebar with player data, keyboard hints, and border.
        Refresh the screen.
        """
        self.window.clear()
        self.window.move(2, 0)
        text = "".join([
                f"  Coins: {player.coins}\n",
                f"  Health: {player.health} / {player.max_health}\n",
                f"  Facing: {player.facing}\n",
                f"  {player.cell.terrain.name} at ({player.cell.x}, {player.cell.y})\n",
                f"  Seed: {player.level.seed}\n",
                f"  Enemies: {len(player.level.enemies)}\n",
                f"  Island: {player.cell.island.nature.name if player.cell.island is not None else None} \n",
                ])
        self.window.addstr(text)
        self.window.move(self.lines-8, 0)

        controls = [(curses.ACS_UARROW, "move up"),
                    (curses.ACS_LARROW, "move left"),
                    (curses.ACS_DARROW, "move down"),
                    (curses.ACS_RARROW, "move right"),
                    ("E", "heal"),
                    (" ", "attack"),
                    ("Q", "quit"),]
        for char, hint in controls:
            self.draw_control(char, hint)

        self.draw_border()
        self.window.refresh()

    def draw_border(self):
        """
        Draw a grey border around the Sidebar.
        Overrides any text that appears on the edge of the Sidebar.
        """
        self.window.attrset(curses.color_pair(238))
        self.window.border(" ", " ", " ", " ", " ", " ", " ", " ")
        self.window.attrset(0)

    def draw_control(self, char, hint):
        """
        Write a keyboard hint at the current cursor position.
        Use green to highlight the key.
        """
        self.window.addstr("  [ ", curses.color_pair(2) | curses.A_REVERSE)
        self.window.addch(char, curses.color_pair(2) | curses.A_REVERSE)
        self.window.addstr(" ] ", curses.color_pair(2) | curses.A_REVERSE)
        self.window.addstr(hint + "\n")
