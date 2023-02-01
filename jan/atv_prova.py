# • peça para o usuário criar um dicionário com 10 frutas e o preço do quilo. V
# • imprima o dicionário completo V
# • imprima só os valores V
# • imprima os itens com o mesmo valor de preço(se existir)   V
# • faça uma promoção e altere o valor de duas frutas para 1/3 V
# • insira duas novas frutas e seus preços V
# • salve o dicionário em um arquivo V
# • mostre qual fruta mais cara V
# • apague o dicionário V
import random
dici = {}
cont = 1
while len(dici) != 10:
    fruta = input(f"Digite a {cont} fruta:\n")
    try:
        valor = float(input(f"Digite o valor do quilo da:{fruta}\n"))
    except:
        print("O valor da fruta tem que ser um numero real!!")
        continue
    cont += 1
    dici[fruta] = valor

for f,v in dici.items():
    print(f"{f}:{v}")

for i in dici.values():
    print(i)

lista = []
conj = set()
for i in dici.values():
    for n,v in dici.items():
        if i == v:
            t = f"{n}:{v}"
            lista.append(t)

for i in lista:
    if lista.count(i) > 1:
        conj.add(i)
        
if len(conj) != 0:
    print(f"itens de valores iguais:{conj}")

# frutas = dict(maça = 3.0, banana = 2.0, morango = 17.0, melancia = 2.0, uva = 17.0)
# frutas_duplicada = {}
# for i,j in frutas.items():
#     frutas_duplicada.setdefault(j, set()).add(i)

# print(frutas_duplicada)
# resultado =  [print(j,":",i) for i , j in frutas_duplicada.items() if len(j) > 1]

for i in range(2):
    fruta, valor = random.choice(list(dici.items())) # pegar item aleatorio
    dici[fruta] = valor - valor * 0.33
    print(f"A fruta:{fruta} ficou em promoçao!! seu quilo agora é {dici[fruta]:.2f}")
    
for i in range(2):
    fruta = input(f"Adicione a {i + 1} fruta:\n")
    try:
        valor = float(input(f"Digite o valor do quilo da:{fruta}\n"))
    except:
        print("O valor da fruta tem que ser um numero real!!")
        continue
    dici[fruta] = valor

with open("arquivos_txt/frutas.txt", "w" , encoding= "utf8") as fruta:
    for f,v in dici.items():
        fruta.write(f"{f}:{v:.2f}" + "\n")

x = max(dici, key = (lambda k: dici[k])) # pegar o item de maior valor
print(f"O item de maior valor é {x} custando o quilo:{dici[x]}")

dici.clear() # apagar o dicionario