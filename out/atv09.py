nome=input("digite seu nome:\n")
Endereco=input("Digite seu endereço:\n")
Aniversario=input("seu aniversario:\n")
CPF=input("digite seu cpf:\n")
RG=input("Digite seu rg:\n")
dici={
    "nome":nome,
    "endereço":Endereco,
    "aniversario":Aniversario,
    "cpf":CPF,
    "rg":RG
    }
print(dici.items())