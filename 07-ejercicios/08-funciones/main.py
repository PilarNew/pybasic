"""
FUNCIONES:
Una fn es un cjto de instrucciones agrupadas bajo un nombre concreto que pueden reutilizarse invocando a la fn tantas veces como ea necesario 

def nombreDeMiFuncion(parámetros):
    # BLOQUE / CJTO DE INSTRUCCIONES

nombreDeMiFuncion(mi_parametro)

"""

# Ejemplo 1
print("######### EJEMPLO 1 ########")

# Definición de función
def muestraNombre():
    print("Pilar")
    print("Pedro")
    print("Pancho")
    print("Petronia")
    print("Paco")
    print("Paz")
    print("\n")

# Invocación de la función
muestraNombre()
muestraNombre()
muestraNombre()

# Ejemplo 2 Parámetros
print("######### EJEMPLO 2 ########")

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

def muestraTuNombre(data,edad):
    print(f"Hola {data}")
    if edad > 18:
        print(f"{data} eres mayor de edad")

muestraTuNombre(nombre,edad)

# Ejemplo 3
print("######### EJEMPLO 3 ########")

def tabla(numero):
    print(f"Tabla de multiplicar de: {numero}")

    for contador in range(11):
        operacion = numero*contador
        print(f"{numero}*{contador}= {operacion}")
    print("\n")

tabla(3)
tabla(7)

# Ejemplo 3.1

for numero_tabla in range(1,11):
    tabla(numero_tabla)