import curses

class Display:
    def __init__(self, level, lines, cols):
        self.level = level
        self.lines = lines
        self.cols = cols
        self.window = curses.newpad(self.level.lines, self.level.cols)
        self.draw()
        self.refresh()

    def draw(self):
        for cell in self.level.board:
            self.put(cell)

    def update(self):
        for cell in self.level.ticked:
            self.put(cell)

    def put(self, cell):
        # Skip updating if last character. todo: fix
        if (cell.y == self.level.lines-1) and (cell.x == self.level.cols-1):
            return
        color = curses.color_pair(cell.color)
        char = cell.character.char if cell.character else " "
        self.window.move(cell.y, cell.x)
        self.window.addch(char, color)

    def refresh(self):
        self.update()
        y_offset = self.level.player.cell.y
        x_offset = self.level.player.cell.x
        self.window.refresh(y_offset, x_offset, 0, 0, self.lines, self.cols)
        self.window.timeout(10)
