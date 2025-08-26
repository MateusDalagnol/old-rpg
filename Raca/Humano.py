from Raca.Raca import Raca

class Humano(Raca):
    def __init__(self):
        super().__init__('Humano', 9, 0, 'Qualquer')
        self.habilidades = ['Aprendizado', 'Adaptabilidade']

    def exibir_habilidades(self):
        super().exibir_habilidades()
