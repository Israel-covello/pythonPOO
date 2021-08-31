class CalcCubo:
    # Essa função que inicia com __init__ é o metodo construtor.
    # (Ela é executada automaticamente quando instanciá o Objeto)
    # É uma classe que permite calcular o cubo de um número

    def __init__(self, valor):
        self.x = valor
        print('Objeto Criada!')

    def calcula_cubo(self):
        self.cubo = self.x * self.x * self.x
        return 'Cubo calculado: ' + str(self.cubo)


num = int(input('Digite um número para calcular o cubo: '))

objCubo = CalcCubo(num)  # --> Instanciar a classe

cubo = objCubo.calcula_cubo()  # --> O operador ponto "." serve para invocar o metodo da classe. Logo em seguida
# passar o metodo desejado. Ficar atento se tiver que passar algum parametro para o metododo.

print(cubo)
