class Cliente:



    def __init__(self,cedula,nombre,apellido,edad,telefono,direccion, *args, **kargs):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self):
        return f"{self.cedula}--{self.nombre}--{self.apellido}--{self.edad}--{self.telefono}--{self.direccion}"

    def __repr__(self):
        return 'Soy un Cliente'

    def editar_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono

