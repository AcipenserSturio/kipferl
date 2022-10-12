import curses

from .display import Display
from .level import Level
from .utils import CursesContextManager

class Game:
    def __init__(self):
        self.game_quit = False

    def init_palette(self):
        for bg in range(1, 256):
            curses.init_pair(bg, curses.COLOR_BLACK, bg)

    def run(self):
        with CursesContextManager() as stdscr:

            self.init_palette()

            self.level = Level()

            self.display = Display(self.level, curses.LINES-1, curses.COLS-1)

            while not self.game_quit:
                turn = self.handle(stdscr.getch())
                if turn:
                    self.level.enemy_turn()
                    self.display.refresh()
                    self.level.ticked = set()

    def handle(self, key):
        match key:
            case curses.KEY_LEFT:
                self.level.player.walk("l")
                return True
            case curses.KEY_RIGHT:
                self.level.player.walk("r")
                return True
            case curses.KEY_UP:
                self.level.player.walk("u")
                return True
            case curses.KEY_DOWN:
                self.level.player.walk("d")
                return True
            case 113: # q
                self.game_quit = True
                return False
            case 32: # space
                return True
            case _:
                return False
