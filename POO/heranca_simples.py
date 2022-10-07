class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def esta_carrregado(self):
        print("Não estou carregado")

moto = Motocicleta("preta", "ABC-1234", 2)
moto.ligar_motor()

carro = Carro("Branco", "CAR-4321", 4)
carro.ligar_motor()

caminhao = Caminhao("vermelho", "CAM-1423", 8)
caminhao.ligar_motor()
caminhao.esta_carrregado()