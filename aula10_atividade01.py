
# CRIANDO UMA MATRIZ

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]


print ("Elemento (0,0):", matriz[0][0]) #SAIDA  1
print ("Elemento (2,1):", matriz[2][1]) #SAIDA  2


matriz = matriz_4_4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16] 
    ]

def imprimir_matriz_v1():
   matriz=[]
   for linha in matriz:
     print(f"|",end=" ")
   for elemento in linha:
     print(elemento, end="|")
     print()


def criar_e_exibir_matriz():
 matriz = []
 for i in range(4):
  linha = []
  for j in range(4):
   valor = int(input(f"Digite o valor para [{i}][{j}]: "))
  linha.append(valor)
  matriz.append(linha)
  for linha in matriz:
     print(linha)


def somar_elementos_v2():
  soma = 0
  for i in range(4): 
   soma=soma + sum ( matriz_4_4 [i])
   input(f"DIGITE O VALOR PARA {soma}: ")
   print("\n\n")

for i in range(4):
  maior=max(matriz[i])
  print(f"maior valor da linha {i}: {maior})")

def contar_numeros_pares_e_impares():
  pares = sum(1 for linha in matriz for num in linha if num % 2 == 0)
  print(f"Quantidade de números pares: {pares}")

vet_pares=[]
vet_impares=[]
impares = 0
pares = 0
for i in range(4):
    for j in range(4):
        if matriz[i][j] % 2 == 0:
            pares = pares + 1
            vet_pares.append(matriz[i][j])
        else:
            impares = impares + 1
            vet_impares.append(matriz[i][j])

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números pares: {impares}")
print(f"Quantidade de números pares: {vet_pares}")
print(f"Quantidade de números pares: {vet_impares}")

def multiplicar():
  num = int(input("Digite o número para multiplicação: "))
  linha_escolhida = int(input("Digite a linha a ser multiplicada (0-3): "))
  matriz[linha_escolhida] = [num * valor for valor in matriz[linha_escolhida]]
  for linha in matriz:
     print(linha)
num = int(input("Digite o número para multiplicação: "))
linha_escolhida = int(input("Digite a linha a ser multiplicada (0-3): "))
for j in range(4):
    matriz[linha_escolhida][j] *= num
for linha in matriz:
    print(linha)

num = int(input("DIGITE UM NUMERO: "))
linha_escolhida = int(input("DIGITE UM NUMERO: "))

linha= matriz_4_4[linha_escolhida]

for posiçao in range(4):
 linha[posiçao] = linha[posiçao] * num

 print(linha)







if __name__=="__main__" :
 
 imprimir_matriz_v1
 criar_e_exibir_matriz
 somar_elementos_v2
 contar_numeros_pares_e_impares
 multiplicar 