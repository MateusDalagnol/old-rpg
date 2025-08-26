from Classe.Classe import Classe

class Ladrao(Classe):
    def __init__(self):
        super().__init__('Ladrao', 6, 1)
        self.armas = ['Pequenas', 'Medias']
        self.armaduras = ['Leves']
        self.itens_magicos = ['Pergaminho de proteção']
        self.habilidades = {'Ataque furtivo': 1, 'Ouvir ruidos': 1, 'Talentos de ladrão': 1}#valor da habilidade indica o nivel necessario para poder usa-la

    def exibir_habilidades(self):
        super().exibir_habilidades()