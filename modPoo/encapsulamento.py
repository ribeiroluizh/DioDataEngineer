'''
O que é encapsulamento?
Descreve a ideia de agrupar os metodos que manipulam esses dados em uma unidade.
Impõe restrições ao acesso direto a variáveis e métodos e pode evitar a modificação acidental de dados.
Para evitar alterações acidentais, a variável de um objeto só pode ser alterada pelo método desse objeto.


Recursos publicos e privados


Propriedades
property(). 
Você pode usar atributos gerenciados, também conhecidos como propriedades, quando precisar modificar sua 
implementação interna sem alterar a API pública da classe.
@property()
@x.setter()
@x.deleter()

'''

class Conta:
    def __init__(self, nro_agencia, saldo=0):
        
        self._saldo = saldo
        self.nro_agencia = nro_agencia
    
    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo

conta = Conta("0001", 100)

conta.depositar(1000)

# print(conta.mostrar_saldo())

#### Property

class Foo:
    
    def __init__ (self, x=None):
        self._x = x

    @property
    def x (self):
        return self._x or 0
    
    @x.setter
    def x (self, value):
        self._x += value

    @x.deleter
    def x (self):
        self._x = 0

    @x.getter
    def x (self):
        ...
    


foo = Foo(10)
print(foo.x)

foo.x = 20

print(foo.x)

del foo.x
print(foo.x)
