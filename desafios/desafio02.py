n=int(input("Digite um numero maior que 100 :"))
"""
while n <=100:
    print("o numero tem que ser maior que 100")
    n=int(input("Digite um numero maior que 100 :"))
"""
if n <= 100:
    print("o numero tem q ser maior que 100")
else:
    print(list(range(0,n+2,2)))

nota=int(input("Digite sua nota entre 0 e 10"))
while nota > 10 or nota < 0:
    print("valor invalido")
    nota=int(input("Digite sua nota entre 0 e 10"))
else:
    print("valor valido")
