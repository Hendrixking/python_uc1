# CRIANDO E IMPRIMINDO UMA LISTA

vet_dados =[19 , 21, 10, 96, 41]

def criar_inprimir_lista ():
    vetor = [10 , 15, 25, 45, 90]
    print(f"\n\tO CONTEUDO DO VETOR É ({vetor})\n")

def criar_imprimir_lista_v2 (vetor):
    print(f"\n\tO CONTEUDO DO VETOR É {vetor}\n")


def interando_sobre_lista (vetor) :
    for i in vetor:
        print(f"Valor do elemento {i} ")


def soma_dos_elementos (vetor) :
    soma = sum(vetor) 
    print(f"SOMA DOS VETORES: {soma}")


def maior_e_menor (vetor):
    maior = max(vetor)
    minimo = min(vetor)
    print("MAIOR VALOR:,{}".format(maior))
    print("MINIMO VALOR: {}".format(minimo))


def inverter_ordem (vetor):
    vetor_invertido = vetor[::-1]
    print(f"VETOR INVERTIDO: {vetor_invertido}")


def multiplicar_elementos (vetor):
    multiplicador = 2
    vetor_multi = [elemento * multiplicador for elemento in vetor]
    print(f"VETOR MULTIPLICADOR:, {vetor_multi}")


def conta_quantas_vezes_o_valor_3 (vetor):
    ocorrencias = vetor.count(3)
    print(f"O VALOR 3 APARECE:", {ocorrencias}, "VEZES")


def ordenar_ordem_crescente (vetor):
    vetor_ordenado= sorted(vetor)
    print(f"VETOR ORDENADO:, {vetor_ordenado}")


def remover_elementos_duplicado (vetor):
    vetor_sem_duplicado = list(dict.fromkeys(vetor))
    print(f"VETOR SEM DUPLICATAS: , {vetor_sem_duplicado}")


def pares_e_impar (vetor):
    pares = [num for num in vetor if num % 2 == 0]
    impares = [num for num in vetor if num % 2 != 0]
    print(f"PARES,{pares}")
    print(f"IMPARES, {impares}")


def calcular_media (vetor):
    media = sum(vetor) / len(vetor)
    acima_media = [num for num in vetor if num > media]
    print(f"MEDIA:", media)
    print(f"ELEMENTOS ACIMA DA MEDIA:, {acima_media}")





if __name__=="__main__" :
    
 interando_sobre_lista (vet_dados)
 maior_e_menor (vet_dados)
 soma_dos_elementos(vet_dados)
 inverter_ordem (vet_dados)
 multiplicar_elementos (vet_dados)
 conta_quantas_vezes_o_valor_3 (vet_dados)
 ordenar_ordem_crescente (vet_dados)
 remover_elementos_duplicado (vet_dados)
 pares_e_impar (vet_dados)
 calcular_media (vet_dados)