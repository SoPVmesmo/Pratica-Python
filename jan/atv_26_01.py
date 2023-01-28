import re
with open("arquivos_txt/dom_casmuro.txt") as dom:
    palavras = dom.read()
    palavra = input("Digite uma palavra:\n")
    padrao = re.compile("[a-z]{3,20}")
    verificacao = padrao.search(palavra)
    if verificacao:
        lista = re.findall(r"\b" + palavra + r"\b", palavras)
        if len(lista)  != 0:
            print(f"\033[0;32m A palavra {palavra} existe no texto e apareceu:{len(lista)} vezes\033[0;0m")
        else:
            print(f"A palavra {palavra}\033[1;34m não existe no texto \033[0;0m")
    else:
        print("\033[1;31m A palavra tem que ter no minimo 3 a 20 caracteres e não pode ter numeros!!\033[0;0m")