'''
Implemente uma classe que represente o aluno de uma academia.
Os atributos são: identificador, nome, idade, peso e altura.
Os métodos são:
· Um construtor com parâmetros
· Um método get e um método set para cada atributo devidamente encapsulados
· Um método para calcular o IMC do aluno, sabendo-se que IMC=peso/altura^2 float calcularIMC( )
· Um método para imprimir a ficha do aluno os atributos.
'''
class Aluno:
    def __init__(self,identificador,nome,idade,peso,altura):
        self._identificador = identificador
        self._nome = nome.title()
        self._idade = idade 
        self._peso = peso
        self._altura = altura 
        

    def get_identificador(self):
        return self._identificador

    def identificador(self,novo_identificador):
        if type(novo_identificador) == int:
            self._identificador = novo_identificador
        else:
            print("valor do identificador invalido")
    
    def get_nome(self):
        return self._nome
    
    def set_nome(self,novo_nome):
        if type(novo_nome) == str:
            self._nome = novo_nome.title()
        else:
            print("O nome tem que ser uma string!!")
    
    def get_idade(self):
        return self._idade
    
    def set_idade(self,nova_idade):
        if type(nova_idade) == int:
            self._idade = nova_idade
        else:
            print("A idade tem que ser um numero inteiro!!")
    
    def get_peso(self):
        return self._peso
    
    def set_peso(self,novo_peso):
        if type(novo_peso) == float or type(novo_peso) == int:
            self._peso = novo_peso
        else:
            print("O peso tem que ser um numero real!!")
    
    def get_altura(self):
        return self._altura

    def set_altura(self,nova_altura):
        if nova_altura == float or type(nova_altura) == int:
            self._altura = nova_altura
        else:
            print("A altura tem que ser um numero real")

    def calcular_IMC(self):
        IMC = self._peso/(self._altura**2)
        return IMC

    def ficha(self):
        print(f"Nome do aluno:{self._nome} com identificador:{self._identificador} de idade:{self._idade} com altura de {self._altura} e peso {self._peso} ")


aluno1 =Aluno(17,"pv",19,71,1.8)
aluno1.ficha()