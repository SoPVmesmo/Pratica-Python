class Cliente:
    def __init__(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        print("chamando @property nome")
        return self.__nome.title()

    @nome.setter
    def nome(self,nome):
        print("Chamando setter nome")
        self.__nome = nome

cliente1=Cliente("PV")
cliente1.nome