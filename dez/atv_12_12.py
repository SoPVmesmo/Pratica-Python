#Lembrando que:
# snake_case para variáveis, funções e métodos;
# PascalCase para classes;
#============================================================
# Crie um ambiente O.O. completo utilizando classes e métodos:
# Na classe Livraria sub-classes Revista e Livro sabemos que:
# atributos: nome, Número de páginas, Idioma, Editora, tipo e status
# todos atributos encapsulados fortemente
# métodos para:
# controlar o aluguel dos livros, calculo do aluguel em (07)dias
# controlar a venda dos livros
# OBS: Lembre-se de fazer os GETs e SETs
# OBS: Não esqueça das validações
# OBS: Sempre que acontecer um aluguel ou venda diminuir do estoque.
# OBS: Faça a impressão dos elementos
import re
import datetime
class Livralia:
    def __init__(self):
        self.__tipo = None
        self.__status = None
        self.estoque = 5
        self.pagar_a = 0
        self.pagar_v = 0
        self.a = 0

    @property
    def tipo(self):
        return self.__tipo
        
    @tipo.setter
    def tipo(self,novo_tipo):
        if novo_tipo.isalpha() == True:
            self.__tipo = novo_tipo
        else:
            print("O novo tipo tem que ser uma String")
    
    def valor(self,aluguel,venda):
        if type(aluguel) == float and type(venda) == float:
            self.pagar_a += aluguel
            self.pagar_v += venda
        else:
            print("os valores tem que ser numericos!!!")

    def controlar_aluguel(self,data_retirada,data_entrega):
        if self.estoque == 0:
            print("Esse livro/revista não esta mais disponivel")
        else:
            padrao =re.compile("[0-3][0-9][/][0-2][0-9][/][2][0][2][2]")
            verficacao1 = padrao.search(data_retirada)
            verficacao2 = padrao.search(data_entrega)
            if verficacao1 and verficacao2:
                dia1 = int(data_retirada[0:2])
                mes1 = int(data_retirada[3:5])
                ano1 = int(data_retirada[6::])
                dia2 = int(data_entrega[0:2])
                mes2 = int(data_entrega[3:5])
                ano2 = int(data_entrega[6::])
                entrega = datetime.date(ano1,mes1,dia1)
                retirada = datetime.date(ano2,mes2,dia2)
                e = entrega.day
                r = retirada.day
                a = r - e
                a = int(a)
                self.a = a

            else:
                print("Valor incorreto")
            

    def calculo_aluguel(self):
        if self.a > 7:
            print("voce excedeu o prazo de entrega ira pagar a mais de acordo com os dias")
            atraso = self.a - 7
            atraso = atraso * (self.pagar_a * 0.1)
            print(f"Valor a pagar {self.pagar_a + atraso}")
        else:
            print(f"Valor a pagar {self.pagar_a}")
        

    def venda_dos_livros(self,valor):
        if self.estoque == 0:
            print("N temos mais esse livro/revista")
        else:
            if self.pagar_v != 0:
                if valor == self.pagar_v:
                    print(f"Voce comprou {self.__nome} por R${self.pagar_v}")
                    self.estoque -= 1
                elif valor > self.pagar_v:
                    troco = valor - self.pagar_v
                    print(f"Voce comprou {self._Livro__nome} no valor:R${self.pagar_v} e recebeu de troco:R${troco}")
                    self.estoque -= 1
                else:
                    print("Valor incorreto")
            else:
                print("Esse livro/revista n pode ser vendido")

    def venda_das_revistas(self,valor):
        if self.estoque == 0:
            print("N temos mais esse livro/revista")
        else:
            if self.pagar_v != 0:
                if valor == self.pagar_v:
                    print(f"Voce comprou {self.__nome} por R${self.pagar_v}")
                    self.estoque -= 1
                elif valor > self.pagar_v:
                    troco = valor - self.pagar_v
                    print(f"Voce comprou {self._Revista__nome} no valor:R${self.pagar_v} e recebeu de troco:R${troco}")
                    self.estoque -= 1
                else:
                    print("Valor incorreto")
            else:
                print("Esse livro/revista n pode ser vendido")

    def impressão(self):
        return print(f'''O livro/revista de nome:{self._Livro__nome}
com {self._Livro__numero_de_paginas} paginas 
no idioma:{self._Livro__idioma} e editora:{self._Livro__editora} 
ainda tem a quantidade de estoque:{self.estoque}''')
    
class Livro(Livralia):
    def __init__(self, nome, numero_de_paginas, idioma, editora):
        self.__nome = nome.title()
        self.__numero_de_paginas = numero_de_paginas
        self.__idioma = idioma.title()
        self.__editora = editora.title()
        self.__tipo = None
        self.__status = None
        self.estoque = 5
        self.pagar_a = 0
        self.pagar_v = 0
        self.a = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,novo_nome):
        if novo_nome.isalpha() == True:
            self.__nome = novo_nome.title()
        else:
            print("O nome tem que ser uma String")

    @property
    def numero_de_pagina(self):
        return self.__nome
        
    @numero_de_pagina.setter
    def numero_de_pagina(self,qtd_paginas):
        if qtd_paginas.isnumeric() == True:
            self.__numero_de_paginas = qtd_paginas
        else:
            print("A quantidade de paginas tem que ser int")

    @property
    def idioma(self):
        return self.__idioma
        
    @idioma.setter
    def idioma(self,novo_idioma):
        if novo_idioma.isalpha() == True:
            self.__idioma = novo_idioma.title()
        else:
            print("O idioma tem que ser uma String")

    @property
    def editora(self):
        return self.__editora
        
    @editora.setter
    def editora(self,nova_editora):
        if nova_editora.isalpha() == True:
            self.__editora = nova_editora.title()
        else:
            print("A nova editora tem que ser uma String")

class Revista(Livralia):
    def __init__(self, nome, numero_de_paginas, idioma, editora):
        self.__nome = nome.title()
        self.__numero_de_paginas = numero_de_paginas
        self.__idioma = idioma.title()
        self.__editora = editora.title()
        self.__tipo = None
        self.__status = None
        self.estoque = 5
        self.pagar_a = 0
        self.pagar_v = 0
        self.a = 0
        
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,novo_nome):
        if novo_nome.isalpha() == True:
            self.__nome = novo_nome.title()
        else:
            print("O nome tem que ser uma String")

    @property
    def numero_de_pagina(self):
        return self.__nome
        
    @numero_de_pagina.setter
    def numero_de_pagina(self,qtd_paginas):
        if qtd_paginas.isnumeric() == True:
            self.__numero_de_paginas = qtd_paginas
        else:
            print("A quantidade de paginas tem que ser int")

    @property
    def idioma(self):
        return self.__idioma
        
    @idioma.setter
    def idioma(self,novo_idioma):
        if novo_idioma.isalpha() == True:
            self.__idioma = novo_idioma.title()
        else:
            print("O idioma tem que ser uma String")

    @property
    def editora(self):
        return self.__editora
        
    @editora.setter
    def editora(self,nova_editora):
        if nova_editora.isalpha() == True:
            self.__editora = nova_editora.title()
        else:
            print("A nova editora tem que ser uma String")

hp=Livro("Harry Potter",600,"pt-br","JK")
hp.valor(7.0,45.0)
hp.controlar_aluguel("13/12/2022","21/12/2022")
hp.calculo_aluguel()
hp.venda_dos_livros(50.0)
hp.impressão()