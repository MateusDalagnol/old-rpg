
from rolagem import rolagem

class Personagem:
    def __init__(self, opcao, nome, classe, raca):
        self.nome = nome
        self.classe = classe
        self.raca = raca
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligencia = 0
        self.sabedoria = 0
        self.carisma = 0
    
        rolagem(self, opcao)
            
    def __str__(self):
        return f'\nNome = {self.nome}\nClasse = {self.classe}\nRaca = {self.raca}\nForca = {self.forca}\nDestreza = {self.destreza}\nConstituicao = {self.constituicao}\nInteligencia = {self.inteligencia}\nSabedoria = {self.sabedoria}\nCarisma = {self.carisma}\n'
    
    
    
    



