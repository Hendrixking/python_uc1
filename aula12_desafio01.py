class Conta :
    def __init__ (self, numero, titular, limite,):
        self.titular = titular
        self.numero = numero
        self.limite = limite
        self.saldo = 1500
       
    
    def deposito (self,valor) :
        print(f" VALOR INICIAL: {self.saldo}")
        self.saldo = self.saldo + valor
        print(f" SALDO FINAL : {self.saldo}")

    def sacar (self,valor) :
       print(f" VALOR INICIAL: {self.saldo}")
       self.saldo = self.saldo + valor
       if self.limite + self.limite < valor :
          print(f"ERRO!!!SALDO INSUFICIENTE")
       else:
        print(f"LIMITE NAO ATINGIDO")


    def info (self) :
        print(f"CONTA: {self.numero} - {self.titular} - {self.saldo} ")

class Banco:
    def __init__(self) :
        self.conta=()



 
if __name__=="__main__":
    print(f"CRIANDO A PRIMEIRA CONTA")
    cc_1= Conta ("000001", " Papagaio", 1500.20)
    #cc_1.info()
    cc_1.deposito(1500)
    cc_1.sacar(3100)