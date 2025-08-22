from Personagem import Personagem

def criar_personagem():
    nome = input('digite o nome do personagem: ')
    classe = input('digite a classe do personagem: ')
    raca = input('digite a raça do personagem: ')
    opcao = input('digite o estilo de rolagem desejada:  Classica, Aventureira ou Heroica: ').lower()

    return Personagem(opcao, nome, classe, raca)   

personagem = criar_personagem()

print(personagem)



