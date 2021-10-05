class Departamento:



    def __init__(self,id,empleado_encargado,nombre,descripcion, *args, **kargs):
        self.id = id
        self.empleado_encargado = empleado_encargado
        self.nombre = nombre
        self.descripcion = descripcion



    def __str__(self):
        return f"{self.id}--{self.empleado_encargado}--{self.nombre}--{self.edad}--{self.descripcion}"

    def __repr__(self):
        return 'Soy un Departamento'

    def cambiar_empleado_encargado(self, nuevo_empleado_encargado):
        self.empleado_encargado = nuevo_empleado_encargado



