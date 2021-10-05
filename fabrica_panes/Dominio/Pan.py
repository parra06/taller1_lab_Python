import uuid


class Producto:



    def __init__(self,nombre,departamento,precio, *args, **kargs):
        self.id = uuid.uuid4()
        self.nombre = nombre
        self.departamento = departamento
        self.precio = precio


    def __str__(self):
        return f"{self.id}--{self.nombre}--{self.departamento}--{self.precio}"

    def __repr__(self):
        return str(self.id)

    def apreciar(self, nuevo_precio):
        self.precio = nuevo_precio

    def cumple(self, especificacion):
        dict_pan = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_pan or dict_pan[k] != especificacion.get_value(k):
                return False
        return True



