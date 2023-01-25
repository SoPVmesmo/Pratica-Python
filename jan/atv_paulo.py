def segundo_item(item):
    return item[1]

nova_lista = []
altera_tipo = []
with open("arquivos_txt/notas.txt", "r", encoding="utf8") as notas:
    lista_notas = notas.readlines()
    for linha in lista_notas:
        nova_linha = linha.replace('\n', '').split(':')
        altera_tipo = (nova_linha[0] , float(nova_linha[1]))
        nova_lista.append(altera_tipo)
    print( sorted(nova_lista, key = segundo_item, reverse = True))