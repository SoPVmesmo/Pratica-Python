class Aluno:
    def __init__(self):
        nome=input("Digite o nome do Aluno:\n")
        while True:
            try:
                n =float(input("Digite a 1 nota:\n"))
            except:
                print("Valor invalido")
                continue
            try:
                n2=float(input("Digite a 2 nota:\n"))
            except:
                print("Valor invalido")
                continue
            try:
                n3=float(input("Digite a 3 nota:\n"))
            except:
                print("valor invalido")
                continue
            try:
                n4=float(input("Digite a 4 nota:\n"))
            except:
                print("Valor inavlido")
                continue
            break

        self.nome=nome
        self.n=n
        self.n2=n2
        self.n3=n3
        self.n4=n4
        self.media=(n+n2+n3+n4)/4

aluno1=Aluno()
aluno2=Aluno()
aluno3=Aluno()
aluno4=Aluno()

m=aluno1.media
nome=aluno1.nome

m2=aluno2.media
nome2=aluno2.nome

m3=aluno3.media
nome3=aluno3.nome

m4=aluno4.media
nome4=aluno4.nome
aprovados=[]
reprovados=[]

class Passou:
    def __init__(self,m,nome):
        self.m=m
        self.nome=nome
        if m >= 6:
            print(f"{nome} passou com a nota {m}")
            aprovados.append(nome)
        else:
            print(f"{nome} reprovado com a nota {m}")
            reprovados.append(nome)

m1=Passou(m,nome)
m2=Passou(m2,nome2)
m1=Passou(m3,nome3)
m2=Passou(m4,nome4)

print(f"Lista dos aprovados {aprovados}")
print(f"Lista dos reprovados {reprovados}")