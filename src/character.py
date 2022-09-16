class Character:
    def __init__(self, cell, char):
        self.cell = cell
        self.char = char
        self.coins = 0
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

                self.cell = destination
                self.facing = direction

                if destination.drop:
                    self.collect(destination.drop)

                origin.tick()
                destination.tick()

    def collect(self, drop):
        drop.cell.drop = None
        match drop.char:
            case "ꙮ":
                self.coins += 5
