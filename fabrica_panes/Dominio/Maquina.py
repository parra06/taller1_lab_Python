class Maquina:



    def __init__(self,id,nombre,departamento, *args, **kargs):
        self.id = id
        self.nombre = nombre
        self.departamento = departamento


    def __str__(self):
        return f"{self.id}--{self.nombre}--{self.departamento}"

    def __repr__(self):
        return 'Soy una Maquina'

    def cambiar_departamento(self, nuevo_departamento):
        self.departamento = nuevo_departamento

