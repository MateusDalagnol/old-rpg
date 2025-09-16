from model.Personagem import Personagem
from model.classe.Guerreiro import Guerreiro
from model.classe.Paladino import Paladino
from model.classe.Ladrao import Ladrao
from model.raca.Anao import Anao
from model.raca.Elfo import Elfo
from model.raca.Halfling import Halfling
from model.raca.Humano import Humano

def criar_personagem(nome, classe_str, raca_str, valores):
    # Escolher classe
    if classe_str.lower() == "guerreiro":
        classe = Guerreiro()
    elif classe_str.lower() == "paladino":
        classe = Paladino()
    elif classe_str.lower() == "ladrao":
        classe = Ladrao()
    else:
        raise ValueError("Classe inválida")

    # Escolher raça
    if raca_str.lower() == "anao":
        raca = Anao()
    elif raca_str.lower() == "humano":
        raca = Humano()
    elif raca_str.lower() == "elfo":
        raca = Elfo()
    elif raca_str.lower() == "halfling":
        raca = Halfling()
    else:
        raise ValueError("Raça inválida")

    # Retorna a instância do personagem com os valores
    return Personagem(nome, classe, raca, valores)