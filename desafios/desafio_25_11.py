"""Implemente uma classe chamada Carro
Com os seguintes atributos: modelo do carro, cor, potencia motor, consumo(Km por litros), Litros no Tanque, velocidade
• implemente o método pintar() para alterar a cor do carro
• Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque.
 Esse  método recebe como parâmetro a distância em km.
• Forneça um método abastecer( ), que colocar combustível no tanque.
• Faça um programa para testar a classe Carro."""
class Carro:
    def __init__(self,modelo_do_carro,cor,potencia_motor,consumo,velocidade):
        self._modelo_do_carro = modelo_do_carro
        self.cor = cor
        self._potencia_motor = potencia_motor
        self.consumo = consumo
        self.litros_tanque = 0
        self._velocidade = velocidade

    def pintar(self,nova_cor):
        if nova_cor.isalpha() == True:
            self.cor = nova_cor
            return self.cor
        else:
            print("Cor tem que ser uma String")

    def abastecer(self,quantidade):
        if  type(quantidade) == float or type(quantidade) == int and quantidade > 0:
            max = self.litros_tanque + quantidade
            if max > 40:
                print("O valor ultrapassa o limite do tanque de gasolina")
            else:
                print("carro abastecido!!!")
                self.litros_tanque += quantidade
        else:
            print("O valor tem que ser um numero real positivo!!")

    def andar(self,distancia):
        if self.litros_tanque > 0:
            if type(distancia) == float or type(distancia) == int and distancia > 0:
                distancia_max = self.litros_tanque * self.consumo
                if  distancia > distancia_max:
                    print("Sem gasolina para essa distancia")
                else:
                    print("Distancia percorrida!!")
                    self.litros_tanque -= (distancia/self.consumo)
            else:
                print("A distancia tem que ser um numero real positivo")
        else:
            print("O tanque esta sem gasolina!!!")
    

fusca=Carro("fusca","Azul","traseiro, 4 cilindros boxer, 2 válvulas por cilindro",12,"70 km por hora")

#print(fusca.cor)
#fusca.pintar("vermelho")
#print(fusca.cor)

#print(fusca.litros_tanque)
#fusca.abastecer(40)
#print(fusca.litros_tanque)

#print(fusca.litros_tanque)
#fusca.andar(400)
#print(fusca.litros_tanque)