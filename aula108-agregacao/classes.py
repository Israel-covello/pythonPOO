class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_produto(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return f'R$ {total}'


'''
Essa é uma relação de agregação de classes, onde a classe CarrinhoDeCompras 
pode existir sem a classe produtos, porem sem a classe produtos,
ela não executa nada. Então ela precisa da classe Produtos.
E a classe Produtos não depende em nada da classe CarrinhoDeCompras.
'''


class Produtos:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
