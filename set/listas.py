notas=[0,7,9,9,9,10,0,8.8,7,5,5]
notas.insert(1,7.5)
notas.remove(0)
notas.append(6)
print(notas)

#adicioanando 10 itens em uma lista sem poder repetir o item
v = []
while len(v) < 10:
    x = int(input("Escreva um numero: "))
    if x in v:
        print("Nao pode escrever esse numero.")
    else:
        v.append(x)
print(v)

#somando as notas, vendo a quantidade de notas e fazendo a media delas
sm_das_nts=sum(notas)
qtd_de_notas=len(notas)
media_das_notas=sm_das_nts/qtd_de_notas
print(media_das_notas)

#validando as notas (notas q são 0)
notas_validas = [nota for nota in notas if nota > 0]
print(notas_validas)

media_valida=sum(notas_validas)/len(notas_validas)
print(media_valida)

#contando quantos 7 e 9 tem 
qtd_de_nove=notas.count(9.0)
print(qtd_de_nove)
qtd_de_sete_nove=notas.count(9.0) + notas.count(7.0)
print(qtd_de_sete_nove)

#alunos q tirarão 6 ou acima
alunos_que_passou=0
for  nota in notas:
    if nota >= 6:
        alunos_que_passou =alunos_que_passou +1
print(alunos_que_passou)

#quantidades de alunos q tirou 7,8 ou ficou entre eles 
qtd_alunos_na_media = sum([7.0 <= nota <= 8.0 for nota in notas])
print(qtd_alunos_na_media)