class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod #transforma em método de classe
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    

    #metodo estático
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

p = Pessoa.criar_de_data_nascimento(1992, 2, 25, 'Luiz')

print(p.nome, p.idade)

print(Pessoa.e_maior_idade(17))
print(Pessoa.e_maior_idade(28))
