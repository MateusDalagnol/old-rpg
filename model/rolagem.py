import random

def rolar_dados(opcao):
    valores_disponiveis = []
    if(opcao == 'classica'):
        for _ in range(6):
            valores_disponiveis.append(rolagem())
    elif(opcao == 'aventureira'):
        for _ in range(6):
            valores_disponiveis.append(rolagem())
    elif(opcao == 'heroica'):
        for _ in range(6):
            valores_disponiveis.append(rolagem_heroica())
    return valores_disponiveis

def rolagem():
    valor_atributo = 0
    for _ in range(3):
        valor_atributo += random.randint(1,6)
    return valor_atributo

def rolagem_heroica():
    valores = []
    for _ in range(4):
        valores.append(random.randint(1,6))
    valores.remove(min(valores))
    return sum(valores)