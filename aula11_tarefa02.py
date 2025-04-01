
 
d1 = {"a": 1, "b": 2}
d2 ={"b": 3, "c": 4}

d1.update(d2)

print("RESULTADO",d1)


d1 = {"a":1, "b":2}
d3 ={"a":1, "b":2}

d2 = {"b":3,"c": 4}

print(f"DICIONARIO ORIGINAL: ")
print(f"D1       :{d1}")
print(f"D2       :{d2}")

d1.update(d2)
d2.update(d3)


print(f"DICIONARIO ATUALIZADO: ")
print(f"D1       :{d1}")
print(f"D2       :{d2}")



frase = "o rato roeu a roupa do rei de roma"
palavras = frase.split()
contagem = {}

for palavra in palavras:
 contagem[palavra] = contagem.get(palavra, 0) +1

print(contagem)









