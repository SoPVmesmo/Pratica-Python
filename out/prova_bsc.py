import datetime
from wsgiref.simple_server import sys_version
def Q1():
    n1=float(input("Digite sua 1 nota"))
    n2=float(input("Digite sua 2 nota"))
    n3=float(input("Digite sua 3 nota"))
    n4=float(input("Digite sua 4 nota"))
    m=(n1+n2+n3+n4)/4
    print(f"Sua media foi {m}")

def Q2():
    m=float(input("Digite os metros"))
    c=m*100
    print(f"{m} metros convertido em centimentros fica {c} centimetros")

def Q3():
    h=int(input("Quantas horas por mês vc trabalha?"))
    d=float(input("Quanto vc ganha por hora ?"))
    s_b=h*d
    i=s_b * 0.24
    s_l=s_b - i
    print(f"Seu salario com os impostos fica {s_l}")

def Q4():
    data=datetime.date.today()
    hora=datetime.datetime.now()
    print(data)
    print(hora)

def Q5():
    r=float(input("Digite o raio"))
    a_c=(r*2)*3.14
    print(f"A area do circulo é {a_c}")

def Q6():
    f="A casa do garoto tem algumas coisas legais"
    vogais="aA"
    for i in range(len(vogais)):
        f=f.replace(vogais[i],"")#replace troca uma letra por outra
    print(f)

def Q7():
    print(sys_version)#imprimir a versão do python

def Q8():
    termo=int(input("Digite um termo:\n"))
    num1,num2=0,1
    contador = 0
    while contador < termo:
        num3 = num1 + num2
        if num3 == termo:
            print("termo encontrado")
            break
        num1= num2
        num2=num3 
        contador +=1

def Q9():
    d=int(input("Digite a quantidade de dias"))
    t_h=d*24
    print(f"{d} tem o total de {t_h} horas")

def Q10():
    num=str(int(2**10000))
    print(f"A quantidade de digitos é {len(num)}")

def Q11():
    lista=[10,11,20,22,30,33,40,44,50,55,60,66,70,77,80,88,90,99]

    impares = [num for num in lista if num % 2 == 1]
    pares = [num for num in lista if num % 2 == 0]
    multiplos_2 = [num for num in lista if num % 2 == 0]


    print(f"Os impares são {impares}")
    print(f"OS pares são {pares}")
    print(f"OS multiplos de 2 são {multiplos_2}")

def Q12():
    while True:
        compri=float(input("Digite o 1 valor"))
        lar=float(input("Digite o 3 valor"))

        if compri != lar:
            a=compri * lar
            print(f"a area do terreno é {a}")
            break
        else:
            print("Não é um retangulo")
