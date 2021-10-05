from tienda_mascotas.Dominio.Mascotas import Mascotas


class Gato (Mascotas):
    __raza = ""

    def __init__(self, nombre, raza, edad, color, peso, precio):
        self.raza = raza
        super(Gato, self).__init__(nombre, edad, color, peso, precio)

    def __str__(self):
        return f"{self.id}--{self.nombre}--{self.raza}--{self.edad}--{self.color}--{self.peso}--{self.precio}"

    def __repr__(self):
        return f"\nId: {self.id}\nNombre: {self.nombre}\nRaza: {self.raza}\nEdad: {self.edad}" \
               f"\nColor: {self.color}\nPeso: {self.peso}\nPrecio: {self.precio}\n"

    def estado(self):
        print("Id: ", self.id, "\nNombre: ", self.nombre, "\nRaza: ", self.raza)








