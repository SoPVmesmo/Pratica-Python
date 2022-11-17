import random
print("*"*26)
print("Bem vindo ao jogo da forca")
print("*"*26)
arquivo= open("palavras.txt","r")
lista=[]
for linha in arquivo:
    linha=linha.strip()
    lista.append(linha)
arquivo.close()
numero=random.randrange(0,len(lista))
palavra=lista[numero].upper()
letras_acertadas=["_"*len(palavra)]
letras=[]
ganhou=False
perdeu=False
erros=0
index=0
print(letras_acertadas)
while not ganhou and not perdeu:
    chute=("Digite uma letra")
    c=chute.isalpha()
    if c == True:
        chute=chute.upper()
        if chute in letras:
            print("voçê ja inseriu essa letra tente outra")
        else:
            letras.append(chute)
            if chute in palavra:
                for letra in palavra:
                    if chute  == letra:
                        print(f"A letra {chute} existe na palavra secreta")
                        letras_acertadas[index]=chute
                        print(letras_acertadas)
                    index=index + 1 
            else:
                    print(f"A letra {chute} não existe na palavra secreta")
                    erros=erros + 1

            if erros == 6:
                print(f"Voçê perdeu a palavra era {palavra}")
                perdeu=True

            if "_" not in letras_acertadas:
                print("Parabens voçê ganhou")
                ganhou=True
    else:
        print("tem que ser uma letra!!!")
