class Pessoa:
    def __init__(self,cpf,nome,idade,genero):
        self._cpf = cpf
        self._nome = nome.title()
        self.idade = idade 
        self.genero = genero.title()
       
    def get_cpf(self):
        return self._cpf
    
    def get_genero(self):
        return self.genero
    
    def get_nome(self):
        return self._nome
    
    def set_nome(self,novo_nome):
        n = self._nome
        if type(novo_nome) == str:
            self._nome = novo_nome.title()
            print(f"Nome mudado de {n} para {self._nome}")
        else:
            print("Nome tem que ser uma string!!")

    def get_idade(self):
        return self.idade
    
    def set_idade(self,nova_idade):
        i = self.idade
        if type(nova_idade) == int:
            self.idade = nova_idade
            print(f"Idade mudada de {i} para {self.idade} anos")
        else:
            print("A idade tem que ser um numero inteiro!!")
    
    nome=property(get_nome,set_nome)


class Aluno(Pessoa):
    def __init__(self,serie,cpf,nome,idade,genero):
        super().__init__(cpf,nome,idade,genero)
        self.__notas = []
        self.__media = 0
        self.serie = serie 

    
    def notas(self):
        cont = 1
        while len(self.__notas) != 6:
            nota =input(f"Digite a {cont} nota:\n")
            try:
                nota = float(nota)
            except:
                print("A nota tem que ser um numero real")
                continue
            if nota >= 0 and nota <= 10:
                self.__notas.append(nota)
            else:
                print("Nota invalida")
                continue

            cont += 1

    def get_notas(self):
        return self.__notas
    
    def get_media(self):
        for n in self.__notas:
            self.__media += n
        self.__media = self.__media/6
        return self.__media

    def dar_meio_ponto(self):
        self.__media += 0.5
        return self.__media

    def descricao(self):
        return print(f"Nome do aluno:{self._nome} de cpf:{self._cpf} com a idade:{self.idade} e genero:{self.genero} da serie:{self.serie}")


class Professor(Pessoa):
    def __init__(self,cpf,nome,idade,genero,materias):
        super().__init__(cpf,nome,idade,genero)
        self.materias = materias.title()

    def get_materias(self):
        return self.materias

    def set_materias(self,nova_materia):
        if  type(nova_materia) == str:
            self.materias.title()
        else:
            print("A materia tem que ser uma String")
    
    def descricao(self):
        return print(f"Nome do Professor:{self._nome} de cpf:{self._cpf} com a idade:{self.idade} e genero:{self.genero} com a materia:{self.materias}")


aluno1 = Aluno("2 ano","123.455.213-50","pv",19,"masculino")
aluno1.descricao()
professor1=Professor("123.432.213-70","paulo",32,"masculino",'programação')
professor1.descricao()
professor1.set_idade(30)
professor1.descricao()