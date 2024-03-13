from pokemon import *
from pokedex import * # Replace star imports later
from moves import *
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
    def ResetUI(self):
        os.run("cls")
        print(str(self.ours))
        print(str(self.other))
        print()
        for x in self.messages:
            print(x)
        self.messages = []
    def addMessage(self, add):
        self.messages += add
def battle(playerPokemon, enemyPokemon):
    UIOBJ = UI(playerPokemon, enemyPokemon)
    # Here we go.
    # Start with the intro.
    # Then go into main battle loop:
    # Start loop:
    while playerPokemon.Health > 0 and enemyPokemon.Health > 0:
        # 1. Print out the UI object.
        print(UIOBJ)
        # 1.5. Tick status effects for player
        
        # 2. Reprint output.
        # 3. Ask player for input.
        # 4. Use move.
        # 5. Print out UI (again), with messages.
        # 5.5. Tick status effects for AI
        # 6. Have AI use a random move.
        # 7. Print out UI (again again), with messages.
        # 8. Loop.