class Programa:
    def __init__(self,nome,ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
                
    @property  
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,novo_nome):
        self._nome = novo_nome.title()

    def dar_like(self):
        self._likes += 1


class Filme(Programa):
    def __init__(self,nome,ano,duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes "


class Serie(Programa):
    def __init__(self,nome,ano,temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes "


class Playlist:
    def __init__(self,nome,programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self,item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas
    
    @property
    def tamanho(self):
        return len(self._programas)


vingadores=Filme("vingadores",2018,160)
tmep = Filme("todo mundo em pânico",1999,100)
demolidor = Serie("demolidor",2016,2)
atlanta=Serie("atlanta",2018,2)

atlanta.dar_like()
vingadores.dar_like()
vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()

filmes_e_series = [vingadores,atlanta,demolidor,tmep]
fim_de_semana = Playlist("Fim de semana",filmes_e_series)

print(fim_de_semana.tamanho)

for programa in fim_de_semana:
    print(programa)