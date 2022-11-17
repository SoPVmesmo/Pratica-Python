class Aluno:
    def __init__(self):
        self.__nome=input("Digite o nome do Aluno:\n")
        self.__n1=float(input("Digite a 1 nota:\n"))
        self.__n2=float(input("Digite a 2 nota:\n"))
        self.__n3=float(input("Digite  a 3 nota:\n"))
        self.__n4=float(input("Digite a 4 nota:\n"))

    @property
    def media(self):   
        media =(self.__n1 + self.__n2 + self.__n3 + self.__n4)/4
        return media

    @property
    def passou(self):
        media=self.media
        if  media >= 6.0:
            print("O aluno {} passou com a nota {:02}".format(self.__nome,self.media))
        else:
            print("O aluno {} ficou reprovado por {:02}  pontos".format(self.__nome,6 - self.media))
            
aluno1=Aluno()
aluno1.media
aluno1.passou