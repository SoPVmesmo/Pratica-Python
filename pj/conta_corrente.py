from random import randint
from ast import Num
from unittest import result
valor_emprestimo = 0
saldo=0
deposito=0
saque=0
def conta_corrente():
    n_conta=randint(100000,999999)
    n_cliente=randint(100000,999999)
    saldo=valor_emprestimo + deposito - saque
    return saldo