from pokemon import *
from pokedex import * # Replace star imports later
from moves import *
from UIObject import *
import os
import time

def requestMove(player):
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
    MainUI.addMessage(f"{player.name} used {selectedMove}") # MainUI is a global obj.
    return selectedMove
def battle(playerPokemon, enemyPokemon):
    MainUI.resetPokemon(playerPokemon, enemyPokemon)
    # Here we go.
    # Start with the intro.
    # Then go into main battle loop:
    # Start loop:
    while playerPokemon.health > 0 and enemyPokemon.health > 0:
        playerPokemon.TickStatusEffects()
        # 1. Tick status effects for player
        # 2. Print out the UI object.
        MainUI.ResetUI()
        # 3. Ask player for input.
        toUse = requestMove(playerPokemon)
        # 4. Use move.
        playerPokemon.useMove(toUse, enemyPokemon)
        # 5. Print out UI (again), with messages.
        MainUI.ResetUI()
        # 5.5. Tick status effects for AI
        enemyPokemon.TickStatusEffects()
        # 6. Have AI use a random move.

        # 7. Print out UI (again again), with messages.
        MainUI.ResetUI()
        # 8. Loop.