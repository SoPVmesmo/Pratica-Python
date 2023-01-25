#Q01
# leitura = open('arquivos_txt/valida.txt',"r", encoding="utf-8")
# leitura.seek(4)#pega a partir desse ponto
# print(leitura.read(5))#ler essa quantidade de caracteres

# pegar o arquivo ips.txt retirar o primeiro octeto de cada ip
# e mostrar em tela os mesmos ordenados
# classifique os ips que não são validos.(ips acima de 254)

# with open("arquivos_txt/ips.txt","r",encoding="utf-8") as file:
#     lista = []
#     ler = file.readline()
#     while ler != "":
#         posicao_ponto = ler.find(".")
        
#         lista.append(int(ler[:posicao_ponto]))
#         ler = file.readline()

# lista.sort()
# for i in lista:
#     if i > 254:
#         print(f"{i} - invalido")
#     else:
#         print(f"{i} - valido")

# Forma do Paulo
# nova_lista = []
# with open("arquivos_txt/ips.txt","r",encoding="utf-8") as meus_ips:
#     lista_ips = meus_ips.readlines()
#     for linha in lista_ips:
#         nova_linha = linha.replace("\n", "").split(".")
#         del nova_linha[3]
#         del nova_linha[2]
#         del nova_linha[1]
#         muda_tipo = int(nova_linha[0])
#         nova_lista.append(muda_tipo)
#         nova_lista.sort()
# print(nova_lista)

# Q02
# pegar a lista de nomes e mostrar um apelido para o nome utilizando 3 consoantes do mesmo
# vogais = {"a","e","i","o","u","y","w"}
# with open("arquivos_txt/lista_nomes.txt","r",encoding="utf-8") as file:
#     ler = file.readlines()
#     for l in ler:
#         l = l.replace("\n","")
#         n = l
#         l = l.lower()
#         for v in vogais:
#             l = l.replace(v,"")
#         l = l.strip()
#         if len(l) < 3:
#             print(f"{n} - Invalido")
#         elif len(l) == 3:
#             print(n," - " ,l)
#         else:
#             print(n," - ",l[:3])

#Forma do Paulo
# consoantes = {"b","c","d","f","g","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"}
# nomes = []
# convertido = {}
# apelido = {}
# with open("arquivos_txt/lista_nomes.txt","r",encoding="utf-8") as meus_nomes:
#     lista_nomes = meus_nomes.readlines()
#     for linha in lista_nomes:
#         nova_linha = linha.replace("\n", "").lower()
#         corta_linha = list(nova_linha)
#         convertido = set(corta_linha)
#         apelido = convertido.intersection(consoantes)#intersection:retorna a singularidade de 2 conjuntos
#         if len(apelido) == 3:
#             nomes.append(str(apelido))
#         elif len(apelido) >= 4:
#             apelido.remove(list(apelido)[0])
#             nomes.append(str(apelido))
#     print("\n".join(map(str,nomes)))

# consoantes = {"b","c","d","f","g","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"}
# with open("arquivos_txt/lista_nomes.txt","r",encoding="utf-8") as file:
#     ler = file.readlines()
#     for i in ler:
#         i = i.replace("\n", "")
#         i = i.lower()
#         apelido = list(filter(lambda x:x in consoantes , i))
#         if len(apelido) < 3:
#             print(i," - Invalído")
#         else:
#            print(f"{i} - {apelido[0]}{apelido[1]}{apelido[2]}")