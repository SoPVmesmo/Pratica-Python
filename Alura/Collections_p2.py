#introdução a conjuntos
def a():
    usuarios_data_science = [15,23,43,56]
    usuarios_machine_learning = [13,23,56,42]
    assistiram = usuarios_data_science.copy()#copia uma lista
    assistiram.extend(usuarios_machine_learning)#adiciona uma lista
    print(assistiram)
    print({1,2,3,4,4})#criar um conjunto simples(conjuntos n repetem o item!!!)
    for usuario in set(assistiram):
        print(usuario)
    usuarios_data_science = {15,23,43,56}
    usuarios_machine_learning = {13,23,56,42}
    x=usuarios_machine_learning | usuarios_data_science#|junta dois conjuntos 
    print(x)

#mais operações com conjuntos
def b():
    usuarios_data_science = {15,23,43,56}
    usuarios_machine_learning = {13,23,56,42}
    print(usuarios_data_science & usuarios_machine_learning)#&== e :pega oq tem de igual nos dois 
    fez=usuarios_data_science - usuarios_machine_learning#retira em usuarios_data_science os q tem em usuarios_machine_learning
    print(15 in fez)#verificando se certo item existe
    print(usuarios_machine_learning ^ usuarios_data_science)#^ == ou :verifica quem fez um ou outro dos cursos mas sem ter feito os 2 

#fazendo modificação em tempo real ou n
def c():
    usuarios={1,2,3,4,5}
    print(len(usuarios))
    usuarios.add(6)#adiciona um item no conjunto
    print(len(usuarios))
    usuarios=frozenset(usuarios)#congela o conjunto n pode mais mudar ele

#tranformando txt em conjunto
def d():
    meu_texto="meu nome é PV e to com preguiça de fazer o texto grande q ele fez pv dnvo"
    meu_texto =meu_texto.lower()
    x=set(meu_texto.split())#transforma cada espaço em branoc em um item de uma lista 
    
    #01 forma de se utilizar 
    aparicoes = {}
    for palavra in meu_texto.split():
        ate_agora = aparicoes.get(palavra,0)#procura se a palavra ja existe no dicionario se sim volta o valor dela se n rertonar 0
        aparicoes[palavra] = ate_agora + 1#adiciona o item com o valor 1 ou atualiza ele com as vezes q ele se repetiu
    print(aparicoes)

    #02 forma de se utilizar 
    from collections import defaultdict
    aparicoes2 = defaultdict(int)
    for palavra in meu_texto.split():
        ate_agora = aparicoes2[palavra]#procura se a palavra ja existe no dicionario se sim volta o valor dela se n rertonar 0
        aparicoes2[palavra] = ate_agora + 1#adiciona o item com o valor 1 ou atualiza ele com as vezes q ele se repetiu
    print(aparicoes2)

#dicionarios
def e():
    aparicoes={
        "Guilherme" : 1,
        "Cachorro" : 2,
        "nome" : 2,
        "Vindo" : 1
    }
    print(aparicoes["Guilherme"])#retorna oq tiver na chave Guilherme
    print(aparicoes.get("pv",0))#retorna oq tiver na chave pv se n existir essa chave retorna 0
#outra forma de utilizar o dicionario
    nomes=dict(pv=17,Daniel = 9)
    print(nomes)

#modificação no dicionario
def f():
    aparicoes={
        "Guilherme" : 1,
        "Cachorro" : 2,
        "nome" : 2,
        "Vindo" : 1
    }
    aparicoes["carlos"] = 1#adiciona um item do dicionario
    aparicoes["nome"] = 0#modifica o valor de um dicionario
    del aparicoes["carlos"]#remove dos itens 
    print("nome" in aparicoes)#verifica se tem no dicionario atravez da CHAVE
    print(aparicoes)

    for elemento in aparicoes.keys():#chavez
        print(elemento)

    for elemento in aparicoes.values():#valores
        print(elemento)

    for elemento in aparicoes.items():#itens e valores
        print(elemento)

    for chave,valor in aparicoes.items():#itens e valores
        print(chave,"=",valor)
    
    lista=["pv {}".format(chave) for chave in aparicoes.keys()]#adiciona a palavra pv antes de cada chave
    print(lista)

#usando o defaultdict
def g():
    from collections import defaultdict
    meu_texto="meu nome é PV e to com preguiça de fazer o texto grande q ele fez pv dnvo"
    meu_texto = meu_texto.lower()
    aparicoes2 = defaultdict(int)

    for palavra in meu_texto.split():
        aparicoes2[palavra] += 1#adiciona o item com o valor 1 ou atualiza ele com as vezes q ele se repetiu
    print(aparicoes2)

    class conta:
        def __init__(self):
            print("Criando uma conta")
    contas = defaultdict(conta)
    contas[15]
    contas[17]

    from collections import Counter
    aparicoes = Counter()
    for palavra in meu_texto.split():
        aparicoes[palavra] += 1#adiciona o item com o valor 1 ou atualiza ele com as vezes q ele se repetiu
    print(aparicoes)
    
    aparicoes3 = Counter(meu_texto.split())
    print(aparicoes3)

#contando letras
def h():
    from collections import Counter
    texto1= """PODERIA TER SIDO PIOR, ISSO É CERTO ― disse Mestre Arwyl com uma
expressão séria no rosto redondo enquanto andava à minha volta. ― Eu esperava
que você fosse ficar apenas com vergões, mas, com a sua pele, já devia saber que
não seria assim."""

    texto2="""Eu estava sentado na beira de uma mesa comprida no interior da Iátrica.
Arwyl foi apalpando minhas costas de leve enquanto continuava a conversar."""
    def analisa_frequencia_de_texto(texto):
        aparicoes = Counter(texto.lower())#contando quantos vezes cada caractere aparece no texto
        total_de_caracteres = sum(aparicoes.values())#somando quantos caracteres existem 
        print(total_de_caracteres)

        #uma lista com a porcentagem que cada letra aparece
        proporcoes =  [(letra,frequencia/total_de_caracteres) for letra,frequencia in aparicoes.items()]
        proporcoes =Counter(dict(proporcoes))#usando o dicionario com um contador 
        mais_comuns = proporcoes.most_common(10)#mostrando os 10 mais comuns 

        for caractere, proporcao in mais_comuns:
            print("{} => {:.2f}%".format(caractere,proporcao * 100))
    analisa_frequencia_de_texto(texto1)
h()