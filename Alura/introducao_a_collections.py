from abc import ABCMeta,abstractclassmethod
def a():
    idades = [19,17,78,21]
    print(f"mostrar os itens da lista atual:{idades}")

    idades.append(7)
    print(f"Adicionando a idade 7:{idades}")

    idades.remove(78)
    print(f'Removendo a idade 78:{idades}')

    print(f"O total  de itens na lista é :{len(idades)}")

    idades.insert(0,20)
    print(f"Adicionando a idade 20 na posição 0:{idades}")

    idades.extend([9,27])
    print(f"Adicionando as idades 9 e 19 ao mesmo tempo:{idades}")

    idades_ano_q_vem = [idade+1 for idade in idades]
    print(f"Adicionando um ano as idades:{idades_ano_q_vem}")

    se = [idade for idade in idades if idade < 20]
    print(f"Mostrando apenas as idades menores q 20:{se}")
   
    #Objetos Próprios
def b():
    class ContaCorrente:
        def __init__(self,codigo):
            self.codigo = codigo
            self.saldo = 0
        
        def deposita(self,valor):
            self.saldo += valor
        
        def __str__(self):
            return f"[>> Codigo {self.codigo} saldo:{self.saldo} <<]"

    gui  = ContaCorrente(17)
    dani = ContaCorrente(90)
    dani.deposita(1000)
    gui.deposita(500)

    contas = [dani,gui]

    def deposita_para_todas(contas):
        for conta in contas:
            conta.deposita(100)

    deposita_para_todas(contas)
    print(contas[0],contas[1])
    conta_do_gui = (15,1000)

    def deposita(conta):#separando o comportamento dos dados
        novo_saldo = conta[1] + 100
        codigo = conta[0]
        return (codigo,novo_saldo)

    print(conta_do_gui)
    conta_do_gui = deposita(conta_do_gui)
    print(conta_do_gui)

    usuarios = [("Guilherme",37,1981),("Daniele",31,1987),("Paulo",39,1979)]
    #Não posso mudar a tupla mas posso mudar um valor dela
    contas2 = (gui,dani)
    contas2[0].deposita(300)
    print(contas2[0])

    #Herença e Polimofismo
from operator import attrgetter
def c():
    class Conta(metaclass=ABCMeta):
        def __init__(self,codigo):
            self._codigo = codigo
            self._saldo = 0
        
        def deposita(self,valor):
            self._saldo += valor
        @abstractclassmethod

        def passa_o_mes(self):
            pass

        def __str__(self):
            return f"codigo:{self._codigo} saldo:{self._saldo}"


    class ContaCorrente(Conta):
        def passa_o_mes(self):
            self._saldo -=2


    class ContaPoupança(Conta):
        def passa_o_mes(self):
            self._saldo *=1.01
            self._saldo -= 3


    class ContaInvestimento(Conta):
        pass


    conta16 = ContaCorrente(16)
    conta16.deposita(1000)
    conta16.passa_o_mes()
    print(conta16)

    conta17 = ContaPoupança(16)
    conta17.deposita(1000)
    conta17.passa_o_mes()
    print(conta17)

    contas = [conta16,conta17]
    for conta in contas:
        conta.passa_o_mes() #duck typing
        print(conta)

    #igualdade
def d():
    class ContaSalario:
        def __init__(self,codigo):
            self._codigo = codigo
            self._saldo = 0
        
        def deposita(self,valor):
            self._saldo +=valor

        def __eq__(self,outro):
            return self._saldo == outro._saldo

        def __str__(self):
            return f"codigo:{self._codigo} saldo:{self._saldo}"


    conta1 = ContaSalario(17)
    conta2 = ContaSalario(17)
    conta1.deposita(1000)

    #Enumerate e desacoplando tuplas
def e():
    idades = [17,17,15,87,65,56,49,37]
    l = list(enumerate(idades))
    #print(l)
    #for indice,idade in enumerate(idades):
    #    print(indice,":",idade)
    usuarios =[
        ("Guilherme",37,1981),
        ("Daniele",31,1987),
        ("PV",19,2003)
    ]
    for nome,idade,nacimento in usuarios:
        print(f"seu nome é:{nome} e sua idade é:{idade}")
        
    #Ordem decrecente e cresente
def f():
    lista = [1,2,3,4,5,6,7,8,9]
    print(sorted(lista,reverse=True))#Não modifica a lisa      
    print(sorted(lista))#Não modifica a lisa  

    lista.reverse()#modifica a lista
    print(lista)
    lista.sort()#modifica a lista
    print(lista)

    #Ordem natural das Strings
def g(): 
    nomes = ["PV","David","Ana","alisson"]
    nomes.sort()#organiza em ordem alfabetica e as palavras em forma tem preferencia
    print(nomes)

    #Definir a ordem das contas parte:01
def h():   
    class ContaSalario:
        def __init__(self,codigo):
            self._codigo = codigo
            self._saldo = 0
            
        def deposita(self,valor):
            self._saldo +=valor

        def __eq__(self,outro):#verificar se o codigo de um é igual a outro
            return self._codigo == outro._codigo
        
        def __lt__(self,outro):#verificar se um é maior que o outro
            return self._saldo < outro._saldo

        def __str__(self):
            return f"codigo:{self._codigo} saldo:{self._saldo}"


    conta1 = ContaSalario(1)
    conta1.deposita(2000)

    conta2 = ContaSalario(200)
    conta2.deposita(1000)

    conta3 = ContaSalario(3)
    conta3.deposita(1000)

    contas=[conta1,conta2,conta3]

    #for conta in sorted(contas, reverse=True):
    #    print(conta)

    for conta in sorted(contas, key = attrgetter("_saldo","_codigo")):
        print(conta)
    
    #Definir a ordem das contas parte:02
def i():
    class ContaSalario:
        def __init__(self,codigo):
            self._codigo = codigo
            self._saldo = 0
                
        def deposita(self,valor):
            self._saldo +=valor

        def __eq__(self,outro):#verificar se o codigo de um é igual a outro
            return self._codigo == outro._codigo
            
        def __lt__(self,outro):#verificar se um é maior que o outro
            if self._saldo != outro._saldo:
                return self._saldo < outro._saldo
            else:
                return self._codigo < outro._codigo

        def __str__(self):
            return f"codigo:{self._codigo} saldo:{self._saldo}"


    conta1 = ContaSalario(1)
    conta1.deposita(1500)

    conta2 = ContaSalario(200)
    conta2.deposita(1000)

    conta3 = ContaSalario(3)
    conta3.deposita(1000)

    contas=[conta1,conta2,conta3]

    for conta in sorted(contas):
        print(conta)
   
    #Definir a ordem das contas parte:03
from functools import total_ordering
def j():
    @total_ordering
    class ContaSalario:
        def __init__(self,codigo):
            self._codigo = codigo
            self._saldo = 0
                    
        def deposita(self,valor):
            self._saldo +=valor

        def __eq__(self,outro):#verificar se o codigo de um é igual a outro
            return self._codigo == outro._codigo
                
        def __lt__(self,outro):#verificar se um é maior que o outro
            if self._saldo != outro._saldo:
                return self._saldo < outro._saldo
            else:
                return self._codigo < outro._codigo

        def __str__(self):
            return f"codigo:{self._codigo} saldo:{self._saldo}"


    conta1 = ContaSalario(1)
    conta1.deposita(1500)

    conta2 = ContaSalario(200)
    conta2.deposita(1000)

    conta3 = ContaSalario(1700)
    conta3.deposita(1000)

    contas=[conta1,conta2,conta3]

    if conta3 <= conta3:
        print(True)
    else:
        print(False)