alunas = {}

aluno_1 = {"nome": "Zoe", "notas": [7, 8, 9]}
aluno_2 = {"nome": "Aurora", "notas": [6, 7, 8]}
aluno_3 = {"nome": "Carlos", "notas": [5, 6, 7]}

print(f" DADOS DA ALUNA{aluno_1}")

print(f"AS NOTAS DA ALUNA {aluno_1['nome']} SÃO {aluno_1['notas']}")

media = sum (aluno_1['nome']) / len (aluno_1['nota'])
print(f"A ALUNA {aluno_1['nome']} OBTEVE A MEDIA IGUAL A : {media}")

aluno_1["media"] = media
print(f"DADOS DA ALUNA_1 {aluno_1}")