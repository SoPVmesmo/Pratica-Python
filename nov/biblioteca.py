class Livro:
    def __init__(self,id,nome,autor,genero):
        self.__id = id 
        self.__nome = nome.title()
        self.__autor = autor.title()
        self.genero = genero.title()

    def get_id(self):
        return print(self.__id)

    def get_nome(self):
        return print(self.__nome)
    
    def set_nome(self,novo_nome):
        n=self.__nome

        if type(novo_nome) == str:
            self.__nome = novo_nome.title()
            print(f"nome mudado de {n} para {self.__nome}")
        else:
            print("O novo tem que ser uma string!!")

    def get_genero(self):
        return self.genero
    
    def set_genero(self,novo_genero):
        g=self.genero
        if type(novo_genero) == str:
            self.genero = novo_genero.title()
            print(f"Genero do livro mudado de {g} para {self.genero}")
        else:
            print("O nome tem que ser uma string")
    
    def get_autor(self):
        return self.__autor
    
    def set_autor(self,novo_autor):
        a=self.__autor
        if type(novo_autor) == str:
            self.__autor = novo_autor.title()
            print(f"nome do autor mudado de {a} para {self.__autor}")
        else:
            print("O nome tem que ser uma string")

    nome = property(get_nome,set_nome)
    autor = property(get_autor,set_autor)

    def __str__(self):
        return f" id:{self.__id} Nome:{self.__nome} de autor:{self.__autor} de genero:{self.genero}"

livro1 = Livro(17,"a volta dos que não foram","pv","comedia")
