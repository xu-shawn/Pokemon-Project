from pokemon import Pokemon
import random
from battle import battle, MainUI
from pokedex import Pokedex
import os
import time
# TODO: FIX MAIN GAME LOOP
# TODO: ADD MORE POKEMON
# TODO: FIX BATTLE LOOP
# REMEMBER TO LINT BEFORE TURNING IN

def clearScrn():
    """
    clearScrn()
    Clears the screen and waits a small amount of time
    """
    if os.name == "nt":
        os.system("clear")
    else:
        os.system("clr")
    time.wait(0.5)


def display_welcome():
    print("Welcome to the Pokémon Adventure!")
    print(
        """In this game, you will choose a starter
Pokémon to battle against wild Pokémon."""
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
            "That's not a valid starter Pokémon. Please choose Bulbasaur, Charmander, or Squirtle."
        )
        choice = input("Your choice: ").capitalize()

    print(f"Great choice! You chose {choice}.")
    return choice


def display_battle_instructions():
    print("Now that you have your Pokémon, you're ready to battle.")
    print("During a battle, you can choose a move for your Pokémon to use.")
    print("Each move has different effects, so choose wisely.")
    print("Type the number associated with the move to choose it.")
    time.sleep(3)

def explore_and_battle(player_pokedex):
    wild_pokemon = random.choice(list(starters.values()))
    MainUI.addMessage(f"A wild {wild_pokemon.name} appears!")
    while not player_pokedex.defeated:
        battle(player_pokedex.active_pokemon, wild_pokemon)
        if wild_pokemon.health <= 0:
            break
        player_pokedex.fainted()
    if not player_pokedex.defeated:
        capture_attempt(player_pokedex, wild_pokemon)

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
        # NOTE: STACKED STATUS EFFECTS DOES BREAK...
        ["Scratch", "Tackle", "Ember", "Spread Covid"],
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
    time.sleep(2)
    display_battle_instructions()

    while not player_pokedex.defeated:
        explore_and_battle(player_pokedex)
        print("Between battles, all of your pokemon are healed for half of their max HP.")
        print("This does not include status effects, however.")
        time.sleep(3)
        player_pokedex.healPokemon()
        time.sleep(2)
    print("All of your pokemon have fainted, thats the end of the game. GG")

if __name__ == "__main__":
    main()
