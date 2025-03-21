import random


numero = random.randint(1, 100)

print(f"Tabela de multiplicação do número {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")