from UIObject import *
from random import uniform, randint


class StatusEffect:
    def __init__(self, name, start, effect, finish, duration=2, color=""):
        self.name = name
        self.startup = start
        self.effect = effect  # A function object
        self.duration = duration
        self.initialDuration = duration
        self.color = color
        self.finish = finish

    def StartRunning(self, target):
        self.startup(target)

    def Run(self, target):
        if self.duration == self.initialDuration:
            target.statModifiers[self.name] = {
                "Health": 0,
                "Max Health": 0,
                "Attack": 0,
                "Defense": 0,
                "Speed": 0,
                # Add other stats as needed
            }
        self.duration -= 1
        self.effect(target)
        if self.duration <= 0:
            self.EndStatus(self, target)
            return True
        return False

    def EndStatus(self, target):
        self.finish(
            target, self.targetInitStats
        )  # WARNING: THIS WILL GO BAD IF MULTIPLE EFFECTS CHANGE THE SAME STATS

    def __str__(self):
        return f"{self.color}[{self.duration} {self.name}]{TM.END} "


def simpleDmgMove(me, other, power=0, effective=[], noteffective=[]):

    effectiveness: int = 1

    if other.type in effective:
        effectiveness = 2
    elif other.type in noteffective:
        effectiveness = 0.5

    modifier: float = (
        uniform(0.85, 1) * effectiveness * (1 + (randint(0, 511) < me.speed))
    )

    other.TakeDamage(int((((2 * me.level / 5 + 2) * power * me.attack / other.defense) / 50 + 2) * modifier))

    # Add to UI


def NullFunction(self):
    """
    A placeholder that does nothing to make the code easier to read.
    """
    return None


def tickFire(self):
    self.TakeDamage(10)
    MainUI.addMessage(
        f"{TM.LIGHT_RED}{self.name} took 10 points of FIRE damage!{TM.END}"
    )


def tickPoison(self):
    self.TakeDamage(10)
    MainUI.addMessage(
        f"{TM.LIGHT_PURPLE}{self.name} took 10 points of POISON damage!{TM.END}"
    )


def tickWeaken(self):
    self.attack -= 2
    self.defence -= 2
    self.statModifiers["Weaken"]["Attack"] += 2
    self.statModifiers["Weaken"]["Defence"] += 2
    MainUI.addMessage(f"{TM.LIGHT_GRAY}{self.name} was weakened...{TM.END}")


def endWeaken(self):
    self.attack += self.statModifiers["Weaken"]["Attack"]
    self.defence += self.statModifiers["Weaken"]["Defence"]
    MainUI.addMessage(f"{TM.LIGHT_GRAY}{self.name} is back to full strength!{TM.END}")
    self.statModifiers.remove("Weaken")


def startFrozen(self):
    self.statModifiers["Frozen"]["Speed"] = self.speed
    self.speed = 0  # Maybe make moves fail with probability if speed is much lower than enemy speed
    MainUI.addMessage(f"{TM.LIGHT_CYAN}{self.name} is FROZEN!{TM.END}")


def endFrozen(self):
    self.speed += self.statModifiers["Frozen"]["Speed"]
    self.statModifiers.remove("Frozen")
    MainUI.addMessage(f"{TM.LIGHT_CYAN}{self.name} has thawed out.{TM.END}")

statusEffectDictionary = {"Burning":StatusEffect(
    "Burning", NullFunction, tickFire, NullFunction, 3, TM.LIGHT_RED
),
"Frozen": StatusEffect(
    "Frozen", startFrozen, NullFunction, endFrozen, 2, TM.LIGHT_CYAN
),

"Poisoned": StatusEffect(
    "Poisoned", NullFunction, tickPoison, NullFunction, 3, TM.LIGHT_PURPLE
),

"Weakened": StatusEffect(
    "Weakened", NullFunction, tickWeaken, endWeaken, 3, TM.LIGHT_GRAY
)

}
def inflictEverything(self, other, power=0, effective=[], noteffective=[]):
    inflictStatusEffectMove(
        self,
        other,
        power,
        effective,
        noteffective,
        ["Burning", "Frozen", "Poisoned", "Weakened"],
        100
    )


def inflictStatusEffectMove(
    self, other, power=0, effective=[], noteffective=[], effects=[], probability=[0]
):
    simpleDmgMove(self, other, power, effective, noteffective)
    index = 0
    for effect in effects:
        if randint(1, 100) < probability[index]:
            if not other.checkForStatus(
                effect
            ):  # Do not give the pokemon the same effect multiple times. However, do reset the timer.
                other.addStatus(statusEffectDictionary[effect].deepcopy())  # TODO: Reset the timer
                other.statusEffects.get()
        index += 1


