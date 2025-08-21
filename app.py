import Personagem

opcao = input('digite o estilo de rolagem desejada: ')

personagem = Personagem.Personagem(opcao, nome="Lorien",classe="Mago",raca="Elfo")

print(personagem)