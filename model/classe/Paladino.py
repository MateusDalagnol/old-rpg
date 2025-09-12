from model.classe.Classe import Classe

class Paladino(Classe):
    def __init__(self):
        super().__init__('Paladino', 10, 1) 
        self.armas = ['Todas']
        self.armmaduras = ['Todas']
        self.itens_magicos = ['Pergaminho de proteção']
        self.habilidades = {'Maestria em arma' : 1, 'Imunidade a Doenças': 1, 'Cura pelas': 3, 'Aura de proteção': 6, 'Espada Sagrada': 10, 'Aparar': 1} #valor da habilidade indica o nivel necessario para poder usa-la

    def exibir_habilidades(self):
        return super().exibir_habilidades()