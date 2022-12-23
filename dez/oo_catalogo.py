#Lembrando que:
# snake_case para variáveis, funções e métodos;
# PascalCase para classes;
#============================================================
# Crie um ambiente O.O. completo utilizando classes e métodos conforme abaixo:
# fazer com que os contatos sejam armazenados F
# validar o CPF para Pessoa Física V
# validar CNPJ para pessoa Jurídica V
# montar a agenda dos contatos em formato de lista. F
# utilizar os métodos mágicos.
# implemente as nomenclaturas dos atributos e métodos.
# OBS: Utilize expressões regulares
# OBS: Faça todas as validações
# OBS: Fique atento aos impedimentos dos métodos
# OBS: Faça a impressão dos elementos
import re
class CatalogoContatos:
    def __init__(self,nome,idade,numero):
        self.nome = nome.title()
        self.idade = idade
        self.numero = numero
    
    def __str__(self):
        if self.__class__.__name__ == "CatalogoPessoaFisica":
            return f"Nome:{self.nome} cpf:{self.cpf} idade:{self.idade} numero:{self.numero}"

        elif self.__class__.__name__ == "CatalogoPessoaJuridica":
            return f"Nome:{self.nome} cnpj:{self.cnpj} idade:{self.idade} numero:{self.numero}"

        else:
            return f"Nome:{self.nome} idade:{self.idade} numero:{self.numero}"


class CatalogoPessoaFisica(CatalogoContatos):
    def __init__(self, nome, idade, numero,cpf):
        super().__init__(nome, idade, numero)
        self.cpf = cpf
    
    def verificar_cpf(self):
        padrao_cpf = re.compile("[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}")
        verificar = padrao_cpf.search(self.cpf)
        if verificar:
            return self.cpf
        else:
            raise ValueError('Formato de cpf invalido!!!')
    

class CatalogoPessoaJuridica(CatalogoContatos):
    def __init__(self, nome, idade, numero,cnpj):
        super().__init__(nome, idade, numero)
        self.cnpj = cnpj

    def verificar_cnpj(self):
        padrao_cnpj = re.compile("[0-9]{2}.[0-9]{3}.[0-9]{3}/000[1-2]-[0-9]{2}")
        verificar = padrao_cnpj.search(self.cnpj)
        if verificar:
            return self.cnpj
        else:
            raise ValueError('Formato de cnpj invalido!!!')
    
            
class Agenda():
    def __init__(self,lista = None):
        if lista is None:
            self.lista = []
        else:
            self.lista = lista

    def __len__(self):
        print(f"O numero de contatos na lista é {len(self.lista)}")
        return len(self.lista)
    
    def __getitem__(self,index):
        print(f"O contato de index {index} é {self.lista[index]}")
        return self.lista[index]

    def __setitem__(self,index,valor):
        if index <= len(self.lista):
            print(f"O contato de index {index} foi modificado de {self.lista[index]} para {valor}")
            self.lista[index] = valor
        else:
           raise ValueError("o index foi maior que o numero de itens da lista!!!")
    
    def __contains__(self,valor):
        if valor in self.lista:
            print(f"O item {valor} esta dentro da lista")
        else:
            raise ValueError(f"O item {valor} não esta dentro da lista")

    def append(self,valor):
        self.lista.append(valor)
        print(f"Foi adicionado o contato '{valor}', sua lista atualizada é {self.lista}")

    def __add__(self,outra_lista):
        print(f"Duas listas foram juntas a lista {self.lista} com {outra_lista.lista}")
        return  Agenda(self.lista + outra_lista.lista)

    def __repr__(self):
        return str(self.lista)


pv = CatalogoPessoaFisica("paulo victor",19,"91234-5678","123.456.789-17")
pv.verificar_cpf()
print(pv)

kay = CatalogoPessoaJuridica("kayden",31,"93229-5173","17.123.456/0001-17")
kay.verificar_cnpj()
print(kay)

lista=["Nome:paulo victor idade:19 anos numero:91234-5678 Cpf:123.456.789-17","Nome:kayden Idade:31 anos numero:93229-5173 Cnpj:17.123.456/0001-17"]
lista_de_contatos = Agenda(lista)
print(lista_de_contatos)