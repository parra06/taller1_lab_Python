from tienda_mascotas.Dominio.Especificacion import Especificacion
from tienda_mascotas.Dominio.Inventario import Inventario
from tienda_mascotas.Dominio.Perro import Perro
import random

def test_fuzzing_buscar_mascotas():
    nombres = ['Lucas', 'Mapache', 'Tyson','Firulais']
    razas = ['Labrador','Pitbull','Pastor Aleman','Pub']
    cantidad_perros= random.randint(100, 1000)
    colores = ['Naranja', 'Amarillo', 'Cafe', 'Blanco', 'Negro']
    edades = [0.5,0.8, 1,2, 3]
    peso = random.randint(0,10)
    precios = ['20000','50000','70000','35000']
    inventario = Inventario()
    especificaciones = []
    for i in range(cantidad_perros):
        nombre = random.choice(nombres)
        raza = random.choice(razas)
        color = random.choice(colores)
        edad = random.choice(edades)
        precio = random.choice(precios)

        if i % 100 == 0:
            especificacion = Especificacion()
            especificacion.agregar_parametro('nombre', nombre)
            especificacion.agregar_parametro('raza', raza)
            especificaciones.append(especificacion)

        p = Perro(nombre,raza,edad,color,peso,precio)
        inventario.agregar_objeto(p)
    cantidad_busquedas = random.randint(1, len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(inventario.buscar_mascota(esp))) > 0
        print('encontradas: ')
        print(list(inventario.buscar_mascota(esp)))
    esp_fake = Especificacion()
    esp_fake.agregar_parametro('dientes', 15)
    print(inventario.mascotas)
    assert len(list(inventario.buscar_mascota(esp_fake))) == 0
    nombre = random.choice(nombres)
    raza = random.choice(razas)
    color = random.choice(colores)
    edad = random.choice(edades)
    precio = random.choice(precios)
    p = Perro(nombre, raza, edad, color, peso, precio)
    inventario.agregar_objeto(p)
    try:
        inventario.agregar_objeto(p)
        assert False
    except Exception as ex:
        assert ex;

if __name__ == '__main__':
    test_fuzzing_buscar_mascotas()
