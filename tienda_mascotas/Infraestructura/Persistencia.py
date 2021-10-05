import pickle
import sqlite3
import jsonpickle


from tienda_mascotas.Dominio.Perro import Perro
from tienda_mascotas.Dominio.Gato import Gato
from tienda_mascotas.Dominio.Hamster import Hamster
from tienda_mascotas.Dominio.Cuidador import Cuidador
from tienda_mascotas.Dominio.Accesorio import Accesorio
from tienda_mascotas.Dominio.Configuracion import Configuracion

class Persistencia():

    def connect(self):
        self.con = sqlite3.connect("tienda_mascotas.db")
        self.__crear_tabla_Gato()
        self.__crear_tabla_perro()
        self.__crear_tabla_hamster()
        self.__crear_tabla_accesorio()
        self.__crear_tabla_cuidador()


    def __crear_tabla_cuidador(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE CUIDADOR(cedula text primary key,nombre text, apellido text," \
                    " edad float, telefono text, direccion text) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass



    def __crear_tabla_accesorio(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE ACCESORIO(id text primary key,nombre text, descripcion text," \
                    " precio float, tipo_mascota text) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def __crear_tabla_Gato(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE GATO(id text primary key, nombre text," \
                " raza text, edad number, color text,peso float,precio float) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def __crear_tabla_perro(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE PERRO(id text primary key, nombre text," \
                " raza text, edad number, color text,peso float,precio float) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def __crear_tabla_hamster(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE HAMSTER(id text primary key, nombre text," \
                " edad number, color text,peso float,longitud float, precio float) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_bd(self,objeto):
        cursor = self.con.cursor()

        if isinstance(objeto,Gato):


            query = "insert into GATO(id , nombre ," \
                " raza , edad,color,peso,precio ) values(" \
                f" ?,?,?,?,?,?,?)"
            cursor.execute(query, (str(objeto.id), objeto.nombre, objeto.raza,
                               objeto.edad,objeto.color,objeto.peso,objeto.precio))

        if isinstance(objeto,Perro):

            query = "insert into PERRO(id , nombre ," \
                    " raza , edad,color,peso,precio ) values(" \
                    f" ?,?,?,?,?,?,?)"
            cursor.execute(query, (str(objeto.id), objeto.nombre, objeto.raza,
                                   objeto.edad, objeto.color, objeto.peso, objeto.precio))

        if isinstance(objeto,Hamster):
            query = "insert into HAMSTER(id , nombre ," \
                    "edad,color,peso,longitud,precio ) values(" \
                    f" ?,?,?,?,?,?,?)"
            cursor.execute(query, (str(objeto.id), objeto.nombre,objeto.edad,
                                   objeto.color, objeto.peso,objeto.longitud, objeto.precio))


        if isinstance(objeto,Accesorio):
             query = "insert into ACCESORIO(id ,nombre, descripcion ," \
                "precio,tipo_mascota ) values(" \
                f" ?,?,?,?,?)"
             cursor.execute(query, (str(objeto.id), objeto.nombre, objeto.descripcion,
                               objeto.precio, objeto.tipo_mascota))

        if isinstance(objeto,Cuidador):
            query = "insert into CUIDADOR(cedula ,nombre, apellido ," \
                    "edad,telefono,direccion ) values(" \
                    f" ?,?,?,?,?,?)"
            cursor.execute(query, (str(objeto.cedula), objeto.nombre, objeto.apellido,
                                   objeto.edad, objeto.telefono, objeto.direccion))


        self.con.commit()



    @classmethod
    def save_json(cls, objeto):

        if isinstance(objeto,Cuidador):
            text_open = open("Files/" + str(objeto.cedula) + '.json', mode='w')
            json_gui = jsonpickle.encode(objeto)
            text_open.write(json_gui)
            text_open.close()
        elif isinstance(objeto,Configuracion):
            text_open = open("config/" + str(objeto.valor) + '.json', mode='w')
            json_gui = jsonpickle.encode(objeto)
            text_open.write(json_gui)
            text_open.close()

        else:
            text_open = open("Files/" + str(objeto.id) + '.json', mode='w')
            json_gui = jsonpickle.encode(objeto)
            text_open.write(json_gui)
            text_open.close()



    @classmethod
    def load_json(cls, file_name):
        text_open = open("Files/" + file_name, mode='r')
        json_gui = text_open.readline()
        objeto = jsonpickle.decode(json_gui)
        text_open.close()
        return objeto

    def load_json_config(self,file_name):
        text_open = open("config/" + file_name, mode='r')
        json_gui = text_open.readline()
        objeto = jsonpickle.decode(json_gui)
        text_open.close()
        return objeto