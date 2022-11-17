import random 
print("*"*32)
print("Bem vindo ao jogo da adivinhação")
print("*"*32)
numero=random.randrange(0,101)
ganhou=False
perdeu=False
lista=[]
chances=0
while True:
    d=input('''Qua dificulade vc deseja ??
[1]facil
[2]medio
[3]Dificil\n''')
    dd=d.isnumeric()
    if dd == True:
        d=int(d)
        if d == 1:
            chances = 10
            break
        elif d == 2:
            chances = 7
            break
        elif d == 3:
            chances = 5
            break
        else:
            print("Valor invalido")
    else:
        print("Tem q ser numero")
            
while not ganhou and not perdeu:
    n=input("Digite um numero:\n")
    nn=n.isnumeric()
    if nn == True :
        n=int(n)
        if n in lista :
            print("voçe ja inseriu esse numero")

        else:
            if n == numero:
                print("Voce ganhou")
                ganhou=True

            elif n > numero:
                print("Numero maior que o numero secreto")

            elif n < numero :
                print("Numero menor que o numero secreto")

        if chances == 0:
            print("Voce perdeu")
            perdeu = True

    else:
        print("tem que ser um numero")