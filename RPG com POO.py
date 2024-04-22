from random import randint

class Player:
    def __init__(self, nome, race, classe, level, inventory):
        self.nome = nome
        self.race = race
        self.classe = classe 
        self.level = level
        self.inventory = inventory

    def atacar (self, classe):
        rolagem = randint(1,20)
        if classe['Atk Mod'] != 0:
            atk_roll = rolagem + classe['Atk Mod']
        else:
            atk_roll = rolagem + classe['Spl Mod']

        return atk_roll
    
    def testes(self):
        return randint(1, 20)

def selec_classe():

    classe = 'Inicio'
    
    while classe != 'Mago' or classe != 'Lutador':

        classe = input('Qual classe deseja ser? \n Mago \n Lutador').capitalize()

        if classe == 'Mago':
            atributos = {'Armadura': 10, 'Atk Mod': 0, 'Spl Mod': 2}
        elif classe == 'Lutador':
            atributos = {'Armadura': 13, 'Atk Mod': 2, 'Spl Mod': 0}
        else:
            print(f'As classes disponiveis são lutador e mago. \n Sua seleção: {classe} \n Por favor selecione uma classe válida')

    return atributos

