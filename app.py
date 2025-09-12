from model.Personagem import Personagem
from model.classe.Guerreiro import Guerreiro
from model.classe.Paladino import Paladino
from model.classe.Ladrao import Ladrao
from model.raca.Anao import Anao
from model.raca.Elfo import Elfo
from model.raca.Halfling import Halfling
from model.raca.Humano import Humano

def escolher_classe():
    try:
        print('\n=== Escolha sua classe ===\n1 - Guerreiro\n2 - Paladino\n3 - Ladrão')
        opcao = int(input('Ecolha uma classe: '))

        if opcao == 1:
            return Guerreiro()
        elif opcao == 2:
            return Paladino()
        elif opcao == 3:
            return Ladrao()
        else:
            print('opção invalida')
            return escolher_classe()
    except:
        print('\nCaracter invalido: digite apenas números')
        input('Digite uma tecla para voltar ao menu... ')
        return escolher_classe()

    
def escolher_raca():
    try:
        print('\n=== Escolha sua classe ===\n1 - Anão\n2 - Humano\n3 - ELfo\n4 - Halfling')
        opcao = int(input('Ecolha uma classe: '))

        if opcao == 1:
            return Anao()
        elif opcao == 2:
            return Humano()
        elif opcao == 3:
            return Elfo()
        elif opcao == 4:
            return Halfling()
        else:
            print('opção invalida')
            return escolher_raca()
    except:
        print('\nCaracter invalido: digite apenas números')
        input('Digite uma tecla para voltar ao menu... ')
        return escolher_raca()

def criar_personagem():
    nome = input('Digite o nome do personagem: ')
    classe = escolher_classe()
    raca = escolher_raca()
    opcao = input('\nDigite o estilo de rolagem desejada:  Classica, Aventureira ou Heroica: ').lower()
    return Personagem(opcao, nome, classe, raca)

if __name__ == '__main__':
    personagem = criar_personagem()
    personagem.exibir_personagem()

