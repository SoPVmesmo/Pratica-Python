nome_sobrenome=[]
while True:
    nome=[input("Digite seu nome \n")]
    sobrenome=[input("Digite seu sobrenome \n")]
    nome_sobrenome.append(nome + sobrenome)
    x=input("Deseja adicionar mais ? sim ou não \n")
    if x == "sim" or x ==  "Sim" or x ==  "SIM":
        continue
    elif x == "Não" or x ==  "não" or x ==  "NÃO":
        break
    else:
        while True: 
            if x != "Não" or x != "não" or x != "NÃO" or x != "sim" or x != "Sim" or x != "SIM":
                print("Erro de digitação")
                x=input("Deseja adicionar mais ? sim ou não \n")          
                if x == "sim" or x == "Sim" or x == "SIM":
                    y=0
                    break
                elif x == "Não" or x == "não" or x == "NÃO":
                    y=1
                    break
    if y == 1:
        break
print(nome_sobrenome)

def soma_de_3n(x,y,z):
    return print("a soma dos 3 numeros é:",x+y+z)
soma_de_3n(1,2,3)

n1=int(input("Digite um numero:\n"))
n2=int(input("Digite outro numero:\n"))
n3=int(input("Digite o ultimo numero:\n"))
soma_de_3n(n1,n2,n3)