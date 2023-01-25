dici = {}
lista = []
with open("arquivos_txt/notas.txt","r",encoding = "utf8") as arquivo:
    linhas=arquivo.readlines()
    for i,notas in enumerate(linhas):
        nota = notas.replace("\n", "").split(":")
        dici[float(nota[1])] = nota[0] 

for i in dici.keys():
    lista.append(i)
lista.sort(reverse= True)

for i in lista:
    print(dici[i],":",i)

# file = open("arquivos_txt/notas.txt")
# linhas = file.readlines()
# dici = {}
# lista = []

# for i,notas in enumerate(linhas):
#     nota = notas.replace("\n", "").split(":")
#     dici[float(nota[1])] = nota[0]
# file.close()

# for i in dici.keys():
#     lista.append(i)
# lista.sort(reverse= True)

# for i in lista:
#     print(dici[i],":",i)