import curses

class CursesContextManager:
    """
    A context manager which wraps around access to the curses library
    to set up and reset the terminal behaviour.
    This is a more pythonic reimplementation of an existing wrapper
    provided by the python curses library.
    """
    def __enter__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        try:
            curses.start_color()
        except:
            pass
        return self.stdscr

    def __exit__(self, ex_type, ex_value, ex_traceback):
        self.stdscr.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        return False
