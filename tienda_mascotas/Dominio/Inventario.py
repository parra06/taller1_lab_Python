


from tienda_mascotas.Dominio.Perro import Perro
from tienda_mascotas.Dominio.Gato import Gato
from tienda_mascotas.Dominio.Hamster import Hamster
from tienda_mascotas.Dominio.Cuidador import Cuidador
from tienda_mascotas.Dominio.Accesorio import Accesorio
from tienda_mascotas.Dominio.Especificacion import Especificacion
import os
from pathlib import Path

class Inventario():

    def __init__(self):
        self.mascotas = []

        self.accesorios = []
        self.cuidadores = []

    def eliminar_listas(self):
        self.mascotas.clear()
        self.accesorios.clear()
        self.cuidadores.clear()

    def agregar_objeto(self, objeto):


        if type(objeto) == Perro:
            espec = Especificacion()
            espec.agregar_parametro('id', objeto.id)
            if len(list(self.buscar_mascota(espec))) == 0:
                self.mascotas.append(objeto)

            else:
                raise Exception('Perro repetido')


        if type(objeto) == Gato:
            espec = Especificacion()
            espec.agregar_parametro('id', objeto.id)
            if len(list(self.buscar_mascota(espec))) == 0:
                self.mascotas.append(objeto)
            else:
                raise Exception('Gato repetido')

        if type(objeto) == Hamster:
            espec = Especificacion()
            espec.agregar_parametro('id', objeto.id)
            if len(list(self.buscar_mascota(espec))) == 0:
                self.mascotas.append(objeto)
            else:
                raise Exception('Hamster repetido')

        if type(objeto) == Cuidador:
            espec = Especificacion()
            espec.agregar_parametro('cedula',objeto.cedula)

            if len(list(self.buscar_cuidador(espec))) == 0:
                self.cuidadores.append(objeto)
            else:

                raise Exception('Cuidador repetido')

        if type(objeto) == Accesorio:
            espec = Especificacion()
            espec.agregar_parametro('id', objeto.id)
            if len(list(self.buscar_accesorio(espec))) == 0:
                self.accesorios.append(objeto)
            else:
                raise Exception('Accesorio repetido')


    # ------------------------------------------------------

    def buscar_accesosio_id(self,id):

        for g in self.accesorios:
            if g.id == id:
                yield g

    def buscar_accesosio_nombre(self,nombre):

        for g in self.accesorios:
            if g.nombre == nombre:
                yield g

    def buscar_accesosio_descripcion(self,descripcion):

        for g in self.accesorios:
            if g.descripcion == descripcion:
                yield g

    def buscar_accesosio_precio(self,precio):

        for g in self.accesorios:
            if g.precio == precio:
                yield g

    def buscar_accesosio_tipoM(self,tipoM):

        for g in self.accesorios:
            if g.tipo_mascota == tipoM:
                yield g

    # ------------------------------------------------------


    def buscar_mascota_nombre(self,nombre):

        for g in self.mascotas:
            if g.nombre == nombre:
                yield g

    def buscar_mascota_id(self,id):

        for g in self.mascotas:
            if g.id == id:
                yield g

    def buscar_mascota_edad(self,edad):

        for g in self.mascotas:
            if g.edad == edad:
                yield g

    def buscar_mascota_color(self,color):

        for g in self.mascotas:
            if g.color == color:
                yield g

    def buscar_mascota_peso(self,peso):

        for g in self.mascotas:
            if g.peso == peso:
                yield g

    def buscar_mascota_raza(self,raza):

        for g in self.mascotas:
            if isinstance(g,Hamster):
                pass
            else:
                if g.raza == raza:
                    yield g

    def buscar_mascota_precio(self,precio):

        for g in self.mascotas:
            if g.precio == precio:
                yield g

    def buscar_mascota_longitud(self,longitud):

        for g in self.mascotas:
            if isinstance(g,Hamster):

                if g.longitud == longitud:
                    yield g

    #------------------------------------------------------
    def buscar_cuidador_nombre(self,nombre):

        for g in self.cuidadores:
            if g.nombre == nombre:
                yield g

    def buscar_cuidador_cedula(self,cedula):

        for g in self.cuidadores:
            if g.cedula == cedula:
                yield g

    def buscar_cuidador_apellido(self,apellido):

        for g in self.cuidadores:
            if g.apellido == apellido:
                yield g

    def buscar_cuidador_edad(self,edad):

        for g in self.cuidadores:
            if g.edad == edad:
                yield g

    def buscar_cuidador_telefono(self,telefono):

        for g in self.cuidadores:
            if g.telefono == telefono:
                yield g

    def buscar_cuidador_direccion(self,direccion):
        for g in self.cuidadores:
            if g.direccion == direccion:
                yield g

    # ------------------------------------------------------



    def buscar_mascota(self, especificacion):

        for p in self.mascotas:
            if p.cumple_mascota(especificacion):
                yield p



    def buscar_cuidador(self, especificacion):

        for p in self.cuidadores:
            if p.cumple_cuidador(especificacion):
                yield p

    def buscar_accesorio(self, especificacion):

        for p in self.accesorios:
            if p.cumple_accesorio(especificacion):
                yield p

    # ------------------------------------------------------

    def eliminar_mascota(self,id):

        for g in self.mascotas:
            if g.id == id:
                self.mascotas.remove(g)
                print(self.mascotas)
