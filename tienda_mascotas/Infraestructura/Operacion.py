import os

from tienda_mascotas.Dominio.Inventario import Inventario
from tienda_mascotas.Infraestructura.Persistencia import Persistencia






class Operacion:

    def buscar_objeto(self):
        saver = Persistencia()
        inventario = Inventario()
        for file in os.listdir("./Files"):
            if '.json' in file:
                inventario.agregar_objeto(saver.load_json(file))
        opcion = int(input("\nIngrese el numero 1 para buscar mascotas \n"
                           "Ingrese el numero 2 para buscar Accesorios\n"
                           "Ingrese el numero 3 para buscar Cuidadores\n-->"))

        if opcion == 1:
            valor = input("\nIngrese el valor por el cual desea buscar la mascota\n-->")
            if valor == 'id':
                id = str(input("\nIngrese el id de la mascota\n-->"))

                if len(list(inventario.buscar_mascota_id(id))) == 0:
                    print("\nNo hay Mascotas registradas con ese id\n")
                else:
                    print("\nEncontrado!!!!! :D\n")
                    print(list(inventario.buscar_mascota_id(id)))

                """espec = Especificacion()
                espec.agregar_parametro('id', id)
                if len(list(Inventario.buscar_mascota(espec))) == 0:
                    "No se encuentra registrado"

                else:
                    print(list(Inventario.buscar_mascota(espec)))"""

            if valor == 'nombre':
                nombre = input("\nIngrese el nombre de la mascota\n-->")

                if len(list(inventario.buscar_mascota_nombre(nombre))) == 0:
                    print("\nNo hay Mascotas registradas con ese nombre\n")
                else:
                    print("\nEncontrado!!!!! :D\n")
                    print(list(inventario.buscar_mascota_nombre(nombre)))

            if valor == 'edad':
                edad = int(input("\nIngrese la edad de la mascota\n-->"))
                if len(list(inventario.buscar_mascota_edad(edad))) == 0:
                    print("\nNo hay Mascotas registradas con esa edad\n")
                else:
                    print("\nEncontrado!!!!! :D\n")
                    print(list(inventario.buscar_mascota_edad(edad)))

            if valor == 'color':
                color = input("\nIngrese el color de la mascota\n-->")
                if len(list(inventario.buscar_mascota_color(color))) == 0:
                    print("\nNo hay Mascotas registradas con ese color\n")
                else:
                    print("\nEncontrado!!!!! :D\n")
                    print(list(inventario.buscar_mascota_color(color)))

            if valor == 'peso':
                peso = float(input("\nIngrese el peso de la mascota\n-->"))
                if len(list(inventario.buscar_mascota_peso(peso))) == 0:
                    print("No hay Mascotas registradas con ese peso")
                else:
                    print("Encontrado!!!!! :D")
                    print(list(inventario.buscar_mascota_peso(peso)))

            if valor == 'precio':
                precio = float(input("\nIngrese el precio de la mascota\n-->"))
                if len(list(inventario.buscar_mascota_precio(precio))) == 0:
                    print("\nNo hay Mascotas registradas con ese precio\n")
                else:
                    print("\nEncontrado!!!!! :D\n")
                    print(list(inventario.buscar_mascota_precio(precio)))

            if valor == 'raza':
                raza = input("\nIngrese la raza de la mascota\n-->")
                if len(list(inventario.buscar_mascota_raza(raza))) == 0:
                    print("\nNo hay Mascotas registradas con ese raza\n")
                else:
                    print("\nEncontrado!!!!! :D\n")
                    print(list(inventario.buscar_mascota_raza(raza)))

            if valor == 'longitud':
                longitud = float(input("\nIngrese la longitud de la mascota\n-->"))
                if len(list(inventario.buscar_mascota_longitud(longitud))) == 0:
                    print("\nNo hay Mascotas registradas con esa longitud\n")
                else:
                    print("\nEncontrado!!!!! :D\n")
                    print(list(inventario.buscar_mascota_longitud(longitud)))




        elif opcion == 2:
            valor = input("\nIngrese el valor por el cual desea buscar el Accesorio\n-->")
            if valor == 'id':
                id = str(input("\nIngrese el id del Accesorio\n-->"))

                if len(list(inventario.buscar_accesosio_id(id))) == 0:
                    print("\nNo hay Accesorios registrados con ese id\n")
                else:
                    print("\nEncontrado!!!!! :D\n")
                    print(list(inventario.buscar_accesosio_id(id)))

            if valor == 'nombre':
                nombre = str(input("\nIngrese el nombre del Accesorio\n-->"))

                if len(list(inventario.buscar_accesosio_nombre(nombre))) == 0:
                    print("\nNo hay Accesorios registrados con ese nombre\n")
                else:
                    print("\nEncontrado!!!!! :D\n")
                    print(list(inventario.buscar_accesosio_nombre(nombre)))

            if valor == 'descripcion':
                descripcion = str(input("\nIngrese la descripcion del Accesorio\n-->"))

                if len(list(inventario.buscar_accesosio_descripcion(descripcion))) == 0:
                    print("\nNo hay Accesorios registrados con esa descripcion\n")
                else:
                    print("\nEncontrado!!!!! :D\n")
                    print(list(inventario.buscar_accesosio_descripcion(descripcion)))

            if valor == 'precio':
                precio = int(input("\nIngrese el precio del Accesorio\n-->"))

                if len(list(inventario.buscar_accesosio_precio(precio))) == 0:
                    print("\nNo hay Accesorios registrados con ese precio\n")
                else:
                    print("\nEncontrado!!!!! :D\n")
                    print(list(inventario.buscar_accesosio_precio(precio)))

            if valor == 'tipo mascota':
                tipo_mascota = str(input("\nIngrese el tipo mascota del Accesorio\n-->"))

                if len(list(inventario.buscar_accesosio_tipoM(tipo_mascota))) == 0:
                    print("\nNo hay Accesorios registrados con ese tipo mascota\n")
                else:
                    print("\nEncontrado!!!!! :D\n")
                    print(list(inventario.buscar_accesosio_tipoM(tipo_mascota)))




        elif opcion == 3:
            valor = input("\nIngrese el valor por el cual desea buscar el Cuidador\n-->")
            if valor == 'cedula':
                cedula = str(input("\nIngrese la cedula del Cuidador\n-->"))

                if len(list(inventario.buscar_cuidador_cedula(cedula))) == 0:
                    print("\nNo hay Cuidadores registrados con esa cedula\n")
                else:
                    print("\nEncontrado!!!!! :D\n")
                    print(list(inventario.buscar_cuidador_cedula(cedula)))

            if valor == 'nombre':
                nombre = str(input("\nIngrese el nombre del Cuidador\n-->"))

                if len(list(inventario.buscar_cuidador_nombre(nombre))) == 0:
                    print("\nNo hay Cuidadores registrados con ese nombre\n")
                else:
                    print("\nEncontrado!!!!! :D\n")
                    print(list(inventario.buscar_cuidador_nombre(nombre)))

            if valor == 'apellido':
                apellido = str(input("\nIngrese el apellido del Cuidador\n-->"))

                if len(list(inventario.buscar_cuidador_apellido(apellido))) == 0:
                    print("\nNo hay Cuidadores registrados con ese apellido\n")
                else:
                    print("\nEncontrado!!!!! :D\n")
                    print(list(inventario.buscar_cuidador_apellido(apellido)))

            if valor == 'edad':
                edad = int(input("\nIngrese la edad del Cuidador\n-->"))

                if len(list(inventario.buscar_cuidador_edad(edad))) == 0:
                    print("\nNo hay Cuidadores registrados con esa edad\n")
                else:
                    print("\nEncontrado!!!!! :D\n")
                    print(list(inventario.buscar_cuidador_edad(edad)))

            if valor == 'telefono':
                telefono = str(input("\nIngrese el telefono del Cuidador\n-->"))

                if len(list(inventario.buscar_cuidador_telefono(telefono))) == 0:
                    print("\nNo hay Cuidadores registrados con ese telefono\n")
                else:
                    print("\nEncontrado!!!!! :D\n")
                    print(list(inventario.buscar_cuidador_telefono(telefono)))

            if valor == 'direccion':
                direccion = str(input("\nIngrese la direccion del Cuidador\n-->"))

                if len(list(inventario.buscar_cuidador_direccion(direccion))) == 0:
                    print("\nNo hay Cuidadores registrados con esa direccion\n")
                else:
                    print("\nEncontrado!!!!! :D\n")
                    print(list(inventario.buscar_cuidador_direccion(direccion)))




    def vender(self):
        saver = Persistencia()
        inventario = Inventario()
        for file in os.listdir("./Files"):
            if '.json' in file:
                inventario.agregar_objeto(saver.load_json(file))
        opcion = int(input("\nIngrese el numero 1 para vender mascotas \n"
                           "Ingrese el numero 2 para vender Accesorios\n-->"))

        if opcion == 1:

            id = str(input("\nIngrese el id de la mascota\n-->"))
            if len(list(inventario.buscar_mascota_id(id))) == 0:
                print("\nNo hay Mascotas registradas con ese id")
            else:
                print("\nVendido!!!!! :D")
                os.remove('Files/' + id + '.json')
                inventario.eliminar_listas()


        if opcion == 2:

            id = str(input("\nIngrese el id del Accesorio\n-->"))
            if len(list(inventario.buscar_accesosio_id(id))) == 0:
                print("\nNo hay Accesorios registrados con ese id")
            else:
                print("\nVendido!!!!! :D")
                os.remove('Files/' + id + '.json')
                inventario.eliminar_listas()






