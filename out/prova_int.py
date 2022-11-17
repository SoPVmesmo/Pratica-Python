from datetime import datetime
def Q1():
    print("====================")
    print("Bem vindo a posto PV")
    print("====================")
    print('''=> Tabela de descontos <=
acool acima de 20 litros desconto de 5%
gasolina acima de 40 litros desconto de 6%\n''')
    x=input('''Oque vc deseja 
[A]alcool 4,59
[G]gasolina 5,85\n''')

    xx=x.isalpha()
    if xx == True:
        x=x.lower()

        if x == "a":
            q=input("Digite a quantidade de litros:\n")
            qq=q.isnumeric()
            
            if qq == True:
                q=int(q)
                print("AQUI")
                if q > 20 and q > 0:
                    valor=q * 4.59
                    desconto= valor * 0.05
                    valor= valor - desconto
                    print(f"Valor a pagar {valor}")

                elif q < 21 and q > 0:
                    valor=q * 4.59
                    print(f"Valor a pagar {valor}")   
                else:
                    print(q)
                    print("valor invalido")
            else:
                print("Valor invalido")             
                            
        elif x == "g":
            x=x.lower()
            q =input("Digite a quantidade de litros:\n")
            qq=q.isnumeric()

            if qq == True:
                q=int(q)

                if q > 40.0 and q > 0.0:
                    valor=q * 5.85 
                    desconto=valor * 0.06
                    valor=valor - desconto
                    print(f"Valor a pagar {valor}")
                elif q <= 40.0 and q > 0.0:
                    valor=q* 5.58
                    print(f"Valor a pagar {valor}")
                else:
                    print("Valor invalido")
            else:
                print("Valor invalido")
        else:
            print("Valor invalido")
    else:
        print("valor invalido")

def Q2():
    hora_atual= datetime.now()
    
    h=hora_atual.strftime("%H")
    h_completo=hora_atual.strftime("%H:%M:%S")
    my_dict ={
        "manha":"Bom dia!",
        "tarde":"boa tarde",
        "noite":"Boa noite"
    }

    if int(h) >= 1 and int(h) < 12:
        print("São extamente: ",h_completo," Tenha um ",my_dict["manha"])
    elif int(h) >= 12 and int(h) < 18:
        print("São exatamente: ",h_completo," tenha uma ",my_dict["tarde"])
    else:
        print("São exatamente: ",h_completo, "tenha uma ",my_dict["noite"])

def Q3():
    h_a=100000
    h_m=45000
    cont=0
    while h_m <= h_a:
        h_a1=h_a * (1.5/100)
        h_m1=h_m * (3/100)

        h_a=h_a1 + h_a
        h_m=h_m + h_m1 
        cont=cont+1
    print(f"São necessarios {cont} anos pra se igualar ou superar os habitantes")

def Q4():
    n=input("Digite seu nome\n")
    cont=1
    for i in n :
        print(n[0:cont])
        cont=cont+1

def Q5():

    lista01=[]
    lista02=[]
    lista03=[]
    cont=1
    for i in range(5):
        n=input(f"Digite o {cont} item da Primeira lista\n")
        n2=input(f"Digite o {cont} item da Segunda lista\n")
        lista01.append(n)
        lista02.append(n2)
        lista03.append(n)
        lista03.append(n2)
        cont += cont
    print(f"Primeira lista {lista01}")
    print(f"Segunda lista {lista02}")
    print(f"Terceira lista {lista03}")

def Q6():
    lista=["Conhece a vitima ?","Esteve no local do crime ?","trabalha no local ?","se encontrou com a vitima ?"]
    cont=0
    for i in range(len(lista)):
        s=input(lista[i])
        if s == "sim":
            cont = cont + 1
    print(cont)
    if cont == 2:
        print("Suspeito")
    elif cont == 3:
        print("Cúmplice")
    elif cont == 4:
        print("Culpado")
    else:
        print("inocente")

def Q7():
    n=int(input("Digite um numero"))
    no=str(n)
    print(no*n)

def Q8():
    n=input("Digite um numero")
    q=len(n)
    q=int(q)
    s=q+q
    strq=str(q)
    r=strq[::-1]
    print(f"o len é {q} o reverso é {r} e a soma é {s}")
