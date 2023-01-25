#Uma classe chamada MeuIntervalo para armazenar inteiros no intervalo de 0 a 99.
#Uma classe chamada MeusInteiros que herda de MeuIntervalo ela deve ser capaz
#de gerar uma lista aleatória de inteiros. 
#Ela deve gerar também uma lista do mesmo tamanho de >>> MeuIntervalo <<<,
#nela deve conter a lista de booleanos referentes a comparação da lista
#MeuIntervalo com MeusInteiros onde para cada elemento do intervalo que
#estiver na lista coloque true e para cada que não existir coloque falso
#O construtor sem argumento inicializa as listas como vazias. 
#Todos os métodos mágicos devem ser implementador e também deve implemente os seguintes métodos: 
#• Método para unir duas listas V
#• Método para fazer a interseção de duas litas V
#• Método para inserir um novo elemento na lista V 
#• Método para deletar um inteiro da lista V
#• Método para string onde retorna uma lista em formato de string separados por " - ". V
#• Método para verificar de duas listas são iguais; V
#• Método para limpar uma lista V
import random
class MeuIntervalo:
    def __init__(self):
        self.lista = []

    def intersecao(self,outra):
        lista_iguais = []
        for i in range(len(self.lista)):
            if self.lista[i] in outra:
                lista_iguais.append(self.lista[i])
        print(f"A interseção das listas é {lista_iguais}")

    def lista_em_str(self,lista = None):
        if lista == None:
            lis = self.lista
        else:
            lis = lista
        lis = str(lis)
        lis = lis.replace("[","")
        lis = lis.replace("]","")
        lis = lis.replace(",","-")
        print(f"A lista em str com as modificações fica assim:\n{lis}")
        return lis

    def __len__(self):
        print(f" A quantidade de valores na lista é :{len(self.lista)}")
        return len(self.lista)

    def __getitem__(self,index):
        if index < len(self.lista) and index >= 0:
            return f"{self.lista[index]}"
        else:
            print(f"O index {index} não existe na lista!!")
    
    def __setitem__(self,index,valor):
        if index < len(self.lista) and index >= 0:
            print(f"O valor de index:{index} mudou de {self.lista[index]} para {valor}")
            self.lista[index] = valor
        else:
            print("index maior que que a lista ou menor que 0")

    def __contains__(self,valor):
        if valor in self.lista:
            print(f"O valor {valor} existe na lista")
        else:
            print(f"O valor {valor} não existe na lista")
    
    def append(self,valor):
        if valor < 100 and valor > 0 and type(valor) == int:
            print(f"O item {valor} foi adicionado na lista")
            self.lista.append(valor)
        else:
            print("O valor tem que ser entre 1 e 99")
    
    def pop(self,index):
        if index < len(self.lista) and index <= 0:
            self.lista.pop(index)
        else:
            print(f"O index {index} n existe na lista")

    def limpar_lista(self):
        print("a lista foi Limpa!!")
        self.lista.clear()

    def __add__(self,outra):
        print(f"A lista {self.lista} foi junta com a lista {outra}")
        return self.lista + outra
    
    def __eq__(self,outra):
        if self.lista == outra:
            print("As listas são iguais")
        else:
            print("As listas não são iguis")
        return self.lista == outra
    
    def __repr__(self):
        return str(self.lista)


class MeusInteiros(MeuIntervalo):
    def __init__(self):
        super().__init__()
        self.lista2 = []
    
    def gerar_lista(self):
        lista_b = []
        while len(self.lista2) != len(self.lista):
            self.lista2.append(random.randrange(1,100))
        for i in range(len(self.lista2)):
            if self.lista2[i] in self.lista:
                lista_b.append("True")
            else:
                lista_b.append("False")
        print(f"Lista aleatoria gerada:\n{self.lista2}")
        print(f"Lista de bool:\n{lista_b}")


lista = MeusInteiros()
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)
lista.append(6)
lista.append(7)
lista.append(8)
lista.append(9)
lista.append(10)
lista.gerar_lista()