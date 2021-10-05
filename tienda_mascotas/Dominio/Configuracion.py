import uuid


class Configuracion:
    def __init__(self,valor=""):
        self.id = str(uuid.uuid4())
        self.valor = valor



    def __repr__(self):
        return f"Id: {self.id}\nValor: {self.valor}"

    def cambiar_valor(self,nuevo_valor):
        self.valor = nuevo_valor
