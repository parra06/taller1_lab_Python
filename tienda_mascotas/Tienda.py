import os
import uuid

from tienda_mascotas.Dominio.Cuidador import Cuidador
from tienda_mascotas.Dominio.Especificacion import Especificacion
from tienda_mascotas.Dominio.Inventario import Inventario
from tienda_mascotas.Infraestructura.Operacion import Operacion
from tienda_mascotas.Dominio.Perro import Perro
from tienda_mascotas.Dominio.Configuracion import Configuracion
from tienda_mascotas.Dominio.Gato import Gato
from tienda_mascotas.Dominio.Hamster import Hamster
from tienda_mascotas.Dominio.Accesorio import Accesorio
from tienda_mascotas.Infraestructura.Persistencia import Persistencia

config = ""
def cargar_file():
    global config
    inventario.eliminar_listas()
    for file in os.listdir("./Files"):
        if '.json' in file:
            inventario.agregar_objeto(saver.load_json(file))

    for file in os.listdir("./config"):
        if '.json' in file:
            config=saver.load_json_config(file)

if __name__ == "__main__":
    saver = Persistencia()
    saver.connect()
    inventario = Inventario()
    cargar_file()
    operacion = Operacion()

    continuar=True
    print(config.valor)
    while continuar:

        if config.valor == 'bd':

            valor = int(input("\nEsta configurado para guardar en base de datos\n\n"
                          "Ingrese el numero 1 para continuar con esta configuracion \n"
                          "Ingrese el numero 2 para guardar con serializacion\n-->"))

            if valor == 2:
                os.remove('config/' + config.valor + '.json')
                config.cambiar_valor('sr')
                print("\nConfigurado con serializacion\n")
            else:
                print("\nConfigurado con base de datos\n")



        else:
            valor = int(input("\nEsta configurado para guardar con serializacion\n"
                              "Ingrese el numero 1 para continuar con esta configuracion \n"
                              "Ingrese el numero 2 para guardar con base de datos\n-->"))

            if valor == 2:
                os.remove('config/' + config.valor + '.json')
                config.cambiar_valor('bd')
                print("\nConfigurado con base de datos\n")

            else:
                print("\nConfigurado con serializacion\n")

        saver.save_json(config)

        opcion = int(input("\nPara ver inventarios ingrese 1\n"
                               "Para guardar una mascota ingrese 2\n"
                           "Para guardar un Accesorio ingrese 3\n"
                           "Para guardar un Cuidador ingrese 4\n"
                           "Para buscar Ingrese 5\n"
                           "Para vender un Accesorio o una mascota ingrese 6\n"
                           "Para salir ingrese 7\n-->"))

        if opcion==1:
            cargar_file()
            opcion1=int(input("\nPara ver inventario Mascotas ingrese 1\n"
                               "Para ver inventario Accesorios ingrese 2\n"
                           "Para ver inventario Cuidadores ingrese 3\n"
                              "Para ver todos los inventarios ingrese 4\n-->"))
            if opcion1 == 1:
                if(len(list(inventario.mascotas)))==0:
                    print("\nNo hay Macotas en el Inventario\n")
                else:
                    print("\nInventario Mascotas\n")
                    print(inventario.mascotas)
            if opcion1 == 2:
                if (len(list(inventario.accesorios))) == 0:
                    print("\nNo hay Accesorios en el Inventario\n")
                else:
                    print("\nInventario Accesorios\n")
                    print(inventario.accesorios)
            if opcion1 == 3:
                if (len(list(inventario.cuidadores))) == 0:
                    print("\nNo hay Cuidadores en el Inventario\n")
                else:
                    print("\nInventario Cuidadores\n")
                    print(inventario.cuidadores)
            if opcion1 == 4:
                if (len(list(inventario.mascotas))) == 0:
                    print("\nNo hay Macotas en el Inventario\n")
                else:
                    print("\nInventario Mascotas\n")
                    print(inventario.mascotas)

                if (len(list(inventario.accesorios))) == 0:
                    print("\nNo hay Accesorios en el Inventario\n")
                else:
                    print("\nInventario Accesorios\n")
                    print(inventario.accesorios)

                if (len(list(inventario.cuidadores))) == 0:
                    print("\nNo hay Cuidadores en el Inventario\n")
                else:
                    print("\nInventario Cuidadores\n")
                    print(inventario.cuidadores)



        if opcion == 2:
            opcion2=int(input("\nPara guardar un Perro ingrese 1\n"
                               "Para guardar un Gato ingrese 2\n"
                           "Para guardar un Hamster ingrese 3\n-->"))
            if opcion2 == 1:
                print("\n")
                nombre = input("Nombre: ")
                raza = input("Raza: ")
                edad = int(input("Edad: "))
                color = input("Color: ")
                peso = float(input("Peso: "))
                precio = float(input("Precio: "))
                perro = Perro(nombre,raza,edad,color,peso,precio)
                if config.valor == 'bd':
                    saver.guardar_bd(perro)

                else:
                    saver.save_json(perro)


            if opcion2 == 2:
                print("\n")
                nombre = input("Nombre: ")
                raza = input("Raza: ")
                edad = int(input("Edad: "))
                color = input("Color: ")
                peso = float(input("Peso: "))
                precio = float(input("Precio: "))
                gato = Gato(nombre,raza,edad,color,peso,precio)
                if config.valor == 'bd':
                    saver.guardar_bd(gato)
                else:
                    saver.save_json(gato)

            if opcion2 == 3:
                print("\n")
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                color = input("Color: ")
                peso = float(input("Peso: "))
                longitud = float(input("Longitud: "))
                precio = float(input("Precio: "))
                hamster = Hamster(nombre,edad,color,peso,longitud,precio)
                if config.valor == 'bd':
                    saver.guardar_bd(hamster)
                else:
                    saver.save_json(hamster)
        cargar_file()
        if opcion == 3:
            print("\n")
            nombre = input("Nombre: ")
            descripcion = input("Descripcion: ")
            precio = float(input("Precio: "))
            tipo_mascota = input("Tipo Mascota: ")
            accesorio = Accesorio(nombre,descripcion,precio,tipo_mascota)
            if config.valor == 'bd':
                saver.guardar_bd(accesorio)
            else:
                saver.save_json(accesorio)
                cargar_file()
        if opcion == 4:
            print("\n")
            cedula = input("Cedula: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            edad = int(input("Edad: "))
            telefono = input("Telefono: ")
            direccion = input("Direccion: ")

            cuidador = Cuidador(cedula,nombre,apellido,edad,telefono,direccion)
            if config.valor == 'bd':
                saver.guardar_bd(cuidador)
            else:
                saver.save_json(cuidador)
                cargar_file()
        if opcion == 5:
            print("\n")
            operacion.buscar_objeto()

        if opcion == 6:
            print("\n")
            operacion.vender()

        if opcion == 7:
            continuar = False








    #g = Gato("Juanito","Siames",4,"Negro",5,35000)
    """p = Perro("Mapache", "Pitbull",1,"Blanco y Negro",9, 2000)"""
    #h= Hamster("Pedro",1,"Amarillo",0.5,10,15000)
    """saver.guardar_bd(g)
    saver.guardar_bd(p)
    saver.guardar_bd(h)"""
    #a = Accesorio("Hueso","Hueso para que el perro fortalezca sus dientes",10000, "Perro" )
    """saver.guardar_bd(a)"""

    #c = Cuidador("5555555","Santiago","Parra",20,"31138369","Cra 10 bla bla")
    """#saver.guardar_bd(c)"""

    #p = Perro("Mapache", "Pitbull", 1, "Blanco y Negro", 9, 2000)
    """p1 = Perro("Lucas", "Pitbull", 1, "Blanco y Negro", 9, 2000)
    g = Gato("Juanito", "Siames", 4, "Negro", 5, 35000)
    h = Hamster("Pedro", 1, "Amarillo", 0.5, 10, 15000)
   
    saver.save_json(p1)"""
    #saver.save_json(p)
    #saver.save_json(g)
    #saver.save_json(h)

    #saver.save_json(c)
    #saver.save_json(a)


    """print(inventario.mascotas)






    operacion = Operacion()
    #operacion.buscar_objeto()
    operacion.vender()
    cargar_file()
    print(inventario.mascotas)"""








