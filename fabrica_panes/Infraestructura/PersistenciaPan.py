import pickle
import sqlite3
import jsonpickle

from fabrica_panes.Dominio import Pan


class PersistenciaPan():

    def connect(self):
        self.con = sqlite3.connect("fabrica_de_panes.sqlite")
        self.__crear_tabla()


    def __crear_tabla(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE PAN(id text primary key, nombre text," \
                " departamento text, precio float) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_guitarra(self,pan : Pan):
        cursor = self.con.cursor()
        query = "insert into PAN(id , nombre ," \
                " departamento , precio ) values(" \
                f" ?,?,?,?)"
        cursor.execute(query, (str(pan.id), pan.nombre, pan.departamento,
                               pan.precio))
        self.con.commit()

    @classmethod
    def save(cls, pan):
        binary_open = open("files/" + str(pan.id) + '.gui', mode='wb')
        pickle.dump(pan, binary_open)
        binary_open.close()

    @classmethod
    def load(cls, file_name):
        binary_open = open("files/" + file_name, mode='rb')
        pan = pickle.load(binary_open)
        binary_open.close()
        return pan

    @classmethod
    def save_json(cls, pan):
        text_open = open("files/" + str(pan.id) + '.json', mode='w')
        json_gui = jsonpickle.encode(pan)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        pan = jsonpickle.decode(json_gui)
        text_open.close()
        return pan