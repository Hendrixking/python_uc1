def calcular_notas (notas):

    menor_nota = min(notas)
    
    notas.remove(menor_nota)
    
    media = sum(notas) / len(notas)
    
    return media
notas = [7.0, 5.0, 4.5, 5.0, 6.5]
media = calcular_notas(notas)
print(f"A MEDIA DAS NOTAS É: {media:.2f}")
    
