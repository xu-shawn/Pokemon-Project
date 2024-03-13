from pokemon import Pokemon
import random
from battle import battle, MainUI
from pokedex import Pokedex
import os
import time
# REMEMBER TO LINT BEFORE TURNING IN
# There are broken moves and EXP gain is mega overtuned but im out of energy
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
        ["Scratch", "Tackle", "Ember", "Spread Covid", "P A I N"],
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
tier2 = {
    "Pikachu":Pokemon(
        "Pikachu",
        ["Electric"],
        35,
        ["Thunder Shock", "Thunderbolt"],
        40,
        30,
        55,
        9,
        "A Pikachu. It's cute and electric!",
    ),
    "Eevee":Pokemon(
        "Eevee",
        ["Normal"],
        25,
        ["Tackle", "Double Kick", "Bite"],
        30,
        25,
        35,
        64,
        "An adorable Eevee with potential.",
    ),
    "Vulpix":Pokemon(
        "Vulpix",
        ["Fire"],
        30,
        ["Ember", "Double Kick", "Fire Spin"],
        35,
        25,
        40,
        125,
        "A fox-like Pokémon with a fiery tail.",
    ),
}
tier3 = {
    "Dragonite":Pokemon(
        "Dragonite",
        ["Dragon", "Flying"],
        75,
        ["Outrage", "Wing Attack", "Dragon Claw"],
        120,
        100,
        80,
        1000,
        "A powerful dragon Pokémon capable of flying long distances.",
    ),
    "Gyardos":Pokemon(
        "Gyarados",
        ["Water", "Flying"],
        60,
        ["Aqua Tail", "Crunch", "Hyper Beam"],
        100,
        80,
        85,
        2744,
        "A fearsome sea serpent Pokémon with a vicious temper.",
    ),
    "spoon guy":Pokemon(
        "Alakazam",
        ["Psychic"],
        55,
        ["Psychic", "Future Sight", "Shadow Ball"],
        80,
        70,
        90,
        1728,
        "A highly intelligent and powerful psychic Pokémon.",
    ),
}
finalBoss = {"???":Pokemon(
    "???",
    ["???"],
    250,
    ["Absorb", "Spread Covid", "Smog", "Outrage", "Rock Throw", "P A I N"],
    100,
    100,
    100,
    15625,
    "This is what happens when someone has to come up with a boss on the spot."
)}
firstTimeAround = True
global currentEnemies 
currentEnemies = starters # This will update as the game goes on.
tier = 1
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
    global currentEnemies, firstTimeAround, tier
    if len(currentEnemies) == 0:
        tier += 1
        if tier == 2:
            currentEnemies = tier2
        elif tier == 3:
            currentEnemies = tier3
        elif tier == 4:
            currentEnemies = finalBoss
        else:
            print("Congradulations, you have defeated the final boss.")
            print("Now you, and I, can rest.")
            exit()
    wild_pokemon = random.choice(list(currentEnemies.values()))
    MainUI.addMessage(f"A wild {wild_pokemon.name} appears!")
    while not player_pokedex.defeated:
        battle(player_pokedex.active_pokemon, wild_pokemon)
        if wild_pokemon.health <= 0:
            break
        player_pokedex.fainted()
    if not player_pokedex.defeated:
        player_pokedex.active_pokemon.gainEXP((5 + int(2 ** wild_pokemon.level)))
        for pokemon in player_pokedex.collection:
            player_pokedex.collection[pokemon].gainEXP((5 + int(3 ** wild_pokemon.level))) # The active pokemon gains double XP,
            # but all pokemon gain XP, so that the non-active pokemon dont fall behind.
        capture_attempt(player_pokedex, wild_pokemon)

def capture_attempt(player_pokedex, wild_pokemon):
    # Simplified capture mechanic
    print("Do you want to attempt to capture the wild Pokémon? (yes/no)")
    choice = input().lower()
    if choice == "yes":
        if random.randint(0, 4): # High chance of capture, because oh man you will need the pokemon.
            print(f"{wild_pokemon.name} was successfully captured!")
            player_pokedex.add_pokemon(wild_pokemon)
        else:
            print(f"The wild {wild_pokemon.name} escaped!")
    else:
        print("Continuing the adventure!")
    currentEnemies.pop(wild_pokemon.name)



def main():
    global firstTimeAround
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
        if player_pokedex.defeated:
            break
        if firstTimeAround:
            print("Between battles, all of your pokemon are healed for half of their max HP.")
            print("This does not include status effects, however.")
            firstTimeAround = False
        time.sleep(3)
        player_pokedex.healPokemon()
        time.sleep(2)
    print("All of your pokemon have fainted, thats the end of the game. GG")

if __name__ == "__main__":
    main()
