from pokemon import *


def simpleDmgMove(me, other, power=0, effective=[], noteffective=[]):

    effectiveness: int = 1

    if other.type in effective:
        effectiveness = 2
    elif other.type in noteffective:
        effectiveness = 0.5

    modifier: float = (
        uniform(0.85, 1) * effectiveness * (1 + (randint(0, 511) < me.speed))
    )

    other.Damage((2 * me.level / 5 + 2) * power * me.attack / me.defense)

    # Add to UI
def NullFunction(self):
    '''
    A placeholder that does nothing to make the code easier to read.
    '''
    return None

def tickFire(self):
    self.Damage(10)
    # Add to UI

def tickPoison(self):
    self.Damage(10)
    # Add to UI

def tickWeaken(self):
    self.attack -= 2
    self.defence -= 2
    self.statModifiers["Weaken"]["Attack"] += 2
    self.statModifiers["Weaken"]["Defence"] += 2

def endWeaken(self):
    self.attack += self.statModifiers["Weaken"]["Attack"]
    self.defence += self.statModifiers["Weaken"]["Defence"]
    self.statModifiers.remove("Weaken")

def startFrozen(self):
    self.statModifiers["Frozen"]["Speed"] = self.speed
    self.speed = 0 # Maybe make moves fail with probability if speed is much lower than enemy speed

def endFrozen(self):
    self.speed += self.statModifiers["Frozen"]["Speed"]
    self.statModifiers.remove("Frozen")

statusFire = StatusEffect("Burning", NullFunction, tickFire, NullFunction, TM.LIGHT_RED)
statusFrozen = StatusEffect("Frozen", startFrozen, NullFunction, endFrozen, TM.LIGHT_CYAN)
statusPoison = StatusEffect("Poisoned", NullFunction, tickPoison, NullFunction, TM.LIGHT_PURPLE)
statusWeaken = StatusEffect("Weakened", NullFunction, tickWeaken, endWeaken, TM.LIGHT_GRAY)

def inflictEverything(self, other, power=0, effective=[], noteffective=[]):
    inflictStatusEffectMove(self, other, power, effective, noteffective, ["Burning", "Frozen", "Poisoned", "Weakened"])
def inflictStatusEffectMove(self, other, power=0, effective=[], noteffective=[], effects=[]):
    simpleDmgMove(self, other, power, effective, noteffective)
    for effect in effects:
        if not other.checkForStatus(effect): # Do not give the pokemon the same effect multiple times. However, do reset the timer.
            other.addStatus(statusFire.deepcopy()) # TODO: Reset the timer
            other.statusEffects.get()
MOVES_DICTIONARY = {
    "Scratch": lambda me, other: simpleDmgMove(
        me, other, 40, [], ["Rock", "Steel"]
    ),
    "Tackle": lambda me, other: simpleDmgMove(
        me, other, 40, [], ["Rock", "Steel"]
    ),
    "Pound": lambda me, other: simpleDmgMove(me, other, 40, [], ["Rock", "Steel"]),
    "Rage": lambda me, other: simpleDmgMove(me, other, 20, [], ["Rock", "Steel"]),
    "Fury Attack": lambda me, other: simpleDmgMove(
        me, other, 15, [], ["Rock", "Steel"]
    ),
    "Ember": lambda me, other: simpleDmgMove(
        me,
        other,
        40,
        ["Grass", "Ice", "Bug", "Steel"],
        ["Fire", "Water", "Rock", "Dragon"],
    ),
    "Fire Spin": lambda me, other: simpleDmgMove(
        me,
        other,
        35,
        ["Grass", "Ice", "Bug", "Steel"],
        ["Fire", "Water", "Rock", "Dragon"],
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
    "Ice Shard": lambda me, other: simpleDmgMove(
        me,
        other,
        40,
        ["Grass", "Ground", "Flying", "Dragon"],
        ["Fire", "Water", "Ice", "Steel"],
    ),
    "Double Kick": lambda me, other: simpleDmgMove(
        me,
        other,
        30,
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
    "Confusion": lambda me, other: simpleDmgMove(
        me, other, 50, ["Fighting", "Poison"], ["Psychic", "Steel"]
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
    "Lick": lambda me, other: simpleDmgMove(
        me, other, 30, ["Psychic", "Ghost"], ["Dark"]
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
    "Smog": lambda me, other: simpleDmgMove(
        me, other, 30, ["Grass", "Fairy"], ["Poison", "Ground", "Rock", "Ghost"]
    ),
    "Dream Eater": lambda me, other: simpleDmgMove(
        me, other, 100, ["Fighting", "Poison"], ["Psychic", "Steel"]
    ),
    "Body Slam": lambda me, other: simpleDmgMove(
        me, other, 85, [], ["Rock", "Steel"]
    ),
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
    "Headbutt": lambda me, other: simpleDmgMove(
        me, other, 70, [], ["Rock", "Steel"]
    ),
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
    ) # This is a test move because lmao ha ha
}
