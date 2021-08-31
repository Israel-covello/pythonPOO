
class Pessoa:
    ano_atual = 2021       # Atributo de Classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod             # Metodo de Classe
    def por_ano_nascimento(cls, nome, ano_nascimento):    # cls é pela convenção, usado para referênciar a classe, quando é usado metodos de class
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


p1 = Pessoa('Isral', 26)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
