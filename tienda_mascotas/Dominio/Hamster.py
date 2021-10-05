from tienda_mascotas.Dominio.Mascotas import Mascotas




class Hamster(Mascotas):
    __longitud = 0
    def __init__(self,nombre,edad,color,peso,longitud,precio):
        self.longitud = longitud
        super(Hamster, self).__init__(nombre,edad,color,peso,precio)


    def __str__(self):
        return f"{self.id}--{self.nombre}--{self.edad}--{self.color}--{self.peso}--{self.precio}"

    def __repr__(self):
        return f"\nId: {self.id}\nNombre: {self.nombre}\nEdad: {self.edad}" \
               f"\nColor: {self.color}\nPeso: {self.peso}\nLongitud: {self.longitud}\nPrecio: {self.precio}\n"

    def estado(self):
        print("Id: ",self.id, "\nNombre: ",self.nombre,"\nLongitud: ",self.longitud)







