import re
endereco = "Rua da flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro,RJ, 23440-120"
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) # Match \se foi encontrato|
if busca:
    cep =busca.group() # retorna oq foi encontrato
    print(cep)