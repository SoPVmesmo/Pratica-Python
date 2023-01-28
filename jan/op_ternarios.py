user_log = True
msg = " Usuario Logado com Sucesso" if (user_log) else "Login incorreto!! verifique seu usuario e sua senha"
print(msg)

idade = input("Informe sua idade:\n")
if not idade.isnumeric():
    print("voçe precisa digitar somente numeros!!")
else:
    idade = int(idade)
    e_adolecente = (idade > 12 and idade < 18)
    e_de_maior = (idade >= 18)
    msg = "Voce é de maior!! parabens já pode ser preso!!"if e_de_maior else "voce é adolecente!!" if e_adolecente else "voce é criança"
print(msg)