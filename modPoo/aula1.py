class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro
        self.marcha = 1
    
    def buzinar(self):
        print(f'A {self.modelo} está buzinando')

    def parar(self):
        print('Parando a bike')
        print('Bicicleta parada')

    def correr(self):
        print('pedala, pedala, pelada')
        print('correndoo!! cuidado !')

    def trocar_marcha (self, nro_marcha):
        print('Trocando marcha')

        if nro_marcha > self.marcha:
            print('marcha trocada...')
            
        else:
            print('não foi possível trocar de marcha')
            
            

    def __str__(self):
        return f'{self.__class__.__name__}: {", ".join([f"{chave} = {valor}" for chave, valor in self.__dict__.items()])}'


b1 = Bicicleta("vermelha", "Caloi", 2022, 600)

b2 = Bicicleta("verde","monark", 2000, 189)

# Bicicleta.buzinar(b2)
# b1.buzinar()
# b1.parar()
# b1.correr()


b2.trocar_marcha(2)