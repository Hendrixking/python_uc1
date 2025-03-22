def apresenta(nome, idade):
    print(f"nome: {nome}, idade: {idade}")

apresenta("Alice", 30)  # posicional
apresenta(idade=30, nome="Alice")  # nomeado

#tarefa02

def saudacao(nome="MUNDO"):
    print(f"Óla, {nome}!") 

saudacao() # saida: Óla, Mundo!
saudacao("Alice") # Saida: Óla, Munado    

#tarefa03

def  lista_nomes(*nomes):
    for nomes in nomes:
        print(nomes)
        
lista_nomes("Alice", "Bob", "Charlie")      

#tarefa04

def saudacao():
    print("Óla do modulo")
if __name__=="__main__":
    saudacao()

#tarefa05

import sys

def main(args):
    for arg in args:
        print(args)

if __name__ =="__main__":
    main

#tarefa06

import sys

def principal(parametros):
    for dado in parametros:
     print(dado)

"""função soma(numero)
- recebe uma vetor com numero a calculo da soma dos mesmos"""

def soma (numero):
  somatorio=0
  for valor in numero:
    somatorio = somatorio + float(valor)
    
    #print (f"o valor do somatorio é {somatorio}")
    return somatorio

if __name__ =="__main__":
 resultado=soma(sys.argv[1:])
print (f" o valor da soma dos numeros é {resultado}")

#tarefa07

def fatorial(n):
    if n < 0:
        return "Número inválido para fatorial."
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
# Exemplo de chamada
print("Fatorial de 5:", fatorial(5))

if __name__=="__main__":
    
 def  testar_fatorial () :
  #exemplo de chamada
  numero=int(input(" Digite um numero: "))
  resultado=fatorial(numero)
  print(f"fatorial de {numero} é igual a {resultado}\n\n")

