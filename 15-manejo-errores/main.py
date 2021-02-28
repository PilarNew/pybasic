"""
# Capturar excepciones y manejar errores en código susceptible a fallos/errores

try:
    nombre = input("¿Cuál es tu nombre?: ")

    if len(nombre) > 1:
        nombre_usuario = "El nombre es: " + nombre
        print(nombre_usuario)
except:
    print("Ha ocurrido un error, ingresa correctamente el nombre")
else:
    print("Todo ha funcionado correctamente")
finally:
    print("Fin de la iteración!!!")

# Si no se especificaba un nombre se generaba un error interno, pero con try y except se puede hacer un manejo de errores
"""

# Búsqueda en la lista
numeros = [100,20,15,4000,56,88]
try:
    buscado = int(input("Ingresa número: "))

    comprobar = isinstance(buscado,int)

    while not comprobar or buscado <= 0:
        buscado = int(input("Ingresa número: "))
    else:
        print(f"Has introducido el {buscado}")

    print(f"########## Buscar en la lista {buscado} ###########")


    search = numeros.index(buscado)
    print(f"El número buscado existe en la lista es el ínice {search}; {numeros[search]}")
except:
    print("El número no está en la lista")




