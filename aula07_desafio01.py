n= int(input(" DIGITE UM NUMERO: "))
fatorial = 1
contador = n
while contador > 1:
    fatorial *= contador
    contador -= 1
print(f"O FATORIAL DE {n} É: {fatorial}")