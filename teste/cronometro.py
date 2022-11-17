import time
print("Bem vindo, oque deseja fazer ?")
while True:
    i=input('''
Digite:
[1]cronometro
[2]contagem regressiva 
[3]sair\n''')

    ii=i.isnumeric()
    if ii == True:
        i=int(i)
        if i == 1:
            
            for n in range(1,101):
                print(n)
                time.sleep(1)

        elif i == 2 :
            n=input("Digite quantos seguntos sera a contagem\n")
            nn=n.isnumeric()
            if nn == True:
                n=int(n)
                for i in range(1,n+1):
                    print(i)
                    time.sleep(1)
            else:
                print("Valor invalido")

        elif i == 3 :
            print("Obrigado pela presença")
            break
        
        else:
            print("*Valor invalido*\n")
    else:

        print("*Valor invalido*\n")