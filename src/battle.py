from UIObject import MainUI
from random import choice


def requestMove(player):
    print("Choose a move:")
    moveIndex = 0
    moves = player.moves
    for move in moves:
        print(f"{moveIndex} - {move}")
        moveIndex += 1
    move = input("Your move: ")
    # Hacky solution, clean up.
    moveList = [str(x) for x in range(0, moveIndex)]
    while move not in moveList:
        print("That's not a valid move. Please choose again.")
        # Maybe 1 index it?
        move = input(f"Your move (0 to {moveIndex - 1}): ")
    selectedMove = moves[int(move)]
    # MainUI is a global obj.
    MainUI.addMessage(f"{player.name} used {selectedMove}")
    return selectedMove


def battle(playerPokemon, enemyPokemon):
    MainUI.resetPokemon(playerPokemon, enemyPokemon)
    # Here we go.
    # Start with the intro.
    # Then go into main battle loop:
    # Start loop:
    while playerPokemon.health > 0 and enemyPokemon.health > 0:
        playerPokemon.TickStatusEffects()
        if playerPokemon.health <= 0:
            break
        # 1. Tick status effects for player
        # 2. Print out the UI object.
        MainUI.ResetUI()
        # 3. Ask player for input.
        toUse = requestMove(playerPokemon)
        # 4. Use move.
        playerPokemon.useMove(toUse, enemyPokemon)
        if enemyPokemon.health <= 0:
            break
        # 5. Print out UI (again), with messages.
        MainUI.ResetUI()
        # 5.5. Tick status effects for AI
        enemyPokemon.TickStatusEffects()
        if enemyPokemon.health <= 0:
            break
        # 6. Have AI use a random move.
        if enemyPokemon.health > 0:
            the = choice(enemyPokemon.moves)
            MainUI.addMessage(f"{enemyPokemon.name} used {the}")
            enemyPokemon.useMove(the, playerPokemon)
        # 7. Print out UI (again again), with messages.
        MainUI.ResetUI()
        # 8. Loop.
    MainUI.ResetUI()