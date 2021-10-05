class Venta:



    def __init__(self,id,producto,cantidad,fecha,total, *args, **kargs):
        self.id = id
        self.producto = producto
        self.cantidad = cantidad
        self.fecha = fecha
        self.total = total




    def __str__(self):
        return f"{self.id}--{self.producto}--{self.cantidad}--{self.fecha}--{self.total}"

    def __repr__(self):
        return 'Soy una Venta'

    def editar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad



