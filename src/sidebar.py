import curses

SIDEBAR_WIDTH = 60

class Sidebar:
    def __init__(self):
        self.lines = curses.LINES
        self.cols = SIDEBAR_WIDTH
        self.y = 0
        self.x = curses.COLS-self.cols
        self.window = curses.newwin(self.lines, self.cols, self.y, self.x)
        self.draw_border()

    def refresh(self):
        self.window.refresh()

    def draw_border(self):
        self.window.attrset(curses.color_pair(36))
        self.window.border(" ", " ", " ", " ", " ", " ", " ", " ")
        self.window.attrset(0)
