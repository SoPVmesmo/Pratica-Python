def corta_vogal(informacao):
    informacao.lower()
    vogais="aeiou"
    for i in range(len(vogais)):
        informacao=informacao.replace(vogais[i],"")
    print(informacao)
corta_vogal(input("Digite sua palavra ou frase"))

l=[]
contador=[]
def reps():
    while len(l) < 6:
        x=input("Digite uma letra ou numero\n")
        l.append(x)
        if l.count(x) >= 2:           
            contador.append(x)
reps()
print("sua lista é ",l)
print("sua lista com apenas os numeros repetidos são ",contador)

""" outro metodo
l=[]
contador=[]
n=int(input("Digite quantos item serão adicionados a lista\n"))
def reps():
    while len(l) < n:
        x=input("Digite uma letra ou numero\n")
        l.append(x)
        if l.count(x) >= 2:           
            contador.append(x)
reps()
print("sua lista é ",l)
print("sua lista com apenas os numeros repetidos são ",contador)
"""