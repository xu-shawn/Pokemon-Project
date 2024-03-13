import os
import time
def dramaticPause():
    """
    dramaticPause()
    Another name for "one second wait"
    """
    time.sleep(1)
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