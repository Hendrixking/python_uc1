idade =int(input("digite sua idade."))
renda =float(input("qual sua renda."))
nome_sujo= input("voce tem nome sujo.")


if idade >=21 and renda >= 2000 and nome_sujo == "n":
    print ("!!!Emprestimo liberado!!!")
else:
    print ("!!!Emprestimo negado!!!")