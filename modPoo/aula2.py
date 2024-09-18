# Heranças !!


class Veiculo:
    def __init__ (self, cor, placa, nro_rodas):
        self.cor = cor
        self.placa = placa
        self.nro_rodas = nro_rodas

    def ligar_motor(self):
        print('Ligando o motor')

    def __str__(self):
        return f'{self.__class__.__name__}: {", ".join([f"{chave} = {valor}" for chave, valor in self.__dict__.items()])}'

class Motocicleta(Veiculo):
    ...

class Carro(Veiculo):
    ...

class Caminhao(Veiculo):
    
    def __init__(self, cor, placa, nro_rodas, carregado):

        super().__init__(cor, placa, nro_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f'{"Sim" if self.carregado else "Não"} esta carregado')

# moto = Motocicleta('vermelho', 'ABC-0023', 2)
# moto.ligar_motor()

# carro = Carro("preto", "XSB-2039", 4)
# carro.ligar_motor()

caminhao = Caminhao("Azul", "ACE-2030", 8, not False)
caminhao.ligar_motor()
caminhao.esta_carregado()

print(caminhao)