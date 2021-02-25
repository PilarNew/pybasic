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
    
"""

# Ejemplo 1

print("################ EJENPLO 1 ################")

# color = "azul"
color = input("Adivina cuál es mi color favorito: ")
if color == "rojo":
    print("Has adivinado el color")
    print("El color es rojo")
else: 
    print(f"El color no es {color}")
    print("El color es incorrecto")