import re 
with open("arquivos_txt/contatos.txt","r",encoding="utf-8") as file:
    conj = set()
    numeros = file.readlines()
    for i in numeros:
        i = i.replace("\n", "").split(":")
        conj.add(i[1])

with open("arquivos_txt/novos_contatos.txt","w",encoding="utf-8") as novo:
    for i in conj:
        if re.search("-", i):
            novo.write(f"{i}:fixo" + "\n")
        else:
            novo.write(f"{i}:celular" + "\n")