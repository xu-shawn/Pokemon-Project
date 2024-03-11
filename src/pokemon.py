class StatusEffect:
    def __init__(self, effect, duration=2):
        self.effect = effect # A function object
        self.duration = duration
    def Run(self, target):
        self.duration -= 1
        self.effect(target)
        if self.duration <= 0:
            return True
        return False
class Pokemon:
    def __init__(self, name, ttype, health, description, statuseffects, *attacks):
        self.name = name
        self.type = ttype # Not using "type" because its a keyword
        self.health = health
        self.maxHealth = health
        self.attacks = attacks
        self.description = description
        self.statusEffects = statuseffects # A list of functions to run every turn
    def Damage(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            pass # lol idk
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