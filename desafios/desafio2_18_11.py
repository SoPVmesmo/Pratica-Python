'''
Um código orientado a objeto que represente três tipos de bolachas: comuns, normais e especiais.
Elas são vendidas na camada estadual, nacional e importada respectivamente.
Os atributos são: descrição, valor, peso do pacote, taxa, taxa importação (verifique qual objeto recebe cada atributo).
Utilize herança

Os métodos são:
· Um construtor com parâmetros
· Um método get e um método set para cada atributo
· Um método para calcular as taxas'''
class Bolacha:
    def __init__(self,descricao,valor,peso):
        self._descricao = descricao
        self._valor = valor
        self._peso = peso
    
    def get_descricao(self):
        return self._descricao

    def set_descricao(self,nova_descricao):
        if type(nova_descricao) == str:
            self._descricao = nova_descricao
        else:
            print("A descrição tem que ser uma String!!")
    
    def get_valor(self):
        return self._valor

    def set_valor(self,novo_valor):
        n=novo_valor.isnumeric()
        if n == True: 
            self._valor = novo_valor
        else:
            print("O valor tem que ser um numero real!!")
    
    def get_peso(self):
        return self._valor

    def set_peso(self,novo_peso):
        p=novo_peso.isnumeric()
        if p == True:
            self._valor = novo_peso
        else:
            print("O peso tem que ser um numero real!!")
            
class Comuns(Bolacha):
    def __init__(self,descricao,valor,peso):
        super().__init__(descricao,valor,peso)
        self._taxa = 0


    def calcular_taxa(self):
        self._taxa = self._valor*(3/100)
        self._valor +=self._taxa
        return self._valor


class Normais(Bolacha):
    def __init__(self,descricao,valor,peso):
        super().__init__(descricao,valor,peso)
        self._taxa = 0
    def calcular_taxa(self):
        self._taxa = self._valor*(5/100)
        self._valor +=self._taxa
        return self._valor


class Especiais(Bolacha):
    def __init__(self,descricao,valor,peso):
        super().__init__(descricao,valor,peso)
        self._taxa_de_importacao = 0
        self._taxa = 0

    def calcular_taxa(self):
        self._taxa_de_importacao = self._valor*(15/100)
        self._valor +=self._taxa + self._taxa_de_importacao
        return self._valor


oreo=Especiais("abc",4,"240g")
print(oreo.calcular_taxa())

biscoito =Comuns("vds",1.80,"300g")
print(biscoito.calcular_taxa())

bolacha = Normais("qwe",2.5,"250g")
print(bolacha.calcular_taxa())