l1= input("digite.")
l2= input("digite")
l3= input("digite;")

if (l1 == l2 == l3):
    print("!!! seu triangulo é um equilátero !!!")
elif (l1==l2) or (l1==l3) or (l2==l3):
    print("!!! se triangulo é um isósceles")
else:
    print("!!!! seu triangulo é um escaleno!!!")
