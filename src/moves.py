from UIObject import TM, MainUI
from random import uniform, randint
from copy import deepcopy
from typing import Callable
MU = MainUI  # Alias so that E501 will stop SCREAMING AT A LINE THATS TOO LONG


class StatusEffect:
    def __init__(
        self,
        name: str,
        start: Callable,
        effect: Callable,
        finish: Callable,
        duration: int = 2,
        color: str = "",
    ):
        self.name = name
        self.startup = start
        self.effect = effect  # A function object
        self.duration = duration
        self.initialDuration = duration
        self.color = color
        self.finish = finish

    def StartRunning(self, target):
        target.statModifiers[self.name] = {
            "Health": 0,
            "Max Health": 0,
            "Attack": 0,
            "Defense": 0,
            "Speed": 0,
            # Add other stats as needed
        }
        MainUI.addMessage(f"{target.name} is {self.color}{self.name.upper()}{TM.END}!")
        self.startup(target)

    def Run(self, target):
        self.duration -= 1
        self.effect(target)
        if self.duration <= 0:
            self.EndStatus(target)
            return True
        return False

    def EndStatus(self, target):
        self.finish(target)
        # Hopefully, removing the status from the list
        # will cause Python to recognize the status
        # as unused and remove it. If not, uh,
        # memory leaks!
        # del target.statModifiers[self.name]

    def __str__(self):
        return f"{self.color}[{self.duration} {self.name}]{TM.END} "


def simpleDmgMove(me, other, power=0, effective=[], noteffective=[]):

    effectiveness: int = 1
    for p in other.type:
        if p in effective:
            effectiveness *= 2
            MainUI.addMessage(f"It's super effective! ({p})")
        elif p in noteffective:
            effectiveness *= 0.5
            MainUI.addMessage(f"It's not very effective... ({p})")

    modifier: float = (
        uniform(0.85, 1) * effectiveness * (1 + (randint(0, 511) < me.speed))
    )
    MainUI.addMessage(f"Damage Modifier: x{modifier:.3f}")
    amount = int(
            (
                (
                    (2 * me.level / 5 + 2)
                    * power * me.attack / other.defense)
                / 50 + 2)
            * modifier
        )
    other.TakeDamage(amount)

    MainUI.addMessage(f"{other.name} took {amount} damage!")
def lifeSteal(me, other, power=0, effective=[], noteffective=[]):
    
    effectiveness: int = 1
    for p in other.type:
        if p in effective:
            effectiveness *= 2
            MainUI.addMessage(f"It's super effective! ({p})")
        elif p in noteffective:
            effectiveness *= 0.5
            MainUI.addMessage(f"It's not very effective... ({p})")

    modifier: float = (
        uniform(0.85, 1) * effectiveness * (1 + (randint(0, 511) < me.speed))
    )
    MainUI.addMessage(f"Damage Modifier: x{modifier:.3f}")
    amount = int(
            (
                (
                    (2 * me.level / 5 + 2)
                    * power * me.attack / other.defense)
                / 50 + 2)
            * modifier
        )
    other.TakeDamage(amount)
    me.Heal(amount)

    MainUI.addMessage(f"{other.name} took {amount} damage!")


def NullFunction(*anything):
    """
    A placeholder that does nothing to make the code easier to read.
    """
    return None


def tickFire(self):
    self.TakeDamage(2)
    MU.addMessage(
        f"{TM.LIGHT_RED}{self.name} took 2 points of FIRE damage!{TM.END}"
    )


def tickPoison(self):
    self.TakeDamage(3)
    MU.addMessage(
        f"{TM.LIGHT_PURPLE}{self.name} took 3 points of POISON damage!{TM.END}"
    )


def tickWeaken(self):
    self.attack -= 2
    self.defense -= 2
    self.statModifiers["Weakened"]["Attack"] += 2
    self.statModifiers["Weakened"]["Defense"] += 2
    MU.addMessage(f"{TM.LIGHT_GRAY}{self.name} was weakened...{TM.END}")


