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