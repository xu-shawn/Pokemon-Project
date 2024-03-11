from random import uniform, randint

def numberToBar(val, maxi, leng):
    return "[" + "█" * int((val / maxi) * leng) + "░" * (leng - int((val / maxi) * leng)) + "]"

class StatusEffect:
    def __init__(self, effect, duration=2):
        self.effect = effect  # A function object
        self.duration = duration

    def Run(self, target):
        self.duration -= 1
        self.effect(target)
        if self.duration <= 0:
            return True
        return False


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
        return self.experience ** (1 / 3)

    def fight(self, other: "Pokemon"):
        pass

    def calculate_damage(self, ttype: int, power: int):
        modifier: float = (
            uniform(0.85, 1) * ttype * (1 + (randint(0, 511) < self.speed))
        )
        return (2 * self.level / 5 + 2) * power * self.attack / self.defense

    def Damage(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            pass # lol idk
    def __str__(self):
        return f"{self.name} - {numberToBar(self.health, self.maxHealth, 10)} {self.health}/{self.maxHealth}"

    def Heal(self, amt):
        self.health = max(self.health + amt, self.maxHealth)
        # Update status message in UI

    def TickStatusEffects(self):
        # Run every function in the Status Effects list on self
        for effect in self.statusEffects:
            if effect.Run(self):
                self.statusEffects.remove(effect)

    def addStatus(self, status):
        self.statusEffects.append(status)
