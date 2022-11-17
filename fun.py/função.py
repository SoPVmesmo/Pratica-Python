"""#Questão 01   Nivel fácil 
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
        x=int(input(f"Digite o {len(lista)} numero a lista:  "))
        lista.append(x)
    if l in lista:
        return print(True)
    else:
        return print(False)
lis()


#Questão 01        NIvel médio
def n():
    n=int(input("Digite um numero:\n"))
    for x in range(n+1):
        if x % 3 == 0 and x % 5 !=0:
            print(x," = back")
        elif x % 5 == 0 and x % 3 != 0:
            print(x," = front")
        elif x % 5 == 0 and x % 3 == 0:
            print(x," = back e front")
        else:
            print(x)
n()


#Questão 02
def nota():
    n=float(input("Digite sua nota de 0 a 5 para ver como ficaria em EUA:\n"))
    if n == 5:
        n_e="A"
    elif n >= 4.77:
        n_e="-A"
    elif n >= 4.33 and n <= 4.76:
        n_e="+B"
    elif n >= 3.9 and n <= 4.32:
        n_e="B"
    elif n >= 3.47 and n <= 3.89:
        n_e="-B"
    elif n >= 3.0 and n <= 3.46:
        n_e="+C"
    elif n >= 2.6 and n <= 2.99:
        n_e="C"
    elif n >= 2.17 and n <= 2.59:
        n_e="-C"
    elif n >= 1.3 and n <= 2.16:
        n_e="D"
    elif n == 0:
        n_e="F"        
    print(f"Sua nota foi {n} e convertendo-a para nota dos EUA fica {n_e}")

nota()

#Questão 03 
def senha():
    d=input("Digite o dia do seu nascimento:\n")
    m=input("Digite o mês do seu nascimento:\n")
    a=int(input("Digite o ano do seu nascimento:\n"))

    print(f"Sua  senha é : {m}@{d[::-1]}%{d}&{m[::-1]}{a}")
   
senha()

#Questão 04
def palavra():
    p=input("Digite uma palavra para ver se ela é palíndromo:\n")
   
    if p[::-1] == p:
        print(f"A palavra {p} é uma Palíndromo")
    else:
        print(f"A palavra {p} não é uma Palíndromo")
palavra()


#Questão 05
def tri():
    l=[]
    while len(l) != 3:
        x=int(input("Digite um numero\n"))
        if x < 0:
            break
        else:
            l.append(x)
    if len(l) < 3:
        print("Não é possivel fazer um triangulo com esses valores")
    else:
        if l.count(x) == 3:
            print("È um triangulo Equilátero")
        
        elif l.count(x) == 2:
            print("È um triangulo Isósceles")

        else:
            print("È um triangulo Escaleno")

           
tri()
"""
dici02={}
def ad_cliente(): 
    n= int(input("Digite quantos clientes serão adicionados:\n"))
    y=len(dici02) + n
    while len(dici02) != y:
        x=len(dici02)+1
        nome=input(f"Digite o nome do cliente {x}:\n")
        dici02[x]=nome

ad_cliente()
print(dici02)