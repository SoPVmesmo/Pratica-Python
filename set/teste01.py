print("Estruturas de repetição")
contador = 0
while (contador <= 5 ):
    print(contador)
    contador = contador +1
else:
    print("fim do where")


num = 25
while(num > 0):
    if num == 17:
        break
    else:
        print(num)
        num = num - 1

computador = ['Processador', 'Teclado', 'Mouse']
for indice, valor in enumerate(computador):
    print(f"Índice={indice} | Valor={valor}")

    PS2 = ["Devil may cry","God Hand","Resident Evil 4","God of war"]
for jogos in PS2:
    print(jogos)
print('Fim do for')