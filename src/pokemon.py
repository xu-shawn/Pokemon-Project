from moves import TM, MOVES_DICTIONARY
from UIObject import MainUI, time


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
        statuseffects: list = [],
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
        # Temporary modifications made to stats by status effects
        self.statModifiers = (
            {}
        )
        self.description = description
        # A list of functions to run every turn
        self.statusEffects = statuseffects

    @property
    def level(self):
        return int(self.experience ** (1 / 3))
    def gainEXP(self, amt):
        prevLevel = self.level
        self.experience += amt
        if self.level > prevLevel:
            # Flat stat increases per level:
            # 5 HP
            # 5 Power
            # 5 Defence
            # 1 Speed
            print(f"{self.name} gained {self.level - prevLevel} level(s)!")
            self.maxHealth += 5 * (self.level - prevLevel)
            self.attack += 5 * (self.level - prevLevel)
            self.defense += 5 * (self.level - prevLevel)
            self.speed += 1 * (self.level - prevLevel)
            time.sleep(3)
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

    def __str__(self):
        return (
            f"[{self.type[0]}] Lv.{self.level} {self.name} - "
            + f"{numberToBar(self.health, self.maxHealth, 20)}"
            + f" {self.health}/{self.maxHealth}{TM.END} "
            + " ".join([str(x) for x in self.statusEffects])
        )

    def Heal(self, amt):
        """
        Heal(amt)
        Heals the pokemon for the specified amount of health,
        up to a max of its maxHealth.
        """
        self.health = min(self.health + amt, self.maxHealth)
        MainUI.addMessage(f"{TM.GREEN}{self.name} heals for {amt} health!{TM.END}")

    def TickStatusEffects(self):
        """
        TickStatusEffects()
        Runs the function specified in every status effect
        currently attached to the pokemon, and removes them from the list
        if its duration has passed.
        """
        # Run every function in the Status Effects list on self
        # This should ensure that even if elements are removed
        # during iteration, all status effects are triggered.
        for status in self.statusEffects:
            status.Run(self)
        self.statusEffects = [x for x in self.statusEffects if not x.duration <= 0]

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
