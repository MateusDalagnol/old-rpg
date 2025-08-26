class Classe:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.armas = []
        self.armaduras = []
        self.itens_magicos = []
        self.habilidades = {}

    def exibir_habilidades(self):
        print(f'Habilidades da Classe: ')
        for habilidade in self.habilidades:
            print(habilidade, ' | ', end='')
        print('\n')