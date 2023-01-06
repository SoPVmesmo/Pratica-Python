txt = input("Digite um texto:\n")
vogais = {"a","e","i","o","u","A","E","I","O","U"}
cont = 0
for letra in txt:
    if letra in vogais:
        cont += 1
print(f"Total de vogais na frase:{cont}")