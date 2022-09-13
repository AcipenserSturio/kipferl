import curses

from .character import Character

class Cell:
    def __init__(self, level, char, y, x):
        self.level = level
        self.char = char
        self.y = y
        self.x = x
        self.init_qualities()

    def neighbor(self, direction):
        # direction = "u"
        # direction = "d"
        # direction = "l"
        # direction = "r"
        x_offset = 0
        y_offset = 0
        match direction:
            case "u":
                y_offset -= 1
            case "d":
                y_offset += 1
            case "l":
                x_offset -= 1
            case "r":
                x_offset += 1
        return self.level.get_cell(self.y+y_offset, self.x+x_offset)

    def init_qualities(self):
        match self.char:
            case "#":
                self.color = 56
                self.walkable = False
                self.character = None
            case ".":
                self.color = 85
                self.walkable = True
                self.character = None
            case "A":
                self.color = 39
                self.walkable = True
                self.character = Character()
                self.level.set_player(self.character)
            case _:
                self.color = 1
                self.walkable = True
                self.character = None


    def draw(self, window):
        window.addch(self.char, curses.color_pair(self.color))