def endWeaken(self):
    self.attack += self.statModifiers["Weakened"]["Attack"]
    self.defense += self.statModifiers["Weakened"]["Defense"]
    MU.addMessage(f"{TM.LIGHT_GRAY}{self.name} is back "
                  + f"to full strength!{TM.END}")


def startFrozen(self):
    self.statModifiers["Frozen"]["Speed"] = self.speed
    self.speed = 0
    # Maybe make moves fail with probability
    # if speed is much lower than enemy speed


def endFrozen(self):
    self.speed += self.statModifiers["Frozen"]["Speed"]
    MU.addMessage(f"{TM.LIGHT_CYAN}{self.name} has thawed out.{TM.END}")


statusEffectDictionary = {
    "Burning": StatusEffect(
        "Burning", NullFunction, tickFire, NullFunction, 3, TM.LIGHT_RED
    ),
    "Frozen": StatusEffect(
        "Frozen", startFrozen, NullFunction, endFrozen, 2, TM.LIGHT_CYAN
    ),
    "Poisoned": StatusEffect(
        "Poisoned", NullFunction, tickPoison, NullFunction, 3, TM.LIGHT_PURPLE
    ),
    "Weakened": StatusEffect(
        "Weakened", NullFunction, tickWeaken, endWeaken, 5, TM.LIGHT_GRAY
    ),
}


def inflictEverything(self, other, power=0, effective=[], noteffective=[]):
    inflictStatusEffectMove(
        self,
        other,
        power,
        effective,
        noteffective,
        ["Burning", "Frozen", "Poisoned", "Weakened"],
        [100, 100, 100, 100],
    )


def inflictStatusEffectMove(
    self, other, power=0,
    effective=[], noteffective=[],
    effects=[], probability=[0]
):
    simpleDmgMove(self, other, power, effective, noteffective)
    index = 0
    for effect in effects:
        if randint(1, 100) < probability[index]:
            if not other.checkForStatus(
                effect
            ):  # Do not give the pokemon the same effect multiple times.
                # However, do reset the timer.
                other.addStatus(
                    deepcopy(statusEffectDictionary[effect])
                )  # TODO: Reset the timer
        index += 1


