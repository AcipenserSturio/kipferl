import curses

from .utils import CursesContextManager

class Game:
    def __init__(self):
        self.x_offset = 0
        self.y_offset = 0

    def run(self):
        with CursesContextManager() as stdscr:
            stdscr.clear()
            stdscr.refresh()

            curses.init_pair(255, 255, 69)

            pad = curses.newpad(300, 300)
            pad.addstr("Test тест Ελληνικά",
                    curses.color_pair(255))

            while True:
                pad.timeout(10)
                key = stdscr.getch()
                self.handle(key)
                self.testprint(pad, str(key))
                self.testprint(pad, str(curses.KEY_LEFT))
                pad.refresh(self.y_offset, self.x_offset, 0, 0, 30, 70)

    def handle(self, key):
        match key:
            case curses.KEY_LEFT:
                self.testprint(pad)
                self.x_offset += -2
            case curses.KEY_RIGHT:
                self.testprint(pad)
                self.x_offset += 2
            case curses.KEY_UP:
                self.testprint(pad)
                self.y_offset += -1
            case curses.KEY_DOWN:
                self.testprint(pad)
                self.y_offset += 1

    def testprint(self, win, message):
        win.addstr(message + " ", curses.color_pair(255))

