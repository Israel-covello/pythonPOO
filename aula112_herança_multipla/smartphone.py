from eletronico import Eletronico
from log import LogMixin


# Utilizando a classe LogMixin como herança multipla junto com a classe pai "Eletetronico"
class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            error = f'{self._nome} NÃO ESTÁ LIGADO!'
            print(error)
            self.log_error(error)
            return

        if self._conectado:
            error = f'{self._nome} JÁ ESTÁ CONECTADO!'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} ESTÁ CONECTADO!'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} NÃO ESTÁ CONECTADO!'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} FOI DESLIGADO COM SUCESSO!'
        print(info)
        self.log_info(info)
        self._conectado = False
