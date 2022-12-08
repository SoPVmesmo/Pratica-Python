"""
#crie uma classe Livro que possui os atributos: nome,qtdPaginas,autor e preço.
#-crie os metodos getPreco para obter o valor do preco e o metodo setPreco para
#setar um novo valor do preço. (encapsulamento)
#Crie um codigo de teste.
# """
class Livro:
    def __init__(self,nome,qtdpaginas,autor,preco):
        self._nome = nome 
        self.qtdpaginas = qtdpaginas
        self._autor = autor
        self._preco = preco

    def get_preco(self):
        return self._preco
    
    def set_preco(self,novo_preco):
        if type(novo_preco) == int or type(novo_preco) == float and novo_preco > 0:
            self._preco = novo_preco
        else:
            print("O novo preço tem que ser um numero real maior ou igual a 0")


#l=Livro("pv",123,"pv",10)
#l.set_preco(12)
#print(l.get_preco())


class animais:
    def __init__(self,nome,mamifero):
        self.numero_de_patas=4
        self.nome = nome
        self.mamifero = mamifero


class cachorro:
    def __init__(self,):