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
    print("Now that you have your Pokémon, you're ready to battle.")
    print("During a battle, you can choose a move for your Pokémon to use.")
    print("Each move has different effects, so choose wisely.")
    print("Type the number associated with the move to choose it.")


def explore_and_battle(player_pokedex):
    wild_pokemon = random.choice(list(starters.values()))
    print(f"\nA wild {wild_pokemon.name} appears!")
    battle(player_pokedex.active_pokemon, wild_pokemon)


def capture_attempt(player_pokedex, wild_pokemon):
    # Simplified capture mechanic
    print("Do you want to attempt to capture the wild Pokémon? (yes/no)")
    choice = input().lower()
    if choice == "yes":
        if random.randint(0, 1):
            print(f"{wild_pokemon.name} was successfully captured!")
            player_pokedex.add_pokemon(wild_pokemon)
        else:
            print(f"The wild {wild_pokemon.name} escaped!")
    else:
        print("Continuing the adventure!")


starters = {
    "Bulbasaur": Pokemon(
        "Bulbasaur",
        ["Grass"],
        20,
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
        17,
        ["Scratch", "Tackle", "Ember"],
        25,
        15,
        20,
        0,
        "A Charmander. What else is there to say?",
        [],
    ),
    "Squirtle": Pokemon(
        "Squirtle",
        ["Water"],
        23,
        ["Scratch", "Tackle", "Bubble"],
        15,
        25,
        20,
        0,
        "A Squirtle. What else is there to say?",
        [],
    ),
}


def main():
    display_welcome()
    starter_name = choose_starter()
    starterPokemon = starters[starter_name]
    player_pokedex = Pokedex()
    player_pokedex.add_pokemon(starterPokemon)
    del starters[starter_name]
    time.sleep(3)
    display_battle_instructions()

    for _ in range(3):
        explore_and_battle(player_pokedex)
        capture_attempt(player_pokedex, player_pokedex.activePokemon)


if __name__ == "__main__":
    main()
