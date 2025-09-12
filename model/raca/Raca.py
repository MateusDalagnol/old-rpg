class Raca:
    def __init__(self, nome, movimento, infra_visao, alinhamento):
        self.nome = nome
        self.movimento = movimento
        self.infra_visao = infra_visao
        self.alinhamento = alinhamento
        self.habilidades = []

    def exibir_habilidades(self):
        print(f"Habilidades da Raça: ")
        for habilidade in self.habilidades:
            print(habilidade, ' | ', end='')
        print('\n')