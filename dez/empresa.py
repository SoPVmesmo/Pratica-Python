#Lembrando que:
# snake_case para variáveis, funções e métodos;
# PascalCase para classes;
#============================================================
# Crie um ambiente O.O. completo utilizando classes e métodos:
# Crie uma super classe RelogioDePonto, uma subclasse Funcionarios e uma sub-subclasse Operador e Repositor:
# trabalhe com os atributos: hora_entrada, hora_saida, nome, matricula, expediente, ocorrencia 
# todos atributos encapsulados OK
# defina uma correta dsitribuição dos atributos entre as classes
# defina as nomenclaturas dos metodos e com base na explicação abaixo faça:
# você deve fazer os funcionários registrem a entrada e a saida com base no seu expediente
# você informar caso ele entre atrasado ou saia adiantado e mostrar quanto foi esse atraso ou adiantamento
# caso o atraso seja maior que 10 minutos registre uma ocorrencia
# OBS: Lembre-se de fazer os GETs e SETs
# OBS: Não esqueça das validações
# OBS: Faça a impressão dos elementos corretamente
import re
import random 
from datetime import timedelta,time
class RelogioDePonto:

    def get_entrada(self):
        return self._entrada

    def set_entrada(self,novo_horario):
        padrao =re.compile("[0-2][0-9][:][0-5][0-9]")
        verificacao = padrao.search(novo_horario)
        if verificacao:
            minutos = novo_horario[3::]
            minutos =  int(minutos)
            hora = novo_horario[0:2]
            hora = int(hora)
            entrada = minutos + self.converte_horas_a_minutos(hora)
            self._entrada = entrada
        else:
            print("O formato de horario esta incorreto")
    
    def get_saida(self):
        return self._saida

    def set_saida(self,novo_horario):
        padrao =re.compile("[0-2][0-9][:][0-5][0-9]")
        verificacao = padrao.search(novo_horario)
        if verificacao:
            minutos = novo_horario[3::]
            minutos =  int(minutos)
            hora = novo_horario[0:2]
            hora = int(hora)
            saida = minutos + self.converte_horas_a_minutos(hora)
            self._saida = saida
        else:
            print("O o formato de horario esta incorreto")

    def converte_horas_a_minutos(self,horas):
        mi = horas * 60
        return mi
    def __str__(self):
        return f"Voce entrou as {timedelta(minutes = self.get_entrada())} e saiu as {timedelta(minutes = self.get_saida())}"
    entrada = property (get_entrada,set_entrada)
    saida = property (get_saida,set_saida)


class Funcionario(RelogioDePonto):
    def __init__(self,nome):
        self.__nome = nome.title() 
        self._matricula = random.randrange(0,101)
        self._ocorrencia = 0
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,novo_nome):
        if novo_nome.isalpha() == True:
            self._nome = novo_nome.title()
        else:
            print("O nome tem que ser uma String")

    def get_expediente_entrada(self):
        return  self._expediente_entrada

    def set_expediente_entrada(self,novo_horario):
        padrao =re.compile("[0-2][0-9][:][0-5][0-9]")
        verificacao = padrao.search(novo_horario)
        if verificacao:
            minutos = novo_horario[3::]
            minutos =  int(minutos)
            hora = novo_horario[0:2]
            hora = int(hora)
            entrada = minutos + self.converte_horas_a_minutos(hora)
            self._expediente_entrada = entrada
        else:
            print("O formato de horario esta incorreto") 

    def get_expediente_saida(self):
        return self._expediente_saida

    def set_expediente_saida(self,novo_horario):
        padrao =re.compile("[0-2][0-9][:][0-5][0-9]")
        verificacao = padrao.search(novo_horario)
        if verificacao:
            minutos = novo_horario[3::]
            minutos =  int(minutos)
            hora = novo_horario[0:2]
            hora = int(hora)
            saida = minutos + self.converte_horas_a_minutos(hora)
            self._expediente_saida = saida
        else:
            print("O formato de horario esta incorreto")

    def gerar_ocorrencia(self):
        atraso = self._entrada - self._expediente_entrada
        cedo = self._expediente_saida - self._saida
        if atraso > 10:
            print(f"Voce se atrasou {atraso} e gerol uma ocorrencia")
            self._ocorrencia +=1
        if cedo > 10:
           print(f"Voce saiu {cedo} mais cedo e isso gerol uma ocorrencia") 
           self._ocorrencia +=1

    expediente_entrada = property (get_expediente_entrada, set_expediente_entrada)
    expediente_saida = property (get_expediente_saida, set_expediente_saida)

    def __str__(self):
        return f"Ola {self.__nome} com matricula:{self._matricula} sua função é {self.__class__.__name__} seu expediente é {timedelta(minutes = self._expediente_entrada)} das {timedelta(minutes = self._expediente_saida)} e voce entrou as {timedelta(minutes = self._entrada)} e saiu as {timedelta(minutes = self._saida)} voce tem atualmente:{self._ocorrencia} ocorrencias"


class Operador(Funcionario):
    def __init__(self, nome):
        super().__init__(nome)


class Repositor(Funcionario):
    def __init__(self, nome):
        super().__init__(nome)


pv = Repositor("paulo victor")
pv.expediente_entrada = "08:00"
pv.expediente_saida = "14:00"
pv.entrada = "08:10"
pv.saida = "14:00"
pv.gerar_ocorrencia()
print(pv)
