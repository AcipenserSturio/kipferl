class Character:
    def __init__(self, cell, char):
        self.cell = cell
        self.char = char
        self.facing = "d"

    def walk(self, direction):
        # direction = "u"
        # direction = "d"
        # direction = "l"
        # direction = "r"
        origin = self.cell
        destination = origin.neighbor(direction)
        if destination:
            if destination.walkable:
                origin.character = None
                destination.character = self

                origin.tick()
                destination.tick()

                self.cell = destination
                self.facing = direction
