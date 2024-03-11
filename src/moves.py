from pokemon import *

statusFire = StatusEffect()


def simpleDmgMove(self, other, power=0, effective=[], noteffective=[]):
    if other.type in effective:
        other.Damage(power * 2)
    elif other.type in noteffective:
        other.Damage(power // 2)
    else:
        other.Damage(power)
    # Add to UI


def tickFire(self):
    self.Damage(10)
    # Add to UI


def inflictFireMove(self, other, power=0, effective=[], noteffective=[]):
    simpleDmgMove(self, other, power, effective, noteffective)
    other.addStatus(statusFire.deepcopy())


MOVES_DICTIONARY = {
    "Scratch": lambda me, other: simpleDmgMove(
        me, other, 40, ["N/A"], ["Rock", "Steel"]
    ),
    "Tackle": lambda me, other: simpleDmgMove(
        me, other, 40, ["N/A"], ["Rock", "Steel"]
    ),
    "Pound": lambda me, other: simpleDmgMove(me, other, 40, ["N/A"], ["Rock", "Steel"]),
    "Rage": lambda me, other: simpleDmgMove(me, other, 20, ["N/A"], ["Rock", "Steel"]),
    "Fury Attack": lambda me, other: simpleDmgMove(
        me, other, 15, ["N/A"], ["Rock", "Steel"]
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
        me, other, 85, ["N/A"], ["Rock", "Steel"]
    ),
    "Double Slap": lambda me, other: simpleDmgMove(
        me, other, 15, ["N/A"], ["Rock", "Steel"]
    ),
    "Razor Leaf": lambda me, other: simpleDmgMove(
        me,
        other,
        55,
        ["Water", "Ground", "Rock"],
        ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
    ),
    "Headbutt": lambda me, other: simpleDmgMove(
        me, other, 70, ["N/A"], ["Rock", "Steel"]
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
}
