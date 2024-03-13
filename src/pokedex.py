class Pokedex:
    def __init__(self):
        self.collection = {}
        self.active_pokemon = None
    @property
    def defeated(self):
        '''
        Returns true if all pokemon in the pokedex are fainted.
        '''
        for pokemon in self.collection:
            if self.collection[pokemon].health > 0:
                return False
        return True
    @property
    def livingPokemon(self):
        '''
        Returns the exact number of non-fainted pokemon.
        '''
        count = 0
        for pokemon in self.collection:
            if self.collection[pokemon].health > 0:
                count += 1
        return count
    def fainted(self):
        '''
        Replaces the fainted pokemon in the active slot with another, and returns False if it cannot.
        '''
        for pokemon in self.collection:
            if self.collection[pokemon].health > 0:
                self.active_pokemon = self.collection[pokemon]
                return True
        return False
    def add_pokemon(self, pokemon):
        """
        Adds a Pokémon to the Pokédex.
        """
        if pokemon.name not in self.collection:
            self.collection[pokemon.name] = pokemon
            print(f"{pokemon.name} has been added to your Pokédex!")
        else:
            print(f"{pokemon.name} is already in your Pokédex.")
        if self.active_pokemon is None:
            self.active_pokemon = pokemon
        else:
            b = input(f"Would you like to make {pokemon.name}" +
                      " your active pokemon (first into battle)? (yes/no): ")
            while b.lower() not in ['no', 'yes']:
                b = input("That's not yes or no."
                          + f"Make {pokemon.name}"
                          + "the active pokemon? (yes/no) ")
            if b.lower() == 'yes':
                self.active_pokemon = pokemon
                print(f"{pokemon.name} is now your main pokemon.")

    def remove_pokemon(self, name):
        """
        Removes a Pokémon from the Pokédex by name.
        """
        if name in self.collection:
            del self.collection[name]
            print(f"{name} has been removed from your Pokédex.")
        else:
            print(f"{name} is not in your Pokédex.")
    def healPokemon(self):
        for pokemon in self.collection:
            self.collection[pokemon].Heal(self.collection[pokemon].maxHealth // 2)
        print("Pokemon healed!")
    def get_pokemon(self, name):
        """
        Retrieves a Pokémon from the Pokédex by name.
        """
        return self.collection.get(name, None)

    def list_pokemon(self):
        """
        Lists all Pokémon in the Pokédex.
        """
        if self.collection:
            print("Pokédex:")
            for name in self.collection:
                print(name)
        else:
            print("Your Pokédex is empty.")