MOVES_DICTIONARY = {
    "Scratch": lambda me, other: simpleDmgMove(me, other, 40, [], ["Rock", "Steel"]),
    "Tackle": lambda me, other: simpleDmgMove(me, other, 40, [], ["Rock", "Steel"]),
    "Pound": lambda me, other: simpleDmgMove(me, other, 40, [], ["Rock", "Steel"]),
    "Rage": lambda me, other: simpleDmgMove(me, other, 20, [], ["Rock", "Steel"]),
    "Fury Attack": lambda me, other: simpleDmgMove(
        me, other, 15, [], ["Rock", "Steel"]
    ),
    "Ember": lambda me, other: inflictStatusEffectMove(
        me,
        other,
        40,
        ["Grass", "Ice", "Bug", "Steel"],
        ["Fire", "Water", "Rock", "Dragon"],
        ["Burning"], [20]
    ),
    "Fire Spin": lambda me, other: inflictStatusEffectMove(
        me,
        other,
        35,
        ["Grass", "Ice", "Bug", "Steel"],
        ["Fire", "Water", "Rock", "Dragon"],
        ["Burning"], [40]
    ),
    "Bubble": lambda me, other: simpleDmgMove(
        me, other, 40, ["Fire", "Ground", "Rock"], ["Water", "Grass", "Dragon"]
    ),
    "Aqua Jet": lambda me, other: simpleDmgMove(
        me, other, 40, ["Fire", "Ground", "Rock"], ["Water", "Grass", "Dragon"]
    ),
    "Thunder Shock": lambda me, other: simpleDmgMove(
        me, other, 40, ["Water", "Flying"], ["Electric", "Grass", "Dragon"]
    ),
    "Thunderbolt": lambda me, other: simpleDmgMove(
        me, other, 90, ["Water", "Flying"], ["Electric", "Grass", "Dragon"]
    ),
    "Vine Whip": lambda me, other: simpleDmgMove(
        me,
        other,
        45,
        ["Water", "Ground", "Rock"],
        ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
    ),
    "Magical Leaf": lambda me, other: simpleDmgMove(
        me,
        other,
        60,
        ["Water", "Ground", "Rock"],
        ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
    ),
    "Ice Shard": lambda me, other: inflictStatusEffectMove(
        me,
        other,
        40,
        ["Grass", "Ground", "Flying", "Dragon"],
        ["Fire", "Water", "Ice", "Steel"],
        ["Frozen"],[10]
    ),
    "Double Kick": lambda me, other: simpleDmgMove(
        me,
        other,
        60,
        ["Normal", "Ice", "Rock", "Dark", "Steel"],
        ["Poison", "Flying", "Psychic", "Bug", "Fairy"],
    ),
    "Earthquake": lambda me, other: simpleDmgMove(
        me,
        other,
        100,
        ["Fire", "Electric", "Poison", "Rock", "Steel"],
        ["Grass", "Bug"],
    ),
    "Wing Attack": lambda me, other: simpleDmgMove(
        me, other, 60, ["Grass", "Fighting", "Bug"], ["Electric", "Rock", "Steel"]
    ),
    "Peck": lambda me, other: simpleDmgMove(
        me, other, 35, ["Grass", "Fighting", "Bug"], ["Electric", "Rock", "Steel"]
    ),
    "Confusion": lambda me, other: inflictStatusEffectMove(
        me, other, 50, ["Fighting", "Poison"], ["Psychic", "Steel"]
        ["Weakened"], [100]
    ),
    "Twineedle": lambda me, other: simpleDmgMove(
        me,
        other,
        25,
        ["Grass", "Psychic", "Dark"],
        ["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel", "Fairy"],
    ),
    "Rock Throw": lambda me, other: simpleDmgMove(
        me, other, 50, ["Fire", "Ice", "Flying", "Bug"], ["Fighting", "Ground", "Steel"]
    ),
    "Rock Slide": lambda me, other: simpleDmgMove(
        me, other, 75, ["Fire", "Ice", "Flying", "Bug"], ["Fighting", "Ground", "Steel"]
    ),
    "Lick": lambda me, other: inflictStatusEffectMove(
        me, other, 30, ["Psychic", "Ghost"], ["Dark"],
        ["Weakened"], [50]
    ),
    "Outrage": lambda me, other: simpleDmgMove(me, other, 120, ["Dragon"], ["Steel"]),
    "Crunch": lambda me, other: simpleDmgMove(
        me, other, 80, ["Psychic", "Ghost"], ["Fighting", "Dark", "Fairy"]
    ),
    "Bite": lambda me, other: simpleDmgMove(
        me, other, 60, ["Psychic", "Ghost"], ["Fighting", "Dark", "Fairy"]
    ),
    "Flash Cannon": lambda me, other: simpleDmgMove(
        me, other, 80, ["Ice", "Rock", "Fairy"], ["Fire", "Water", "Electric", "Steel"]
    ),
    "Smog": lambda me, other: inflictStatusEffectMove(
        me, other, 30, ["Grass", "Fairy"], ["Poison", "Ground", "Rock", "Ghost"],
        ["Poisoned"], [50]
    ),
    "Dream Eater": lambda me, other: simpleDmgMove(
        me, other, 100, ["Fighting", "Poison"], ["Psychic", "Steel"]
    ),
    "Body Slam": lambda me, other: simpleDmgMove(me, other, 85, [], ["Rock", "Steel"]),
    "Double Slap": lambda me, other: simpleDmgMove(
        me, other, 15, [], ["Rock", "Steel"]
    ),
    "Razor Leaf": lambda me, other: simpleDmgMove(
        me,
        other,
        55,
        ["Water", "Ground", "Rock"],
        ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
    ),
    "Headbutt": lambda me, other: simpleDmgMove(me, other, 70, [], ["Rock", "Steel"]),
    "Absorb": lambda me, other: simpleDmgMove(
        me,
        other,
        20,
        ["Water", "Ground", "Rock"],
        ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
    ),
    "Fairy Wind": lambda me, other: simpleDmgMove(
        me, other, 40, ["Fighting", "Dragon", "Dark"], ["Fire", "Poison", "Steel"]
    ),
    "Struggle Bug": lambda me, other: simpleDmgMove(
        me,
        other,
        50,
        ["Grass", "Psychic", "Dark"],
        ["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel", "Fairy"],
    ),
    "Draining Kiss": lambda me, other: simpleDmgMove(
        me, other, 50, ["Fighting", "Dragon", "Dark"], ["Fire", "Poison", "Steel"]
    ),
    "Shadow Ball": lambda me, other: simpleDmgMove(
        me, other, 80, ["Psychic", "Ghost"], ["Dark"]
    ),
    "Spread Covid": lambda me, other: inflictEverything(
        me, other, 0, [], []
    ),  # This is a test move because lmao ha ha
}
