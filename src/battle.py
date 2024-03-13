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
        dramaticPause()
    def addMessage(self, add):
        self.messages += add
def requestMove(player, UI):
    print("Choose a move:")
    moveIndex = 0 
    moves = player.moves
    for move in moves:
        print(f"{moveIndex} - {move}")
        moveIndex += 1
    move = input("Your move: ")
    moveList = [str(x) for x in range(0, moveIndex)] # Hacky solution, clean up.
    while move not in moveList:
        print("That's not a valid move. Please choose again.")
        move = input(f"Your move (0 to {moveIndex - 1}): ") # Maybe 1 index it?
    selectedMove = moves[int(move)]
    UI.addMessage(f"{player.Name} used {selectedMove}") # Could also make UIOBJ global
    return selectedMove
def battle(playerPokemon, enemyPokemon):
    UIOBJ = UI(playerPokemon, enemyPokemon)
    # Here we go.
    # Start with the intro.
    # Then go into main battle loop:
    # Start loop:
    while playerPokemon.health > 0 and enemyPokemon.health > 0:
        # 1. Print out the UI object.
        UIOBJ.ResetUI()
        # 1.5. Tick status effects for player
        playerPokemon.TickStatusEffects()
        # 2. Reprint output.
        UIOBJ.ResetUI()
        # 3. Ask player for input.
        toUse = requestMove(playerPokemon, UIOBJ)
        # 4. Use move.
        playerPokemon.move(toUse)
        # 5. Print out UI (again), with messages.

        # 5.5. Tick status effects for AI

        # 6. Have AI use a random move.

        # 7. Print out UI (again again), with messages.

        # 8. Loop.