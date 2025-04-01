class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False
 
    def exibir_info (self):
        if self.ligado == True:
            status = "LIGADO"
        else:
            status = "DESLIGADO"
        print(f"{self.marca} {self.modelo} ({self.ano}) ESTA {status} ")


    def ligar (self):
        self.ligado = True
        print(f"O CARRO ESTA LIGADO ")

    def desligar (self):
        self.ligado = False
        print(f"O CARRO ESTA DESLIGADO ")




if __name__=="__main__" :
    
    print(f"CRIANDO UM OBJETO DA CLASSE CARROS")
    meu_carro = Carro("SUBARO", "LEXUS", 2020)
    
    meu_carro.exibir_info()
    meu_carro.ligar()
    meu_carro.desligar()
    
    
    
    
    #print(meu_carro)