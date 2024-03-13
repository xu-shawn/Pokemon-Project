from random import uniform, randint
from moves import *


def numberToBar(val, maxi, leng):
    if val / maxi < 0.3:
        d = TM.LIGHT_RED
    elif val / maxi < 0.6:
        d = TM.YELLOW
    else:
        d = TM.GREEN
    return (
        d
        + "["
        + "█" * int((val / maxi) * leng)
        + "░" * (leng - int((val / maxi) * leng))
        + "]"
    )


class Pokemon:
    def __init__(
        self,
        name: str,
        ttype: list,
        health: int,
        moves: list,
        attack: int,
        defense: int,
        speed: int,
        experience: int,
        description: str,
        statuseffects: list,
    ):
        self.name = name
        self.type = ttype  # Not using "type" because its a keyword
        self.health = health
        self.maxHealth = health
        self.moves = moves
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.experience = experience
        self.statModifiers = (
            {}
        )  # Temporary modifications made to stats by status effects, a dict of dicts
        self.description = description
        self.statusEffects = statuseffects  # A list of functions to run every turn

    @property
    def level(self):
        return int(self.experience ** (1 / 3))

    def getStats(self):
        """
        Gets stats as a dictionary
        """
        return {
            "Name": self.name,
            "Type": self.type,
            "Health": self.health,
            "Max Health": self.maxHealth,
            "Moves": self.moves,
            "Attack": self.attack,
            "Defense": self.defense,
            "Speed": self.speed,
            "Experience": self.experience,
            "Level": self.level,
            "Description": self.description,
            "Status Effects": self.statusEffects,
        }

    def TakeDamage(self, dmg):
        """
        Damages the pokemon for the specified amount.
        DOES NOT do the calculation, and DOES NOT check for faints.
        """
        self.health -= dmg
        self.health = max(self.health, 0)
        MainUI.addMessage(f"{self.name} took {dmg} damage!")

    def __str__(self):
        return (
            f"{self.name} - {numberToBar(self.health, self.maxHealth, 20)} {self.health}/{self.maxHealth}{TM.END}"
            + " ".join([str(x) for x in self.statusEffects])
        )

    def Heal(self, amt):
        """
        Heal(amt)
        Heals the pokemon for the specified amount of health, up to a max of its maxHealth.
        """
        self.health = max(self.health + amt, self.maxHealth)
        MainUI.addMessage(f"{TM.GREEN}{self.name} heals for {amt} health!{TM.END}")

    def TickStatusEffects(self):
        """
        TickStatusEffects()
        Runs the function specified in every status effect
        currently attached to the pokemon, and removes them from the list
        if its duration has passed.
        """
        # Run every function in the Status Effects list on self
        for effect in self.statusEffects:
            if effect.Run(self):  # Run returns true if the effect expires.
                self.statusEffects.remove(effect)
                print(effect)

    def addStatus(self, status):
        """
        addStatus(status)
        Adds the specified status to the pokemon
        and runs the specified startup
        """
        self.statusEffects.append(status)
        status.StartRunning(self)

    def checkForStatus(self, statusName):
        for stat in self.statusEffects:
            if stat.name == statusName:
                return True
        return False

    def useMove(self, moveName, target):
        """
        Use the specified move on the target pokemon.
        """
        move = MOVES_DICTIONARY.get(moveName, None)
        if not move:
            raise ValueError("Move not found! How did this happen?")
        move(self, target)
