import curses

from .utils import CursesContextManager

class Game:
    def __init__(self):
        self.x_offset = 0
        self.y_offset = 0

    def init_palette(self):
        for bg in range(1, 256):
            curses.init_pair(bg, curses.COLOR_BLACK, bg)

    def run(self):
        with CursesContextManager() as stdscr:

            self.init_palette()

            pad = curses.newpad(33, 32)
            for num in range(256):
                pad.addch("#", curses.color_pair(num))
            for num in range(256):
                pad.addch("#", curses.color_pair(num) | curses.A_REVERSE)

            while True:
                pad.timeout(10)
                self.handle(stdscr.getch())
                pad.refresh(self.y_offset, self.x_offset, 0, 0, curses.LINES-1, curses.COLS-1)

    def handle(self, key):
        match key:
            case curses.KEY_LEFT:
                self.x_offset += -2
            case curses.KEY_RIGHT:
                self.x_offset += 2
            case curses.KEY_UP:
                self.y_offset += -1
            case curses.KEY_DOWN:
                self.y_offset += 1
