primeiro_numero= float(input("me dê um numero: "))
segundo_numero= float(input("me dê um numero: "))

if primeiro_numero > segundo_numero:
    print(f"o maior numero é {primeiro_numero}")
elif segundo_numero > primeiro_numero:
    print(f"o maior numero é {segundo_numero}")
else:
    print("os dois numeros são iguais")