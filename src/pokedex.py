class Pokedex:
    def __init__(self):
        self.collection = {}

    def add_pokemon(self, pokemon):
        """
        Adds a Pokémon to the Pokédex.
        """
        if pokemon.name not in self.collection:
            self.collection[pokemon.name] = pokemon
            print(f"{pokemon.name} has been added to your Pokédex!")
        else:
            print(f"{pokemon.name} is already in your Pokédex.")

    def remove_pokemon(self, name):
        """
        Removes a Pokémon from the Pokédex by name.
        """
        if name in self.collection:
            del self.collection[name]
            print(f"{name} has been removed from your Pokédex.")
        else:
            print(f"{name} is not in your Pokédex.")

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