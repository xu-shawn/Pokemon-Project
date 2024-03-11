from random import uniform, randint
class TextModifiers: # Stores ANSI escape sequences that change the text but its actually readable
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"
TM = TextModifiers # Alias
def numberToBar(val, maxi, leng):
    if val / maxi < 0.3:
        d = TM.LIGHT_RED
    elif val / maxi < 0.6:
        d = TM.YELLOW
    else:
        d = TM.GREEN
    return d + "[" + "█" * int((val / maxi) * leng) + "░" * (leng - int((val / maxi) * leng)) + "]"

class StatusEffect:
    def __init__(self, effect, finish, duration=2):
        self.effect = effect  # A function object
        self.duration = duration
        self.initialDuration = duration
        self.finish = finish
    def Run(self, target):
        if self.duration == self.initialDuration:
            self.targetInitStats = target.getStats()
        self.duration -= 1
        self.effect(target)
        if self.duration <= 0:
            self.EndStatus(self, target)
            return True
        return False
    def EndStatus(self, target):
        self.finish(target, self.targetInitStats) # WARNING: THIS WILL GO BAD IF MULTIPLE EFFECTS CHANGE THE SAME STATS

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

        self.description = description
        self.statusEffects = statuseffects  # A list of functions to run every turn

    @property
    def level(self):
        return int(self.experience ** (1 / 3))
    def getStats(self):
        '''
        Gets stats as a dictionary
        '''
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
            "Status Effects": self.statusEffects
            # Add other stats as needed
        }
    def fight(self, other: "Pokemon"):
        pass

    def calculate_damage(self, ttype: int, power: int):
        '''
        calculate_damage(ttype, power)
        '''
        modifier: float = (
            uniform(0.85, 1) * ttype * (1 + (randint(0, 511) < self.speed))
        )
        return (2 * self.level / 5 + 2) * power * self.attack / self.defense

    def Damage(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            pass # lol idk
    def __str__(self):
        return f"{self.name} - {numberToBar(self.health, self.maxHealth, 10)} {self.health}/{self.maxHealth}{TM.END}"

    def Heal(self, amt):
        '''
        Heal(amt)
        Heals the pokemon for the specified amount of health, up to a max of its maxHealth.
        '''
        self.health = max(self.health + amt, self.maxHealth)
        # Update status message in UI

    def TickStatusEffects(self):
        '''
        TickStatusEffects()
        Runs the function specified in every status effect 
        currently attached to the pokemon, and removes them from the list
        if its duration has passed.
        '''
        # Run every function in the Status Effects list on self
        for effect in self.statusEffects:
            if effect.Run(self):
                self.statusEffects.remove(effect)

    def addStatus(self, status):
        '''
        addStatus(status)
        Adds the specified status to the pokemon
        '''
        self.statusEffects.append(status)
