aqv=open("palavras.txt","r")
lista=[]
for linha in aqv:
    linha=linha.strip()
    lista.append(linha)
aqv.close()
print(lista)