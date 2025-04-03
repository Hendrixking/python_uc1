class Veiculo:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    
    def exibir_info(self):
        print(f"{self.marca} {self.modelo} {self.ano}")


class Carro(Veiculo):
      
    def __init__(self, marca, modelo, ano, portas, cor , placa ):
        super().__init__(marca, modelo, ano, cor)
        self.portas = portas
        self. placa = placa
    
    def exibir_info(self):
        super().exibir_info()
        print(f"ESTE CARRO TEM {self.portas} PORTAS")
        print(f"A PLACA DO CARRO É {self.placa}")

meu_carro = Carro("TOYOTA", "COROLLA", 2020, 4, "azul", "ktz902m23")
meu_carro.exibir_info()

     
    




    