from random import randint

class Player:
    def __init__(self, nome, race, classe, level, inventory):
        self.nome = nome
        self.race = race
        self.classe = classe 
        self.level = level
        self.inventory = inventory

    def lutar (self):
        return randint()