MOVES_DICTIONARY = {
    "Scratch": lambda me, other: simpleDmgMove(me, other,
                                               40, [], ["Rock", "Steel"]),
    "Tackle": lambda me, other: simpleDmgMove(me, other,
                                              40, [], ["Rock", "Steel"]),
    "Pound": lambda me, other: simpleDmgMove(me, other,
                                             40, [], ["Rock", "Steel"]),
    "Rage": lambda me, other: simpleDmgMove(me, other,
                                            20, [], ["Rock", "Steel"]),
    "Fury Attack": lambda me, other: simpleDmgMove(
        me, other, 15, [], ["Rock", "Steel"]
    ),
    "Ember": lambda me, other: inflictStatusEffectMove(
        me,
        other,
        40,
        ["Grass", "Ice", "Bug", "Steel"],
        ["Fire", "Water", "Rock", "Dragon"],
        ["Burning"],
        [20],
    ),
    "Fire Spin": lambda me, other: inflictStatusEffectMove(
        me,
        other,
        35,
        ["Grass", "Ice", "Bug", "Steel"],
        ["Fire", "Water", "Rock", "Dragon"],
        ["Burning"],
        [60],
    ),
    "Bubble": lambda me, other: simpleDmgMove(
        me, other,
        40,
        ["Fire", "Ground", "Rock"],
        ["Water", "Grass", "Dragon"]
    ),
    "Aqua Jet": lambda me, other: simpleDmgMove(
        me, other, 40,
        ["Fire", "Ground", "Rock"],
        ["Water", "Grass", "Dragon"]
    ),
    "Thunder Shock": lambda me, other: simpleDmgMove(
        me, other, 40,
        ["Water", "Flying"],
        ["Electric", "Grass", "Dragon"]
    ),
    "Thunderbolt": lambda me, other: simpleDmgMove(
        me, other, 90,
        ["Water", "Flying"],
        ["Electric", "Grass", "Dragon"]
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
        ["Frozen"],
        [10],
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
        me, other, 60,
        ["Grass", "Fighting", "Bug"], ["Electric", "Rock", "Steel"]
    ),
    "Peck": lambda me, other: simpleDmgMove(
        me, other, 35,
        ["Grass", "Fighting", "Bug"], ["Electric", "Rock", "Steel"]
    ),
    "Confusion": lambda me, other: inflictStatusEffectMove(
        me, other, 50,
        ["Fighting", "Poison"], ["Psychic", "Steel"],
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
        me, other, 50,
        ["Fire", "Ice", "Flying", "Bug"],
        ["Fighting", "Ground", "Steel"]
    ),
    "Rock Slide": lambda me, other: simpleDmgMove(
        me, other, 75,
        ["Fire", "Ice", "Flying", "Bug"],
        ["Fighting", "Ground", "Steel"]
    ),
    "Lick": lambda me, other: inflictStatusEffectMove(
        me, other, 30, ["Psychic", "Ghost"], ["Dark"], ["Weakened"], [50]
    ),
    "Outrage": lambda me, other: simpleDmgMove(me, other, 120,
                                               ["Dragon"],
                                               ["Steel"]),
    "Crunch": lambda me, other: simpleDmgMove(
        me, other, 80, ["Psychic", "Ghost"], ["Fighting", "Dark", "Fairy"]
    ),
    "Bite": lambda me, other: simpleDmgMove(
        me, other, 60, ["Psychic", "Ghost"], ["Fighting", "Dark", "Fairy"]
    ),
    "Flash Cannon": lambda me, other: simpleDmgMove(
        me, other,
        80,
        ["Ice", "Rock", "Fairy"],
        ["Fire", "Water", "Electric", "Steel"]
    ),
    "Smog": lambda me, other: inflictStatusEffectMove(
        me,
        other,
        30,
        ["Grass", "Fairy"],
        ["Poison", "Ground", "Rock", "Ghost"],
        ["Poisoned"],
        [70],
    ),
    "Dream Eater": lambda me, other: simpleDmgMove(
        me, other, 100, ["Fighting", "Poison"], ["Psychic", "Steel"]
    ),
    "Body Slam": lambda me, other: simpleDmgMove(me, other,
                                                 85, [], ["Rock", "Steel"]),
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
    "Headbutt": lambda me, other: simpleDmgMove(me, other,
                                                70,
                                                [],
                                                ["Rock", "Steel"]),
    "Absorb": lambda me, other: lifeSteal(
        me,
        other,
        20,
        ["Water", "Ground", "Rock"],
        ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
    ),
    "Fairy Wind": lambda me, other: simpleDmgMove(
        me, other,
        40,
        ["Fighting", "Dragon", "Dark"],
        ["Fire", "Poison", "Steel"]
    ),
    "Struggle Bug": lambda me, other: simpleDmgMove(
        me,
        other,
        50,
        ["Grass", "Psychic", "Dark"],
        ["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel", "Fairy"],
    ),
    "Draining Kiss": lambda me, other: lifeSteal(
        me, other, 50,
        ["Fighting", "Dragon", "Dark"],
        ["Fire", "Poison", "Steel"]
    ),
    "Shadow Ball": lambda me, other: simpleDmgMove(
        me, other, 80, ["Psychic", "Ghost"], ["Dark"]
    ),
    "Spread Covid": lambda me, other: inflictEverything(
        me, other, 1, [], []
    ),  # This is a test move because lmao ha ha
    "P A I N": lambda me, other: simpleDmgMove(
        me, other, 100000, [], []
    )
}
