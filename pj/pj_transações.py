from random import randint    
from ast import Num
from unittest import result
from cliente import *
from conta_corrente import *
from meus_depositos import *
from meus_emprestimos import *
from saque import *
while True: 
   n=input('''
   deseja ser cliente?
   [1]sim
   [2]não
   ''')
   if n== '1':
        cadastro()
        cc=input('''
   deseja criar uma conta corrente?
   [1]Sim
   [2]Não
   ''')
        if cc == '1':
            conta_corrente()
            w=input('''
    O que voçê deseja fazer na sua conta ?
    [1]Depositar
    [2]Sacar
    [3]nenhum
    ''')
            if w =='1':
                depos()
                break
            elif w == '2':
                saque()
                break
            elif 2 == '3':
                break
            else:
                print("valor invalido")
        elif cc== '2':
                d=input('''
            deseja depositar?
            [1]sim
            [2]não
            ''')
            
                if d == '1':
                    depos()
                    conta_corrente()

                elif d == '2':
                    e=input('''
            deseja fazer um emprestimo?
            [1]sim
            [2]não
            ''')
                if e == '1':
                    emprestimo()
                    conta_corrente()
                    saldo()
                else:
                    break
                
   elif n == '2':
            p=input('''
        O que voce deseja?
    [1]Depositar
    [2]Emprestimo
    [3]nenhum
    ''')
            if p == '1':
                cb=input("Digite o numero da conta")
                depos()
                break
            elif p == '2':
                print("Necessario ser cliente para realizar o emprestimo")
                a=input('''
        Deseja ser cliente?
    [1]sim
    [2]não
    ''')
                if a == '1':
                    cadastro()
                    emprestimo()
                break
            else:
                print("Operação encerrada")
                break
   else:
        print("Opçao invalida")