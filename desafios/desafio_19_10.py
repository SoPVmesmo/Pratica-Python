from random import randint
import time

def jogo_ped_pap_tes():
    print("=====================================")
    print("Bem Vindo ao jogo pedra,papel,tesoura")
    print("=====================================")
    f=0#var que que recebe o valor para entrar no if apos o while
    while True:
        x=input("Digite 1 para começar ou 2 para sair\n ")
        xx=x.isnumeric()#verificando se o valor é numerico
        if xx == True:
            x=int(x)#transformando em numero
            if x == 1 :
                t=1#var que recebe o valor para entrar no input escolha
                break
            elif x == 2:
                t=0
                print("======================")
                print("Obrigado pela presença")
                print("======================")
                break
            else:
                print("*valor invalido*\n")
        else:
            print("*valor invalido*\n")
    if t == 1:#if para continuar o jogo caso a var 't' tenha recebido 1 como valor

        while True:
            e=input('''Escolha:
[0]Pedra
[1]Papel
[2]Tesoura\n''')
            ee=e.isnumeric()
            if ee == True:

                e=int(e)
                lista=["Pedra","Papel","Tesoura"]

                if e != 0 and e != 1 and e !=2:
                    print("*Valor invalido*\n")

                else:
                    escolha=lista[e]
                    f=1
                    break

            else:
                print("*Valor invalido*\n")
                
    if f == 1:
        bot=randint(0,2)
        bot=lista[bot]
                    
        print("Pedra")
        time.sleep(1)#delay para contagem regressiva

        print("Papel")
        time.sleep(1)

        print("Tesoura")
        time.sleep(1)

        print("Seu adversario escolheu => ",bot,"\n")
        time.sleep(1.5)

        print(f"voce escolheu => {escolha}\n")
        time.sleep(1.5)

        if bot == "Pedra" and e == 0:
            print("Empate")

        elif bot == "Pedra" and e == 1:
            print("Voçê ganhou")

        elif bot == "Pedra" and e == 2:
            print("Voçê perdeu")

        elif bot == "Papel" and e == 0:
            print("Voçê perdeu")

        elif bot == "Papel" and e == 1:
            print("empate")

        elif bot == "Papel" and e == 2:
            print("Voçê ganhou")

        elif bot == "Tesoura" and e == 0:
            print("Voçê ganhou")

        elif bot == "Tesoura" and e == 1:
            print("Voçê perdeu")

        elif bot == "Tesoura" and e == 2:
            print("empate")
jogo_ped_pap_tes()

def cronometro():
    print("Bem vindo ao cronometro")
    while True:
        n=input("Digite 1 para começar ou 2 para sair\n")
        nn=n.isnumeric()
        if nn == True:
            n=int(n)
            if n == 1 :
                for i in range(6):
                    print(i)
                    time.sleep(1)
                break
            elif n == 2:
                print("Obrigado pela presença")
                break
            else:
                print("Valor invalido")
        else:
            print("Valor invalido")

def jogo():
    lista=["Pedra","Papel","Tesoura"]
    n=randint(0,2)
    bot=lista[n]
    escolha=int(input('''Escolha
[0]Pedra
[1]Papel
[2]Tesoura\n'''))
    escolha=lista[escolha]
    print(escolha)
    print(bot)
    if bot == "Pedra" and escolha == "Pedra":
        print("Empate")

    elif bot == "Pedra" and escolha == "Papel":
        print("voce ganhou")

    elif bot == "Pedra" and escolha == "Tesoura":
        print("voce perdeu")

    elif bot == "Papel" and escolha == "Pedra":
            print("Voce perdeu")

    elif bot == "Papel" and escolha == "Papel":
        print("empate")

    elif bot == "Papel" and escolha == "Tesoura":
        print("voce ganhou")

    elif bot == "Tesoura" and escolha == "Pedra":
        print("voce ganhou")

    elif bot == "Tesoura" and escolha == "Papel":
        print("voce perdeu")

    elif bot == "Tesoura" and escolha == "Tesoura":
        print("empate")