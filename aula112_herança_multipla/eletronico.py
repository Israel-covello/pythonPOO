class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False  # Inicia com o Eletronico desligado

    def ligar(self):
        if self._ligado:
            return
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            return
        self._ligado = False
