import random

def rolar_dados(self, opcao):
        if(opcao == 'classica'):
            self.forca = rolagem()
            self.destreza = rolagem()
            self.constituicao = rolagem()
            self.inteligencia = rolagem()
            self.sabedoria = rolagem()
            self.carisma = rolagem()
        elif(opcao == 'aventureira'):
            valores_disponiveis = []
            for i in range(6):
                valores_disponiveis.append(rolagem())

            atributos_escolhidos: list[str] = []

            for i in range(6):
                atributos_escolhidos = verifica_e_adiciona_valor_no_atributo(self,valores_disponiveis, atributos_escolhidos)
        elif(opcao == 'heroica'):
            valores_disponiveis = []
            for i in range(6):
                valores_disponiveis.append(rolagem_heroica())

            atributos_escolhidos: list[str] = []
            for i in range(6):
                atributos_escolhidos = verifica_e_adiciona_valor_no_atributo(self,valores_disponiveis, atributos_escolhidos)
            
@staticmethod
def rolagem():
    valor_atributo = 0
        
    for i in range(3):
        valor_atributo += random.randint(1,6)
            
    return valor_atributo

@staticmethod
def rolagem_heroica():
    valores = []
        
    for i in range(4):
        valores.append(random.randint(1,6))

    valores.remove(min(valores))

    
    return sum(valores)

def verifica_e_adiciona_valor_no_atributo(self, valores_disponiveis, atributos_escolhidos):

    
    while True:
        print("\n<<Valores disponíveis>>\n")
        for i in valores_disponiveis:
            print(f"{i} | ", end='')
        print('\n')

        valor = int(input("Escolha um valor: "))
        if valor not in valores_disponiveis:
            print('O valor escolhido não existe! Tente novamente.')
            continue

        atributo_escolhido = input('Para qual atributo deseja colocar esse valor: ').lower()        
        if atributo_escolhido in atributos_escolhidos:
            print('\nVocê já escolheu esse atributo! Tente outro.\n')
            continue
        
        if atributo_escolhido not in ['forca','destreza','constituicao','inteligencia','sabedoria','carisma']:
            print('\nAtributo inválido! Tente novamente.\n')
            continue
                        
        if(atributo_escolhido == 'forca'):
            self.forca = valor
        elif(atributo_escolhido == 'destreza'):
            self.destreza = valor
        elif(atributo_escolhido == 'constituicao'):
            self.constituicao = valor
        elif(atributo_escolhido == 'inteligencia'):
            self.inteligencia = valor
        elif(atributo_escolhido == 'sabedoria'):
            self.sabedoria = valor
        else:
            self.carisma = valor
        
        valores_disponiveis.remove(valor)
        atributos_escolhidos.append(atributo_escolhido)     
        return atributos_escolhidos                 