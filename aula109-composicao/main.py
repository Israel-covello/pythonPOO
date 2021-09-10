from classes import Cliente, Endereco


cliente1 = Cliente('Israel', 25)
cliente1.insere_endereco('Pirassununga', 'SP')
print(cliente1.nome)
cliente1.lista_endereco()

cliente2 = Cliente('João', 35)
cliente2.insere_endereco('Belo Horizonte', 'MG')
print('\n', cliente2.nome)
cliente2.lista_endereco()

cliente3 = Cliente('Maria', 65)
cliente3.insere_endereco('Rio de Janeiro', 'RJ')
cliente3.insere_endereco('Salvador', 'BA')
print('\n', cliente3.nome)
cliente3.lista_endereco()
