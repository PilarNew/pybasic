def mi_funcion(nombre):
    return "Hola que tal" + " " + nombre

def mi_segunda_funcion(apellido):
    return "Hola que tal 2" + " " + apellido

# Variables deben estar definidas antes de ejecutar funciones que las emplean
nombre = "Pilar"
apellido = "Gonzalez"

# print("Hola Mundo")
# print(f"Bienvenido {nombre}")

print(mi_funcion(nombre))
print(mi_segunda_funcion(apellido))