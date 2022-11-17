class Pessoa:
    def __init__(self,nome,cpf,idade,sexo,cargo):
        self.__nome = nome.title()
        self.__cpf = cpf
        self.idade = idade
        self.sexo = sexo.title()
        self.__cargo = cargo.title()
     
    def get_nome(self):
        return self.__nome
    
    def set_nome(self,novo_nome):
        n = self.__nome
        if type(novo_nome) == str:
            self.__nome = novo_nome
            print(f"Nome mudado de {n} para {self.__nome}")
        else:
            print("O nome tem que ser uma string")

    def get_cpf(self):
        return self.__cpf
    
    def get_idade(self):
        return self.__idade
    
    def set_nome(self,nova_idade):
        i = self.idade
        if type(nova_idade) == int:
            self.idade = nova_idade
            print(f"Idade mudado de {i} para {self.idade}")
        else:
            print(" A idade tem que ser um numero inteiro")

    def get_sexo(self):
        return self.sexo
    
    def get_cargo(self):
        return self.__cargo
    
    def set_nome(self,novo_cargo):
        n = self.__cargo
        if type(novo_cargo) == str:
            self.__cargo = novo_cargo
            print(f"Cargo mudado de {n} para {self.__cargo}")
        else:
            print("O nome tem que ser uma string")
    
    def __str__(self):
        return f"Nome:{self.__nome} cpf:{self.__cpf} idade:{self.idade} sexo:{self.sexo} cargo:{self.__cargo}"

    nome = property(get_nome,set_nome)