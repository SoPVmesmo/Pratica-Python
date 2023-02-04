from bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        # Given - Contexto
        entrada = "13/03/2000"
        esperado = 22
        funcionario_teste = Funcionario("teste",entrada,1111)

        # When - Ação 
        resultado = funcionario_teste.idade()

        # Then - Desfecho
        assert resultado == esperado

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        # Given - Contexto
        entrada = " Lucas Carvalho "
        esperado = "Carvalho"

        lucas = Funcionario(entrada, "11/11/2000", 1111)

        # When - Ação
        resultado = lucas.sobrenome()

        # Then - Desfecho
        assert resultado == esperado
    
    def test_quando_decrescimo_salario_recebe100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = "Paulo Bragança"
        esperado = 90000
        funcionario_teste = Funcionario(entrada_nome, "11/11/2000", entrada_salario)
        
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

print("oi sara")