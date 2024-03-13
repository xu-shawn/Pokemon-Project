from pokemon import *
import random
from battle import battle
from pokedex import *


def clearScrn():
    """
    clearScrn()
    Clears the screen and waits a small amount of time
    """
    if os.name == "nt":
        os.run("clear")
    else:
        os.system("clr")
    time.wait(0.5)


def display_welcome():
    print("Welcome to the Pokémon Adventure!")
    print(
        "In this game, you will choose a starter Pokémon to battle against wild Pokémon."
    )
    print("You can capture Pokémon by defeating them in battles.")
    print("Let's start by choosing your first Pokémon!")


def choose_starter():
    starters = ["Bulbasaur", "Charmander", "Squirtle"]
    print("Please choose your starter Pokémon:")
    for starter in starters:
        print(f"- {starter}")

    choice = input("Your choice: ").capitalize()
    while choice not in starters:
        print(
            "That's not a valid Pokémon. Please choose Bulbasaur, Charmander, or Squirtle."
        )
        choice = input("Your choice: ").capitalize()

    print(f"Great choice! You chose {choice}.")
    return choice


def display_battle_instructions():
    MainUI.addMessage("Now that you have your Pokémon, you're ready to battle.")
    MainUI.addMessage("During a battle, you can choose a move for your Pokémon to use.")
    MainUI.addMessage("Each move has different effects, so choose wisely.")
    MainUI.addMessage("Type the number associated with the move to choose it.")


def choose_move(moves):  # Function retired, moved to battle.py
    pass


starters = {
    "Bulbasaur": Pokemon(
        "Bulbasaur",
        ["Grass"],
        100,
        ["Scratch", "Tackle", "Vine Whip"],
        20,
        20,
        25,
        0,
        "A Bulbasaur. What else is there to say?",
        [],
    ),
    "Charmander": Pokemon(
        "Charmander",
        ["Fire"],
        80,
        ["Scratch", "Tackle", "Ember"],
        25,
        15,
        20,
        0,
        "A Charmander. What else is there to say?",
        [],
    ),
    "Squirtle": Pokemon(
        "Bulbasaur",
        ["Water"],
        120,
        ["Scratch", "Tackle", "Bubble"],
        15,
        25,
        20,
        0,
        "A Squirtle. What else is there to say?",
        [],
    ),
}


def main() -> None:
    # Initialize Player Pokedex
    playerPokedex = Pokedex()
    display_welcome()
    starter_name = choose_starter()
    starterPokemon = starters[starter_name]
    playerPokedex.add_pokemon(starterPokemon)
    del starters[starter_name]
    display_battle_instructions()
    # First battle:
    battle(playerPokedex.activePokemon, random.choice(list(starters.values())))


if __name__ == "__main__":
    main()
