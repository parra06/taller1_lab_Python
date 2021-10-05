class Empleado:



    def __init__(self,cedula,nombre,apellido,edad,telefono,direccion,tipo,departamento, *args, **kargs):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.direccion = direccion
        self.tipo = tipo
        self.departamento = departamento

    def __str__(self):
        return f"{self.cedula}--{self.nombre}--{self.apellido}--{self.edad}--{self.telefono}--{self.direccion}--{self.tipo}" \
               f"--{self.departamento}"

    def __repr__(self):
        return 'Soy un Operador'

    def editar_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono

    def cambiar_departamento(self, nuevo_departamento):
        self.departamento = nuevo_departamento

