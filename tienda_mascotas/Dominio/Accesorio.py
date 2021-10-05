import uuid


class Accesorio:



    def __init__(self,nombre,descripcion,precio,tipo_mascota):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.tipo_mascota = tipo_mascota


    def __str__(self):
        return f"{self.id}--{self.descripcion}--{self.precio}--{self.tipo_mascota}"

    def __repr__(self):
        return f"\nId: {self.id}\nNombre: {self.nombre}\nDescripcion: {self.descripcion}\nPrecio: {self.precio}" \
               f"\nTipo Mascota: {self.tipo_mascota}\n"

    def apreciar(self, nuevo_precio):
        self.precio = nuevo_precio

    def cumple_accesorio(self, especificacion):
        dict = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict or dict[k] != especificacion.get_value(k):
                return False
        return True

