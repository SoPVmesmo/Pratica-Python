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
        self.lista = [self._identificador]

    def get_identificador(self):
        return self._identificador

    def set_identificador(self,novo_identificador):
        if type(novo_identificador) != int: 
            print("O identificador tem que ser um numero inteiro!!")
        else:
            if novo_identificador in self.lista:
                print("Esse identificador ja existe!!")
            else:
                self._identificador = novo_identificador

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,novo_nome):
        if type(novo_nome) == str:
            self._nome = novo_nome.title()
        else:
            print("O nome tem que ser uma String") 
    
    def get_idade(self):
        return self._idade
    
    def set_idade(self,nova_idade):
        if type(nova_idade) == int and nova_idade > 0:
            self._idade = nova_idade
        else:
            print("A idade tem que ser um numero inteiro positivo!!") 
    
    @property
    def peso(self):
        return self._peso
    
    @peso.setter
    def peso(self,novo_peso):
        if type(novo_peso) == float or type(novo_peso) == int and novo_peso > 0:
            self._peso = novo_peso
        else:
            print("O peso tem que ser um numero positivo")
    
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self,nova_altura):
        if type(nova_altura) == float or type(nova_altura) == int and nova_altura > 0:
            self._altura = nova_altura
        else:
            print("A altura tem que ser um numero valido positivo!!")
   
    identificador = property(get_identificador,set_identificador)
    idade = property()
    idade = idade.getter(get_idade)
    idade = idade.setter(set_idade)


aluno1 = Aluno(17,"pv",19,63,1.80)

print(aluno1.altura)
aluno1.altura = 1.85
print(aluno1.altura)