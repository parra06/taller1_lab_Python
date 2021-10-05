class Cuidador:



    def __init__(self,cedula,nombre,apellido,edad,telefono,direccion):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self):
        return f"{self.cedula}--{self.nombre}--{self.apellido}--{self.edad}--{self.telefono}--{self.direccion}"

    def __repr__(self):
        return f"\nCedula: {self.cedula}\nNombre: {self.nombre}\nApellido: {self.apellido}\nEdad: {self.edad}" \
               f"\nTelefono: {self.telefono}\nDireccion: {self.direccion}\n"

    def editar_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono

    def cumple_cuidador(self, especificacion):
        dict = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict or dict[k] != especificacion.get_value(k):
                return False
        return True

