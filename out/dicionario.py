#keys() retorna todas as chaves do dici
#values() retorna os valores do dici
#items() retorna os pares (chaves e valores)
#has_key(chave) descobrir se x chave ta no dici
#fromkeys pega um dici e cria outra com as chaves deles onde os valores são iguais
#copy copia um dici
#get retorna o valor sem chave
#updade junta 2 dici
#popitem exclui uma dupla aleatoria do dici
#pop remove o a dupla do dici
nome=input("digite seu nome:\n")
Endereco=input("Digite seu endereço:\n")
Aniversario=input("seu aniversario:\n")
CPF=input("digite seu cpf:\n")
RG=input("Digite seu rg:\n")
dici={
    "nome":"PV",
    "endereço":"Endereço",
    "aniversario":"17/04/2003",
    "cpf":"17",
    "rg":"7"
    }
print(dici.items())

print(dici.keys())

print(dici.values())

print(dici.keys())

dici["sobrenome"]="oliveira"

print(dici.values())


dici02={}
def ad_cliente(): 
    n= int(input("Digite quantos clientes serão adicionados:\n"))
    y=len(dici02) + n
    while len(dici02) != y:
        x=len(dici02)+1
        nome=input(f"Digite o nome do cliente {x}:\n")
        dici02[x]=nome

ad_cliente()
print(dici02.items())
ad_cliente()
print(dici02.items())


Dici={
    "Nome":"PV",
    "Sobrenome":"Oliveira",
    "Idade":19,
}
print(Dici.get("Nome"))#forma 01 de se trazer um valor
print(Dici["Sobrenome"])#forma 02 de se tarzer um valor

if "Nome" in Dici:#So procura pela chaves!!!
    print("A chave 'Nome' existe no dicionario!")
else:
    print("A chave 'Nome' não existe no dicionario!")

Dici["sexo"]="Masculino"#Adicionar um item uma dupla no dicionario

for x in Dici:
    print(x)#mostra todas as chaves 
    print(Dici[x])#mostra todos os valores

for x, y in Dici.items():#forma mais bonitinha de se mostrar os valores
    print(x,y)


Amigos={
    "Matheus":{
        "Nome":"Mathues",
        "Idade":19,
        "Sexo":"masculino"
    },
    "Sammira":{
        "Nome":"Sammira",
        "Idade":19,
        "Sexo":"feminino"
    },
    "Laisa":{
        "Nome":"Laisa",
        "Idade":19,
        "Sexo":"Feminino"
    },
    "Saulo":{
        "Nome":"Saulo",
        "Idade":19,
        "Sexo":"Masculino"
    }
}
print(Amigos.values())