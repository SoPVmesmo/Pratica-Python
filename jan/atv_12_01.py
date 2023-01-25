aqv = open("arquivos_txt/O_Valor_do_Tempo.txt","r", encoding="UTF-8")
linha = aqv.readline()
lista = []
txt = ""
while linha != "":
    txt += linha
    lista += linha.split()
    linha = aqv.readline()
conj = set()
for i in lista:
    if lista.count(i) >= 2:
        conj.add(i)

conj.remove("a")
conj.remove("o")
for i in conj:
    txt = txt.replace(i,"")
print(txt)