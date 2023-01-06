import re
from collections import Counter,defaultdict
import random
class Conta:
    def __init__(self,nome,idade,cpf):
        self.__nome = nome.title()
        self.__idade = idade
        self.__cpf = cpf
        self.__id=random.randrange(0,100)
    
    def verificacao_cpf(self):
        padrao_cpf =re.compile("[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}")
        verificar = padrao_cpf.match(self.__cpf)
        if verificar:
            return print('CPF valido!!!')
        else:
            raise ValueError("Formato de cpf invalido!!!")
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,novo_nome):
        if novo_nome.isalpha() == True:
            self.__nome = novo_nome.title()
        else:
            raise ValueError("O novo nome tem que ser uma String")
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self,nova_idade):
        if nova_idade.isalpha() == True:
            self.__idade = nova_idade
        else:
            raise ValueError("A idade tem q ser um numero inteiro maior que 0")
    
    @property
    def cpf(self):
        return self.__cpf

    @property
    def id(self):
        return self.__id


class ListadeClientes:
    def __init__(self,lista = None):
        if lista == None:
            self.lista = []
        else:
            self.lista = lista


pv=Conta("paulo victor",19,"123.456.789-17")
print(pv.id)
print(pv.nome) 
print(pv.idade) 
print(pv.cpf)    
pv.verificacao_cpf() 