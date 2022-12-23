import re
padrao_cpf = re.compile("[0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2}")
cpf=input("Digite seu cpf:\n")
verificacao = padrao_cpf.search(cpf)

if verificacao:
    print(f"seu cpf {verificacao.group()} é valido!!!")
else:
    raise ValueError("Seu cpf n é valido")


numero = input ("digite um numero entre 0 e 9:\n")
padrao_numero = re.compile("[0-9]")
match = padrao_numero.match(numero)

if not match:
    print(f"{numero} ñ é um numero de 0 a 9,Deu Ruim")
else:
    raise ValueError(f"{match.group()} é um numero entre 0 e 9,Deu Bom")



p = re.compile("[^1234]*@")#O primeiro numero n pode ser de 1 a 4 e o segundo pode ser qualquer coisa o ultimo tem que ser @
a="6_@"
v=p.search(a)
if v:
    print(v.group())
else:
    raise ValueError("Erro")