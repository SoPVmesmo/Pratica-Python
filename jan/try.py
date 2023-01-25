#seleciona :Ctrl + ; comentar tudo
#seta pra cima enter roda novamente o codigo
#Ctrl + D seleciona mais de uma palavra
try:
    print(2+"pv")
except TypeError:
    print("ops deu erro")

try:
    print(2+2)
except TypeError:
    print("ops deu erro")

try:
    print(x)
except:
    print("Variavel x não esta definada")
finally:
    print("O try except esta finalizado")

try:
    print("hello")
except:
    print("not hello")
else:
    print("hello "*2)