from classes import CarrinhoDeCompras, Produtos

carrinho = CarrinhoDeCompras()

p1 = Produtos('Camisa', 50)
p2 = Produtos('iPhone', 10000)
p3 = Produtos('Caneca', 15)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p2)

carrinho.lista_produto()
print(carrinho.soma_produto())
