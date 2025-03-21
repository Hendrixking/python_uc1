soma = 0
while True:
    numero = int(input(" DIGITE UM NUMERO POSITIVO OU UM NUMERO NEGATIVO PARA ENCERRAR: "))
    if numero < 0:
        break
    soma += numero
print(f"A SOMA DOS NUMEROS POSITIVO DIGITADO É: {soma}")