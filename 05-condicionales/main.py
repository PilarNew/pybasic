# Estructura de control que permite controlar el flujo del programa
"""
# IF

SI se_cumple_esta_condicion:
    Ejecutar grupo de instrucciones

SI NO:
    Se ejecutan otro grupo de instrucciones

if condicion:
    instrucciones
else:
    otras instrucciones
    

# Operadores de Comparación

== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

# Operadores lógicos

and = y
or = o
! = negación
not = no
"""

# Ejemplo 1
print("################ EJENPLO 1 ################")

color = "azul"
# color = input("Adivina cuál es mi color favorito: ")
if color == "rojo":
    print("Has adivinado el color")
    print("El color es ROJO")
else: 
    print(f"El color no es {color}")
    print("El color es incorrecto")


# Ejemplo 2
print("\n################ EJENPLO 2 ################")

year = 2020
# year = int(input("¿En qué año estamos?: "))
if year >= 2021:
    print("Estamos de 2021 en adelante!!")
else: 
    print("Es un año anterior a 2021")

# Ejemplo 3
print("\n################ EJENPLO 3 ################")

nombre = input("¿Cuál es tu nombre?: ")
continente = input("¿En qué continente vives?: ")
ciudad = input("¿En qué ciudad vives?: ")
edad = input(("Qué edad tienes?: "))
mayoria_edad = 18

if int(edad) >= mayoria_edad:
    print(f"{nombre} es mayor de edad")
    if continente == "Europa":
        print(f"Es europeo y de {ciudad}")
    else:
        print(f"El usuario no es Europeo, es de {ciudad} en {continente}")
else:
    print(f"{nombre} no es mayor de edad")


# Ejemplo 4
print("\n################ EJENPLO 4 ################")

dia = int(input("Introduce el número del día de la semana: "))

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miércoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
elif dia == 6:
    print("Es sábado")
else:
    print("Es domingo")

# Ejemplo 5
print("\n################ EJENPLO 5 ################")

edad_minima = 18
edad_maxima = 60
edad_oficial = int(input("Introduce tu edad: "))
# Operadores lógico
if edad_oficial>=edad_minima and edad_oficial <= edad_maxima:
    print("Estás en edad de trabajar")
else:
    print("No estás en edad de trabajar")


# Ejemplo 6
print("\n################ EJENPLO 6 ################")

pais = "Alemania"

if pais == "México" or pais == "España" or pais == "Chile":
    print(f"{pais} es país hispano parlante")
else:
    print(f"{pais} NO es país hispano parlante")

# Ejemplo 7
print("\n################ EJENPLO 7 ################")

pais = "España"

if not (pais == "México" or pais == "España" or pais == "Chile"):
    print(f"{pais} NO es país hispano parlante")
else:
    print(f"{pais} es país hispano parlante")

# Ejemplo 8
print("\n################ EJENPLO 8 ################")

pais = "Chile"

if pais != "México" and pais != "España" and pais != "Chile":
    print(f"{pais} NO es país hispano parlante")
else:
    print(f"{pais} es país hispano parlante")