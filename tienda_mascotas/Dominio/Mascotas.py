import uuid


class Mascotas():

    def __init__(self,nombre,edad,color,peso,precio):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.peso = peso
        self.precio = precio


    def apreciar(self, nuevo_precio):
        self.precio = nuevo_precio

    def pesar(self, nuevo_peso):
        self.peso = nuevo_peso

    def estado(self):
        print("Id: ",self.id, "\nNombre: ",self.nombre)

    def cumple_mascota(self, especificacion):
        dict = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict or dict[k] != especificacion.get_value(k):
                return False
        return True