import random

def rolagem(self, opcao):
        if(opcao == 'classica'):
            self.forca = rolagem()
            self.destreza = rolagem()
            self.constituicao = rolagem()
            self.inteligencia = rolagem()
            self.sabedoria = rolagem()
            self.carisma = rolagem()
            
        elif(opcao == 'aventureira'):
            atributos_escolhidos = []
            
            for i in range(6):
                
                valor_do_atributo = rolagem()
                print(f'\nValor obtido = {valor_do_atributo}\n')
                
                while True:
                    atributo_escolhido = input('Para qual atributo deseja colocar esse valor: ').lower()
                    
                    if atributo_escolhido in atributos_escolhidos:
                        print("\nVocê já escolheu esse atributo! Tente outro.\n")
                        continue
        
                    if atributo_escolhido not in ['forca','destreza','constituicao','inteligencia','sabedoria','carisma']:
                        print("\nAtributo inválido! Tente novamente.\n")
                        continue
                        
                    if(atributo_escolhido == 'forca'):
                        self.forca = valor_do_atributo
                    elif(atributo_escolhido == 'destreza'):
                        self.destreza = valor_do_atributo
                    elif(atributo_escolhido == 'constituicao'):
                        self.constituicao = valor_do_atributo
                    elif(atributo_escolhido == 'inteligencia'):
                        self.inteligencia = valor_do_atributo
                    elif(atributo_escolhido == 'sabedoria'):
                        self.sabedoria = valor_do_atributo
                    else:
                        self.carisma = valor_do_atributo
                        
                    atributos_escolhidos.append(atributo_escolhido)
                    
                    break
        else:
            atributos_escolhidos = []
            
            for i in range(6):
                
                valor_do_atributo = rolagem_heroica()
                print(f'\nValor obtido = {valor_do_atributo}\n')
                
                while True:
                    atributo_escolhido = input('Para qual atributo deseja colocar esse valor: ').lower()
                    
                    if atributo_escolhido in atributos_escolhidos:
                        print("\nVocê já escolheu esse atributo! Tente outro.\n")
                        continue
        
                    if atributo_escolhido not in ['forca','destreza','constituicao','inteligencia','sabedoria','carisma']:
                        print("\nAtributo inválido! Tente novamente.\n")
                        continue
                        
                    if(atributo_escolhido == 'forca'):
                        self.forca = valor_do_atributo
                    elif(atributo_escolhido == 'destreza'):
                        self.destreza = valor_do_atributo
                    elif(atributo_escolhido == 'constituicao'):
                        self.constituicao = valor_do_atributo
                    elif(atributo_escolhido == 'inteligencia'):
                        self.inteligencia = valor_do_atributo
                    elif(atributo_escolhido == 'sabedoria'):
                        self.sabedoria = valor_do_atributo
                    else:
                        self.carisma = valor_do_atributo
                        
                    atributos_escolhidos.append(atributo_escolhido)
                    
                    break

def rolagem():
    valor_atributo = 0
        
    for i in range(3):
        valor_atributo += random.randint(1,6)
            
    return valor_atributo

def rolagem_heroica():
    valores = []
        
    
    for i in range(4):
        valores.append(random.randint(1,6))

    valores.remove(min(valores))

    
    return sum(valores)
    
            