


from fabrica_panes.Dominio import Pan
from fabrica_panes.Dominio.EspecificacionPan import EspecificacionPan


class InventarioPan():

    def __init__(self):
        self.panes = []

    def agregar_pan(self, pan):

        if type(pan) == Pan:
            espec = EspecificacionPan()
            espec.agregar_parametro('id', pan.id)
            if len(list(self.buscar(espec))) == 0:
                self.panes.append(pan)
            else:
                raise Exception('Pan repetido')

    def buscar(self, especificacion):

        for p in self.panes:
            if p.cumple(especificacion):
                yield p
