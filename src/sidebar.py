import curses

SIDEBAR_WIDTH = 40

class Sidebar:
    def __init__(self):
        self.lines = curses.LINES
        self.cols = SIDEBAR_WIDTH
        self.y = 0
        self.x = curses.COLS-self.cols
        self.window = curses.newwin(self.lines, self.cols, self.y, self.x)
        self.window.bkgd(" ", curses.color_pair(188))
        self.draw_border()

    def refresh(self, player):
        self.window.clear()
        self.draw_border()
        self.window.move(1, 1)
        text = f"Coins: {player.coins}"
        self.window.addstr(text)
        self.window.refresh()

    def draw_border(self):
        self.window.attrset(curses.color_pair(238))
        self.window.border(" ", " ", " ", " ", " ", " ", " ", " ")
        self.window.attrset(0)
