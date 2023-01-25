# Q01
# lista_compras = [
#     {"descrição":"Água","preço":2.00},
#     {"descrição":"Leite","preço":3.00},    
#     {"descrição":"Carne","preço":18.00},
#     {"descrição":"Pizza","preço":9.00},
#     {"descrição":"Chocolate","preço":6.50}
# ]
# lista_com_imposto = list(map(lambda x:{"descrição":x["descrição"] ,
# "preço":x["preço"] + x["preço"] * 0.10 },lista_compras))

# for i in lista_com_imposto:
#     print("Descrição :{}, Preço :{:.2f}".format(i["descrição"],i["preço"]))

# Q02
# numeros = set()
# for i in range(5):
#     n = int(input(f"Digite o {i+1} numero:\n"))
#     numeros.add(n)

# minimo = min(numeros)
# maximo = max(numeros)

# min_max = lambda x,y : {"max":x * 2, "min":y * 3}
# print(min_max(maximo,minimo))

# maior_q_20 = list(filter(lambda x: x > 20, numeros))
# print(f" maiores que 20:{maior_q_20}")

# Q03
# lista_com_imposto = sorted(lista_com_imposto, key =lambda x: x["preço"])

# print(f"O item com menor valor é:{lista_com_imposto[0]} e o item com maior valor é:{lista_com_imposto[len(lista_com_imposto)-1]}")