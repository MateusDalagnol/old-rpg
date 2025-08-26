from Classe.Classe import Classe

class Guerreiro(Classe):
    def __init__(self):
        super().__init__('Guerreiro', 10, 1) 
        self.armas = ['Todas']
        self.armmaduras = ['Todas']
        self.itens_magicos = ['Pergaminho de proteção']
        self.habilidades = {'Maestria em arma' : 1, 'Ataque extra': 6, 'Aparar': 1} #valor da habilidade indica o nivel necessario para poder usa-la

    def exibir_habilidades(self):
        return super().exibir_habilidades()