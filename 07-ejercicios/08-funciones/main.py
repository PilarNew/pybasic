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
