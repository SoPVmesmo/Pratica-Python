# O programa abaixo pede ao usuário que escolha um nome 
# de arquivo, existente em seu diretório, e exibe seu conteúdo 
# na tela.
def Q01():
    nome = input("Digite o nome do arquivo:\n")
    try:
        file = open(nome,"r")
        linha = file.readline()
        while linha != "":
            print(linha, end= "")
            linha = file.readline()
        file.close()
    except:
        print(f"O arquivo {nome} não existe!!")

# O programa abaixo cria um arquivo, chamado “pontos.txt”, com 30 pontos 
# bidimensionais (2D), com coordenadas aleatórias (x,y) no intervalo 0 a 400. Ao 
# final, mostra na tela o conteúdo do arquivo gerado
def Q02():
    from random import randrange
    file = open("arquivos_txt/pontos.txt","w")
    try:
        quantidade = int(input("Digite a quantidade de coordenadas que voçe deseja criar:\n"))
    except:
        print("O valor tem que ser um numero inteiro positivo!!")

    for i in range(quantidade):
        file.write(f"{randrange(0,401)}:{randrange(0,401)}" + "\n")
    file.close()

    file = open("arquivos_txt/pontos.txt","r")
    linha = file.readline()
    while linha != "":
        print(linha, end = "")
        linha = file.readline()
        
# O programa abaixo faz a leitura de um arquivo, chamado “pontos.txt”, com 
# pontos bidimensionais (2D), com coordenadas (x,y). Calcula e escreve o 
# centroide de todos os pontos lidos.
def Q03():
    pontos = 0 
    somay = 0 
    somax = 0

    file = open("arquivos_txt/pontos.txt","r")
    linha = file.readline()

    while linha != "":
        linha = linha.split(":")
        somax += float(linha[0])
        somay += float(linha[1])
        linha = file.readline()
        pontos +=1
    file.close()
    print(f"A soma dos x é:{somax}")
    print(f"A soma dos y é:{somay}")
    print(f"Os pontos são:{pontos}")

# Copiando um Arquivo Texto
def Q04():
    nome = input("Digite o nome do arquivo a ser copiado:\n")
    copia = input("Digite o nome do novo arquivo:\n")

    file = open(nome,"r")
    linha = file.readline()
    file2 = open(copia,"w")

    while linha != "":
        file2.write(linha)
        linha = file.readline()
    print("Arquivo copiado")

# Anexando uma Nova Linha ao
# Final de um Arquivo
def Q05():
    nome = input("Digite o nome do arquivo:\n")
    quantidade = int(input("Quantos linhas serão adicionadas?:\n"))
    file = open(nome,"a")
    for i in range(quantidade):
        file.write(input(f"Digite a {i+1} linha:\n") + "\n")