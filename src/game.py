import curses

from .level import Level
from .utils import CursesContextManager

class Game:
    def __init__(self):
        self.x_offset = 0
        self.y_offset = 0
        self.game_quit = False

    def init_palette(self):
        for bg in range(1, 256):
            curses.init_pair(bg, curses.COLOR_BLACK, bg)

    def run(self):
        with CursesContextManager() as stdscr:

            self.init_palette()

            self.level = Level()
            self.level.load("assets/levels/temp")
            self.level.build()

            pad = curses.newpad(self.level.lines, self.level.cols)
            self.level.draw(pad)

            while not self.game_quit:
                pad.refresh(self.y_offset, self.x_offset, 0, 0, curses.LINES-1, curses.COLS-1)
                pad.timeout(10)
                self.handle(stdscr.getch())

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
            case 113: # q
                self.game_quit = True
