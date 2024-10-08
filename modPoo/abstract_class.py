from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        ...
    
    @abstractmethod
    def desligar(self):
        ...

    @property
    @abstractproperty
    def marca(self):
        ...

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("ligado")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligado")

    @property
    def marca(self):
        return "LG"


class ControleArCondicionado(ControleRemoto):
    
    def ligar(self):
        print("ar condicionado ligado")

    def desligar(self):
        print("ar condicionado desligado.")

    @property
    def marca(self):
        return "Samsung"

controle = ControleTV()

controle.ligar()
controle.desligar()
print(controle.marca)

Samsung = ControleArCondicionado()

Samsung.ligar()
Samsung.desligar()
print(Samsung.marca)