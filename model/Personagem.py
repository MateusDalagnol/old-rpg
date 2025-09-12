from model.rolagem import rolar_dados

class Personagem:
    def __init__(self, opcao, nome, classe, raca):
        self.nome = nome
        self.nivel = 1
        self.classe = classe
        self.raca = raca
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligencia = 0
        self.sabedoria = 0
        self.carisma = 0
    
        rolar_dados(self, opcao)
            
    def exibir_personagem(self):
        print(f'\nNivel = {self.nivel}\nNome = {self.nome}\nClasse = {self.classe.nome}\nRaca = {self.raca.nome}')
        self.raca.exibir_habilidades()
        self.classe.exibir_habilidades()
        print(f'\nForca = {self.forca}\nDestreza = {self.destreza}\nConstituicao = {self.constituicao}\
        \nInteligencia = {self.inteligencia}\nSabedoria = {self.sabedoria}\nCarisma = {self.carisma}\n')
    
    
    
    



