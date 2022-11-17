n=input("Digite um numero")
try:
    float(n)
    print(n)
except ValueError:
    print("Erro")