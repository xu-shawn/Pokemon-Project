class Pokemon:
    def __init__(self, name, ttype, health, *attacks):
        self.name = name
        self.type = ttype # Not using "type" because its a keyword
        self.health = health
        self.attacks = attacks