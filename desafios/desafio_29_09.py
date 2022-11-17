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
    d_i=[]
    m_i=[]
    d=input("Digite o dia do seu nascimento:\n")
    m=input("Digite o mês do seu nascimento:\n")
    a=int(input("Digite o ano do seu nascimento:\n"))

    for x in d:
        d_i.append(x)
    d_i.reverse()

    for y in m:
        m_i.append(y)
    m_i.reverse()

    print(f"Sua  senha é : {m}@{d_i[0]}{d_i[1]}%{d}&{m_i[0]}{m_i[1]}{a}")
   
senha()

#Questão 04
def palavra():
    l=[]
    l_i=[]
    p=input("Digite uma palavra para ver se ela é palíndromo:\n")
    for x in p:
        l.append(x)
        l_i.append(x)
    l_i.reverse()
    if l_i == l:
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