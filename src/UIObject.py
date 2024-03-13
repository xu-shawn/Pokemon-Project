import os
import time
def dramaticPause():
    """
    dramaticPause()
    Another name for "one second wait"
    """
    time.sleep(1)
class TextModifiers: # Stores ANSI escape sequences that change the text but its actually readable
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"
TM = TextModifiers # Alias
class UI:
    def __init__(self, p1, p2):
        self.ours = p1
        self.other = p2
        self.messages = []
    def resetPokemon(self, p1, p2):
        self.ours = p1
        self.other = p2
    def ResetUI(self):
        os.run("cls")
        print(str(self.ours))
        print(str(self.other))
        print()
        for x in self.messages:
            print(x)
        self.messages = []
        dramaticPause()
    def addMessage(self, add):
        self.messages += add
global MainUI
MainUI = UI(None, None)