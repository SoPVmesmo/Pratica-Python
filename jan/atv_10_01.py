#nomes = input("x y").split()
#print(nomes)

#criar file valores.txt 15.000 7.500 1.000
#criar um cod que leia os valores de valores.txt 
#implemente um novo arquivo 
#chamado pagamentos.txt com a seguinte extrututa bidimensional:
#nome:valor
#solicite os 3 nomes dos funcionarios
valor=open("arquivos_txt/valores.txt","r")
pag =open("arquivos_txt/pagamentos.txt","w")
cont = 1
visu={}
for linha in valor:
    nome=input(f"Digite o {cont} nome:\n")
    pag.write(f"{nome}:{linha}")
    visu[nome]=linha
    cont +=1
print(visu)
valor.close()
pag.close()