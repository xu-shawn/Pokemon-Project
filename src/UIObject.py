import os
import time


def dramaticPause():
    """
    dramaticPause()
    Another name for "three second wait"
    """
    time.sleep(3)
    MainUI.flush_input()

# TextModifiers
# Stores ANSI escape sequences that change the text's color and stuff


class TextModifiers:
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


TM = TextModifiers  # Alias


class UI:
    def flush_input(self):
        try:
            import msvcrt
            while msvcrt.kbhit():
                msvcrt.getch()
        except ImportError:
            import sys
            import termios  # for linux/unix
            termios.tcflush(sys.stdin, termios.TCIOFLUSH)

    def __init__(self, p1, p2):
        self.ours = p1
        self.other = p2
        self.messages = []

    def addMessage(self, add):
        self.messages.append(add)

    def resetPokemon(self, p1, p2):
        self.ours = p1
        self.other = p2

    def ResetUI(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print("Your pokemon:")
        print(str(self.ours))
        print("Their pokemon:")
        print(str(self.other))
        print()
        for x in self.messages:
            print(x)
        self.messages = []
        dramaticPause()


global MainUI
MainUI = UI(None, None)
