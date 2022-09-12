import curses

from .keyboard import KeyboardHandler

class Game:
    def __init__(self):
        self.keyboard_handler = KeyboardHandler()

    def run(self):
        curses.wrapper(update_screen)


def update_screen(stdscr):
    stdscr.clear()
    stdscr.refresh()

    x_offset = 0
    y_offset = 0

    curses.init_pair(255, 255, 69)

    pad = curses.newpad(300, 300)
    pad.addstr("Test тест Ελληνικά",
               curses.color_pair(255))

    while True:
        pad.timeout(10)
        key = stdscr.getch()
        match key:
            case curses.KEY_LEFT:
                x_offset += -2
            case curses.KEY_RIGHT:
                x_offset += 2
            case curses.KEY_UP:
                y_offset += -1
            case curses.KEY_DOWN:
                y_offset += 1
        pad.refresh(y_offset, x_offset, 0, 0, 30, 30)
