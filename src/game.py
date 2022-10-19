"""
Contains the Game class, which controls high-level game logic
and communicates game state with the curses display.
"""

import curses

from .display import Display
from .level import Level
from .utils import CursesContextManager

class Game:
    """
    Controls high-level game logic like starting, quitting the game, starting a level.
    Communicates game state with the curses display.
    Processes turns.
    """
    def __init__(self):
        self.game_quit = False
        self.quick_end_turn = False
        self.level = None
        self.display = None

    def init_palette(self):
        for index in range(1, 256):
            curses.init_pair(index, curses.COLOR_BLACK, index)

    def run(self):
        """
        Initialise the Level and Display.
        Process player input and game logic, until player quits the game.
        """
        with CursesContextManager() as stdscr:

            self.init_palette()

            self.level = Level(self)
            self.display = Display(self.level, curses.LINES-1, curses.COLS-1)

            while not self.game_quit:
                turn = self.handle(stdscr.getch())
                if turn:
                    self.enemy_turn()
                    self.display.refresh()
                    self.level.ticked = set()

    def enemy_turn(self):
        """
        Process the turn for each Enemy.
        """
        self.quick_end_turn = False
        for enemy in self.level.enemies:
            if self.quick_end_turn:
                break
            enemy.do_turn()

    def handle(self, key):
        """
        Depending on player input,
        interact with Player or UI elements.
        If the player action ends the turn, return True, else return False.
        """
        if key == curses.KEY_LEFT:
            self.level.player.walk("l")
            return True
        if key == curses.KEY_RIGHT:
            self.level.player.walk("r")
            return True
        if key == curses.KEY_UP:
            self.level.player.walk("u")
            return True
        if key == curses.KEY_DOWN:
            self.level.player.walk("d")
            return True
        if key == 113: # q
            self.game_quit = True
            return False
        if key == 101: # e
            self.level.player.heal()
            return True
        if key == 32: # space
            self.level.player.attack_nearby()
            return True
        return False

    def over(self):
        self.quick_end_turn = True
        self.level = Level(self)
        self.display = Display(self.level, curses.LINES-1, curses.COLS-1)
