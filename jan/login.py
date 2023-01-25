import os 

def add_usuario(usuario,senha):
    novo_usuario = open("arquivos_txt/login.txt","a")
    novo_usuario.write(usuario+":"+senha+"\n")
    novo_usuario.close()
    return None

arquivo_n_existe = os.path.isfile("arquivos_txt/login.txt")#verifica se o arquivo existe

if arquivo_n_existe != True:
    usuario = input("Digite o nome de usuario:\n")
    senha = input("Digite a senha de acesso:\n")
    add_usuario(usuario,senha)
else:
    arquivo_vazio = os.stat("arquivos_txt/login.txt").st_size == 0 #verificando se o file ta vazio
    if arquivo_vazio:
        usuario = input("Digite o nome de usuario:\n")
        senha = input("Digite a senha de acesso:\n")
        add_usuario(usuario,senha)
        
    arquivo = open("arquivos_txt/login.txt")
    linhas = arquivo.readlines()
    usuario = input("Informe seu usuario:\n")
    senha = input("Informe sua senha:\n")

    for i,linha in enumerate(linhas):
        nova_linha = linha.replace("\n","").split(":")
        if usuario == nova_linha[0] and senha == nova_linha[1]:
            print("Dados OK! sistema acessada com Sucesso")
            break
        elif i+1 == len(linhas) and usuario != nova_linha[0]:
            arquivo.close()
            add_usuario(usuario,senha)
            print("Novo usuario cadastrado")
            break
        else:
            acesso = 0
            if usuario == nova_linha[0]:
                acesso += 1
            if senha == nova_linha[1]:
                acesso += 1
            if  acesso == 1:
                print("Usuario ou senha incorreto!!")
                break
            else:
                print("Verifique seus dados e tente novamente")
    arquivo.close()