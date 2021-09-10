from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever


escritor = Escritor('Jão')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

'''
Associação simples de classes. 
Usando o metodo ferramenta da classe Escritor, 
consigo associar as classes de maneira simples.
'''
escritor.ferramenta = caneta
escritor.ferramenta.escrever()

