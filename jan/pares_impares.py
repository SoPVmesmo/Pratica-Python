lista = []
with open("arquivos_txt/pares.txt","r", encoding="utf-8") as pares:
    ler = pares.readline()
    while ler != "":
        lista.append(int(ler))
        ler = pares.readline()

with open("arquivos_txt/impares.txt","r", encoding="utf-8") as impares:
    ler = impares.readline()
    while ler != "":
        lista.append(int(ler))
        ler = impares.readline()

lista.sort()
with open("arquivos_txt/pareseimpares.txt","a", encoding = "utf-8") as file:
    for i in lista:
        file.write(f"{i}"+"\n")