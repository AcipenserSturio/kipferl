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
            self.level.load("assets/levels/huge")
            self.level.build()

            self.display = curses.newwin(curses.LINES, curses.COLS)

            while not self.game_quit:
                self.refresh()
                self.display.timeout(10)
                self.handle(stdscr.getch())

    def handle(self, key):
        match key:
            case curses.KEY_LEFT:
                self.level.player.walk("l")
            case curses.KEY_RIGHT:
                self.level.player.walk("r")
            case curses.KEY_UP:
                self.level.player.walk("u")
            case curses.KEY_DOWN:
                self.level.player.walk("d")
            case 113: # q
                self.game_quit = True

    def refresh(self):
        self.x_offset = self.level.player.cell.x
        self.y_offset = self.level.player.cell.y
        for y in range(curses.LINES):
            for x in range(curses.COLS):
                cell = self.level.get_cell(y+self.y_offset, x+self.x_offset)
                if cell:
                    self.put(cell, y, x)
        self.display.refresh()

    def put(self, cell, y, x):
        # Edge case last character. todo: fix
        if (y == curses.LINES-1) and (x == curses.COLS-1):
            return
        color = curses.color_pair(cell.color)
        char = cell.character.char if cell.character else " "
        self.display.move(y, x)
        self.display.addch(char, color)
