# Faça a verificação de cada funcionário para aplicar o valor de desconto no valor de salario de cada um. Crie um novo arquivo com os funcionários e os novos salários.
# fun = {}
# with open("arquivos_txt/funcionarios.txt", "r", encoding = "utf-8") as funcionarios:
#     lista_funcionarios = funcionarios.readlines()
#     for i in lista_funcionarios:
#         i = i.replace("\n","").split(":")
#         if float(i[1]) > 1200 :
#             desconto =lambda x: x - (x * 0.13)
#             n = desconto(float(i[1]))
#             fun[i[0]] = n
#         else:
#             desconto =lambda x: x - (x * 0.07)
#             n = desconto(float(i[1]))
#             fun[i[0]] = n

# with open("arquivos_txt/novo_salario.txt" , "w" , encoding= "utf-8") as salario:
#     for f,s in fun.items():
#         salario.write(f"{f}:{s}" + "\n")


# fun = {}
# with open("arquivos_txt/funcionarios.txt", "r", encoding = "utf-8") as funcionarios:
#     lista_funcionarios = funcionarios.readlines()
#     for i in lista_funcionarios:
#         i = i.replace("\n","").split(":")
#         n = float(i[1])
#         desconto = (n - (n * 0.13))if n > 1200 else (n - (n * 0.07))
#         fun[i[0]] = desconto

# with open("arquivos_txt/novo_salario.txt" , "w" , encoding= "utf-8") as salario:
#     for f,s in fun.items():
#         salario.write(f"{f}:{s}" + "\n")


with open("arquivos_txt/descontos.txt" ,"r", encoding="utf-8") as desconto:
    des = desconto.readlines()
    valores = []
    descontos = []
    for i in des:
        i = i.replace("\n","").split(":")
        valores.append(i[0])
        descontos.append(i[1])

fun = {}
with open("arquivos_txt/funcionarios.txt", "r", encoding = "utf-8") as funcionarios:
    lista_funcionarios = funcionarios.readlines()
    for i in lista_funcionarios:
        i = i.replace("\n","").split(":")
        n = float(i[1])
        desconto = (n - n * (float(descontos[0])/100)) if n > float(valores[1]) else (n - (n * float(descontos[1])/100))
        fun[i[0]] = desconto

with open("arquivos_txt/novo_salario.txt" , "w" , encoding= "utf-8") as salario:
    for f,s in fun.items():
        salario.write(f"{f}:{s}" + "\n")
