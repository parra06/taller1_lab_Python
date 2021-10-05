import uuid


class Producto:



    def __init__(self,tipo,nombre,proveedor,precio, *args, **kargs):
        self.id = uuid.uuid4()
        self.tipo = tipo
        self.nombre = nombre
        self.proveedor = proveedor
        self.precio = precio


    def __str__(self):
        return f"{self.id}--{self.tipo =}--{self.nombre =}--{self.proveedor}--{self.precio}"

    def __repr__(self):
        return 'Soy un Producto'

    def apreciar(self, nuevo_precio):
        self.precio = nuevo_precio

    def cambiar_proveesor(self, nuevo_proveedor):
        self.proveedor = nuevo_proveedor

    def cumple(self, especificacion):
        dict_producto = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_producto or dict_producto[k] != especificacion.get_value(k):
                return False
        return True