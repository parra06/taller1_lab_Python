class Pedido:



    def __init__(self,id,producto,cantidad,fecha,fecha_entrega,total, *args, **kargs):
        self.id = id
        self.producto = producto
        self.cantidad = cantidad
        self.fecha = fecha
        self.fecha_entrega = fecha_entrega
        self.total = total




    def __str__(self):
        return f"{self.id}--{self.producto}--{self.cantidad}--{self.fecha}--{self.fecha_entrega}--{self.total}"

    def __repr__(self):
        return 'Soy un Pedido'

    def editar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def cambiar_fecha_entrega(self, nueva_fecha_entrega):
        self.fecha_entrega = nueva_fecha_entrega



