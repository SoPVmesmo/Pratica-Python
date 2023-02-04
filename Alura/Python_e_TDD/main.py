from bytebank import Funcionario

def teste_idade():
    Funcionario_teste = Funcionario("teste", "13/03/2000", 1111)
    print(f"Teste = {Funcionario_teste.idade()}")

    Funcionario_teste = Funcionario("teste", "01/12/1999", 1111)
    print(f"Teste = {Funcionario_teste.idade()}")

    Funcionario_teste = Funcionario("teste", "17/04/2003", 1111)
    print(f"Teste = {Funcionario_teste.idade()}")

teste_idade()