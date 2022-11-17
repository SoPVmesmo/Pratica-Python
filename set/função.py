def par(n):
    return(n % 2 == 0)

print(par(3))
def hello(nome):
    print("iae",nome)
hello("Paulo")

def mult(x,num=2):
    return x, x*num
    
a,b=mult(2)
print(a,b)

a,b=mult(2, num=10)
print(a,b)

a,b=mult(3,5)
print(a,b)


def mensagem(msg):
    print("-"*20)
    print(   msg  )
    print("-"*20)
mensagem("  Erro de sistema  ") 


def soma(a=0,b=0,c=0):
    print(f"A={a} e B={b} C={c}")
    s=a+b+c
    print(f"A soma dos numeros eh: {s}")
soma(c=10,b=5)


def soma_n(*valores):
    s=0
    for num in valores:
        s += num
        print('Somando os valores{} temos {}'.format(valores,s))


soma_n(1,2,3)
soma_n(1,2,3,4,5)


def cont(*num):
    for valor in num: 
        print(f"{valor}",end='')
    print("Fim")

def conte(*num):
    tam=len(num)
    print(f"recebe os valores{num} e são ao todo {tam}")
conte(1,2,3)
conte(1,2,3,4)


a=[1,2,3,4]
def dobra(lst):
    pos=0
    while pos < len(lst):
        lst[pos]*=2
        pos+=1
dobra(a)
print(a)

def msg(msg):
    print("-"*len(msg))
    print(msg)
    print("-"*len(msg))
msg("vendo se isso vai da certo")