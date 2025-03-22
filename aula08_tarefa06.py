
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