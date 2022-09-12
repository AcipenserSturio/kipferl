from .keyboard import KeyboardHandler
from .display import Display

class Game:
    def __init__(self):
        pass
    def run(self):
        keyboard_handler = KeyboardHandler()
        display = Display()
        display.run()
