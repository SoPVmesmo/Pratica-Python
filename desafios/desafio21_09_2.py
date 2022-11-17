
n1=input("Digite um numero: ")
n2=input("Digite outro numero :")
o=input("vc desejar somar,dividir,multiplicar ou subtrair: ")

if n1.find(".") == True or n2.find(".") == True:
    n1 = float(n1)
    n2 = float(n2)
else:
    n1 = int(n1)
    n2 = int(n2)

if o == "somar":
    ope=n1+n2

if o == "dividir":
    ope=n1/n2

if o == "multiplicar":
    ope=n1*n2

if o == "subtrair":
    ope=n1 - n2

if ope % 2 == 1:
    p_i="Inpar"
else:
    p_i="Par"

if ope > 0:
    p_n="Positivo"
else:
    p_n="Negativo"

if type(ope) == int:
    a = "Inteiro"
else:
    a = "Decimal"

print("O resultado da operação é:{} ele é {} , {} e {}".format(ope,p_i,p_n,a))

sem=["Sábado","Domingo","Segunda","Terça","quarta","Quinta","Sexta"]
n3=int(input("Digite um numero que esteja de 0 a 6 sendo domindo 1 e sabado 0: "))

while n3 < 0 or n3 > 6:
    print("Numero invalido")
    n3=int(input("Digite um numero que esteja de 0 a 6: "))
else:
    dia=sem[n3]
    print(dia)