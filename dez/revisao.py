class ListaCustomizada:
    def __init__(self,lista = None):
        if lista is None:
            self.lista = []
        else:
            self.lista = lista

    def __len__(self):
        print(f"O numero de itens na lista é {len(self.lista)}")
        return len(self.lista)
    
    def __getitem__(self,index):
        print(f"O item no index {index} é {self.lista[index]}")
        return self.lista[index]

    def __setitem__(self,index,valor):
        if index <= len(self.lista):
            print(f"O item de index {index} foi modificado de {self.lista[index]} para {valor}")
            self.lista[index] = valor
        else:
           print("o index foi maior que o numero de itens da lista!!!")
    
    def __contains__(self,valor):
        if valor in self.lista:
            print(f"O item {valor} esta dentro da lista")
        else:
            print(f"O item {valor} não esta dentro da lista")

    def append(self,valor):
        self.lista.append(valor)
        print(f"Foi adicionado o item '{valor}', sua lista atualizada é {self.lista}")

    def __add__(self,outra_lista):
        print(f"Duas listas foram juntas a lista {self.lista} com {outra_lista.lista}")
        return  ListaCustomizada(self.lista + outra_lista.lista)

    def __repr__(self):
        return str(self.lista)

minha_lista = ListaCustomizada()
minha_lista.append(1)
minha_lista.append(2)
minha_lista.append(3)
minha_lista.append(4)
minha_lista.append(10)

len(minha_lista)#quantos itens existes na minha lista
minha_lista[3]#verificar o item na posição 4
minha_lista[4] = 5 #trocando o valor da posição 5 por 5
print(minha_lista)#mostrando minha lista
3 in minha_lista#verificando se se um item ta na lista

outra_lista = ListaCustomizada()
outra_lista.append(6)
outra_lista.append(7)
lista3 = minha_lista + outra_lista
print(lista3)
print(lista3 + minha_lista)