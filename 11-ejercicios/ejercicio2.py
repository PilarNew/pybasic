"""
EJERCICIO 2
- Escribir programa que añada valores a una lista mientras que su longitud sea menor a 12 y luego mostrar la lista
- Plus: Usar while y for

"""
# coleccion = []

# for contador in range(0,12):
#     coleccion.append(f"elemento - {contador}")
#     print("Mostrando el " + coleccion[contador])
# print(coleccion)
coleccion = []
contador = 0
while contador < 12:
    coleccion.append(f"elemento - {contador}")
    print("Mostrando el " + coleccion[contador])
    contador +=1