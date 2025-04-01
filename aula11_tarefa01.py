pessoa = {"nome" : "papagaio", "idade":  49, "cidade": "petropolis"}
print(f"DADOS DE PESSOA: {pessoa}")

pessoa ["idade"] = 48
print(f"DADOS ATUALIZADO: {pessoa}")

pessoa ["email"] = "luiz.rodrigo.net@gmail.com"
print(f"DADOS ATUALIZADO: {pessoa}")

pessoa [ "sexo"] = "m"
print(f"DADOS ATUALIZADO: {pessoa}")

del pessoa["nome"]
del pessoa["email"]
print(f"DADOS ATUIALIZADO: {pessoa}")
