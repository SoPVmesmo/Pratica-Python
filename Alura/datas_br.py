from datetime import datetime,timedelta
class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()
    
    def mes_cadastro(self):
        meses_do_ano =[
            "janeiro","fevereiro","março","abril","maio",
            "junnho","julho","agosto","setembro","outubro",
            "novembro","dezembro"
        ]
        mes_castro = self.momento_cadastro.month
        return meses_do_ano[mes_castro - 1].title()
    
    def dia_semana(self):
        dia_semana_lista = ["segunda","terça","quarta",
        "quinta","sexta","sabado","domingo"]
        dia_semana = self.momento_cadastro.weekday()
        return dia_semana_lista[dia_semana].title()

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada
    
    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days = 30)) - self.momento_cadastro
        return tempo_cadastro

    def __str__(self):
        return self.format_data()