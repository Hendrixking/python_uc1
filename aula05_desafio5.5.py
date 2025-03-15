nome = input("digite seu nome.")
senha = input("digite sua senha.")

if (len(nome) < 3 ):
    print("!!!ERRO senha invalida !!!")

elif (len(senha) < 6 ):
    print("!!! ERRO senha invalida !!!")

elif (senha=="123456") or (senha=="senha"):

    print("!!! erro senha fraca !!!")
else:
    print(" {ok} senha valida!!!!")