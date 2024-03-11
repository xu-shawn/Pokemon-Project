def display_welcome():
    print("Welcome to the Pokémon Adventure!")
    print("In this game, you will choose a starter Pokémon to battle against wild Pokémon.")
    print("You can capture Pokémon by defeating them in battles.")
    print("Let's start by choosing your first Pokémon!")

def choose_starter():
    starters = ['Bulbasaur', 'Charmander', 'Squirtle']
    print("Please choose your starter Pokémon:")
    for starter in starters:
        print(f"- {starter}")
    
    choice = input("Your choice: ").capitalize()
    while choice not in starters:
        print("That's not a valid Pokémon. Please choose Bulbasaur, Charmander, or Squirtle.")
        choice = input("Your choice: ").capitalize()
    
    print(f"Great choice! You chose {choice}.")
    return choice

def display_battle_instructions():
    print("Now that you have your Pokémon, you're ready to battle.")
    print("During a battle, you can choose a move for your Pokémon to use.")
    print("Each move has different effects, so choose wisely.")
    print("Type the name of the move to use it.")

def choose_move(moves):
    print("Choose a move:")
    for move in moves:
        print(f"- {move}")
    
    move = input("Your move: ").capitalize()
    while move not in moves:
        print("That's not a valid move. Please choose again.")
        move = input("Your move: ").capitalize()
    
    return move

def main():
    display_welcome()
    starter_name = choose_starter()
    display_battle_instructions()

if __name__ == "__main__":
    main()