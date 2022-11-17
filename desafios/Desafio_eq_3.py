#Questão 01   Nivel fácil 
def soma():
    soma=0
    n=int(input("Digite um numero:\n"))
    for nu in range(n+1):
        soma=soma+nu
    print(f"A soma de todos os numeros menores ou igual a {n} eh:{soma}")
soma()


#questão 02
def ano():
    a=int(input("Digite um ano para descobrir se ele é bissexto:\n"))
    if a % 4 == 0:
        return print(True)
    else:
        return print(False)
ano()


#Questão 03
cont=[1]
def numero():
    n=int(input("Digite um numero para saber as potências de 2 menores ou iguais a ele:\n"))
    contador=1
    while contador != n:
        contador=contador+1
        if contador**2 <= n:
            cont.append(contador)
        else:
            break
    print("as potências de 2 menores ou iguais a",n,"são",cont)

numero()


#Questão 04
def bi():
    n=int(input("Digite um numero para transforma-lo em binario:\n"))
    binario = format(n,"b")#transforma o numero em binario aq
    print("o numero {} em binario fica {}".format(n,binario))
bi()


#Questão 05
def lis():
    l=int(input("Qual sera o tamanho da lista?\n"))
    lista=[]
    while len(lista) != l:
        x=int(input("Digite um numero a lista:  "))
        lista.append(x)
    if l in lista:
        return print(True)
    else:
        return print(False)
lis()