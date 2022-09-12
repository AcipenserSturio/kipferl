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
        self.stdscr.keypad(1)
        try:
            curses.start_color()
        except:
            pass
        # Clearing and refreshing is not in the official wrapper:
        # However, there is no harm in doing it as early as possible.
        self.stdscr.clear()
        self.stdscr.refresh()
        return self.stdscr

    def __exit__(self, ex_type, ex_value, ex_traceback):
        self.stdscr.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        return False
