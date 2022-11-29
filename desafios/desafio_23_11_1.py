"""Implemente uma classe Aluno, que deve ter os  seguintes atributos: nome, curso, tempoSemDormir  (em horas).
Essa classe deverá ter os seguintes  métodos:
estudar (que recebe como parâmetro a qtd de horas de  estudo e acrescenta tempoSemDormir )
dormir (que recebe como parâmetro a qtd de horas de  sono e reduz tempoSemDormir )
Crie um código de teste da classe, criando um objeto da classe aluno e usando os métodos estudar e dormir.
Ao final imprima quanto tempo o aluno está sem  dormir"""
from datetime import datetime
class Aluno:
    def __init__(self,nome,curso,tempoSemDormir):
        self._nome = nome.title()
        self._curso = curso
        self.tempoSemDormir = tempoSemDormir

    def estudar(self,horas_de_estudo):
        if type(horas_de_estudo) == int:
            horas_de_estudo +=  self.tempoSemDormir
        else:
           raise ValueError("valor invaido")
        return horas_de_estudo
    
    def dormir(self,horas_de_sono):
        if type(horas_de_sono) == int:
            horas_de_sono += self.tempoSemDormir
        else:
           raise ValueError("valor invaido")
        return horas_de_sono

pv=Aluno("pv","back-end",10)
print(pv.estudar(5))
print(pv.dormir(8))