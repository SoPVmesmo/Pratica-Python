#este programa gera e imprime os numeros primos entre 2
#e n, escolhendo pelo usuario, usando o algoritmo chamado
#de "crivo de eratosstenes"
num = int( input("Digite um numero:"))
conj = set(list(range(2,num+1)))
for i in range(2,num+1):
    conj -= set(range(i * 2,num+1,i))
print(conj)