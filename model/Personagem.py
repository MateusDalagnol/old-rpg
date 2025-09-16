class Personagem:
    def __init__(self, nome, classe, raca, atributos):
        self.nome = nome
        self.nivel = 1
        self.classe = classe
        self.raca = raca
        self.forca = atributos[0] if atributos else 0
        self.destreza = atributos[1] if atributos else 0
        self.constituicao = atributos[2] if atributos else 0
        self.inteligencia = atributos[3] if atributos else 0
        self.sabedoria = atributos[4] if atributos else 0
        self.carisma = atributos[5] if atributos else 0
            
    def exibir_personagem(self):
        print(f'\nNivel = {self.nivel}\nNome = {self.nome}\nClasse = {self.classe.nome}\nRaca = {self.raca.nome}')
        self.raca.exibir_habilidades()
        self.classe.exibir_habilidades()
        print(f'\nForca = {self.forca}\nDestreza = {self.destreza}\nConstituicao = {self.constituicao}\
        \nInteligencia = {self.inteligencia}\nSabedoria = {self.sabedoria}\nCarisma = {self.carisma}\n')