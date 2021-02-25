# """
# FUNCIONES:
# Una fn es un cjto de instrucciones agrupadas bajo un nombre concreto que pueden reutilizarse invocando a la fn tantas veces como ea necesario 

# def nombreDeMiFuncion(parámetros):
#     # BLOQUE / CJTO DE INSTRUCCIONES

# nombreDeMiFuncion(mi_parametro)

# """

# # Ejemplo 1
# print("######### EJEMPLO 1 ########")

# # Definición de función
# def muestraNombre():
#     print("Pilar")
#     print("Pedro")
#     print("Pancho")
#     print("Petronia")
#     print("Paco")
#     print("Paz")
#     print("\n")

# # Invocación de la función
# muestraNombre()
# muestraNombre()
# muestraNombre()

# # Ejemplo 2 Parámetros
# print("######### EJEMPLO 2 ########")

# nombre = input("Ingresa tu nombre: ")
# edad = int(input("Ingresa tu edad: "))

# def muestraTuNombre(data,edad):
#     print(f"Hola {data}")
#     if edad > 18:
#         print(f"{data} eres mayor de edad")

# muestraTuNombre(nombre,edad)

# # Ejemplo 3
# print("######### EJEMPLO 3 ########")

# def tabla(numero):
#     print(f"Tabla de multiplicar de: {numero}")

#     for contador in range(11):
#         operacion = numero*contador
#         print(f"{numero}*{contador}= {operacion}")
#     print("\n")

# tabla(3)
# tabla(7)

# # Ejemplo 3.1

# for numero_tabla in range(1,11):
#     tabla(numero_tabla)


# # Ejemplo 4 -  Parámetros opcionales
# print("######### EJEMPLO 4 ########")


# def getEmpleado(nombre,run=None):
#     print("EMPLEADO")
#     print(f"Nombre: {nombre}")
#     if run != None:
#         print(f"RUN: {run}")

# getEmpleado("Pilar","333333")


# # Ejemplo 5 -  Return - Parámetros opcionales
# print("######### EJEMPLO 5 ########")

# def saludame(nombre):
#     saludo = f"Hola saludos {nombre}"
#     return saludo

# print(saludame("Nana"))


# # Ejemplo 6
# print("\n######### EJEMPLO 6 ########")

# def calculadora(numero1,numero2,basicas = False):
#     suma = numero1 + numero2
#     resta = numero1 - numero2
#     division = numero1 / numero2
#     multiplicacion = numero1 * numero2

#     cadena ="" 

#     if basicas != False:
#         cadena += "Suma: " + str(suma)
#         cadena += "\n"
#         cadena += "Resta: " + str(resta)
#         cadena += "\n"
#     else:
#         cadena += "Suma: " + str(suma)
#         cadena += "\n"
#         cadena += "Resta: " + str(resta)
#         cadena += "\n"
#         cadena += "Multiplicación: " + str(multiplicacion)
#         cadena += "\n"
#         cadena += "División: " + str(division)
#         cadena += "\n"

#     return cadena
   

    
    
# print(calculadora(5,5))


# Ejemplo 7
print("\n######### EJEMPLO 7 ########")

def getNombre(nombre):
    texto = f"El nombre es {nombre}"
    return texto

def getApellido(apellido):
    texto = f"Los apellidos son: {apellido}"
    return texto

def devuelveTodo(nombre,apellido):
    texto = getNombre(nombre) + "\n" + getApellido(apellido)
    return texto

print(devuelveTodo('Pilar','González Mann'))