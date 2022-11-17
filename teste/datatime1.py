from datetime import datetime

print('A DATA E O HORÁRIO\nESTÃO ATUALIZADOS!\n')
#fuso_horario = int(input('Digite o fuso horário: \n|'))

data_atual  = datetime.now()
dia         = data_atual.day
mes         = data_atual.month
ano         = data_atual.year
hora        = data_atual.hour # fuso_horario - data_atual.hour
minutos     = data_atual.minute
segundos    = data_atual.second

print("DATA: {:02}/{:02}/{}".format(dia, mes, ano))
print("HORÁRIO: {:02}:{:02}:{:02}".format(hora, minutos, segundos))

if(hora >= 5 and hora <= 12):
    print('BOM DIA!')
elif(hora >= 13 and hora <= 17):
    print('BOA TARDE!')
elif(hora >= 18 and hora <= 23):
    print('BOA NOITE!')
else:
    print('ESTÁ NA HORA DE DORMIR!\n')