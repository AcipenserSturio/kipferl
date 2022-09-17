import curses

SIDEBAR_WIDTH = 40

class Sidebar:
    def __init__(self):
        self.lines = curses.LINES
        self.cols = SIDEBAR_WIDTH
        self.y = 0
        self.x = curses.COLS-self.cols
        self.window = curses.newwin(self.lines, self.cols, self.y, self.x)
        # self.window.bkgd(" ", curses.color_pair(188))
        self.draw_border()

    def refresh(self, player):
        self.window.clear()
        self.window.move(2, 0)
        text = f"  Coins: {player.coins}\n  Coordinates: ({player.cell.x}, {player.cell.y})"
        self.window.addstr(text)
        self.window.move(self.lines-7, 0)

        controls = [(curses.ACS_UARROW, "move up"),
                    (curses.ACS_LARROW, "move left"),
                    (curses.ACS_DARROW, "move down"),
                    (curses.ACS_RARROW, "move right"),
                    ("Q", "quit"),]
        for char, hint in controls:
            self.draw_control(char, hint)

        self.draw_border()
        self.window.refresh()

    def draw_border(self):
        self.window.attrset(curses.color_pair(238))
        self.window.border(" ", " ", " ", " ", " ", " ", " ", " ")
        self.window.attrset(0)

    def draw_control(self, char, hint):
        self.window.addstr("  [ ", curses.color_pair(2) | curses.A_REVERSE)
        self.window.addch(char, curses.color_pair(2) | curses.A_REVERSE)
        self.window.addstr(" ] ", curses.color_pair(2) | curses.A_REVERSE)
        self.window.addstr(hint + "\n")
