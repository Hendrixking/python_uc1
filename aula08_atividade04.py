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
    
def  testar_fatorial () :

  numero=int(input(" Digite um numero: "))
  resultado=fatorial(numero)
  print(f"fatorial de {numero} é igual a {resultado}\n\n")

  if __name__=="__main__":
    testar_fatorial()


  