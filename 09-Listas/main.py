"""
LISTAS (arrays)

Son colecciones o conjuntos de datos/valores, bajo un único nombre.
Para acceder a esos valores podemos usar un índice numérico.

"""

pelicula ="Batman"

peliculas = ["Batman","Spiderman", "El Señor de los anillos","Hello"]

# Tupla -> no se puede modificar
cantantes = list(('2pac','Drake', 'Jennifer López',"Phill"))

# Rango de números
years = list(range(2020,2050))
variada = ["Victor", 10,4.4, True, "Texto"]

# print(peliculas)
# print(cantantes)
# print(years)
# print(variada)

# Índices positivos de izquierda 0
# De derecha a izquierda se comienza con -1
# Se reemplaza el valor del índice 1
peliculas[1] ="Gran Torino"
print(peliculas)
print(peliculas[0])
print(peliculas[-1])
print(peliculas[1:3])
print(peliculas[1:])

# Añadir Elemento a lista
cantantes.append("KC")
print(cantantes)

# # Recorrer y mostrar una lista
# print("\n############# LISTADO PELÍCULAS ##############")

# nueva_pelicula =""
# while nueva_pelicula != "parar":
#     nueva_pelicula = input("Introduce la nueva película: ")
#     if nueva_pelicula != "parar":
#         peliculas.append(nueva_pelicula)

# for pelicula in peliculas:
#     print(f"{peliculas.index(pelicula) + 1}: {pelicula}")

# Listas multidimensionales
print("\n############# LISTADO DE CONTACTOS ##############")

contactos = [
    ["Mario","mario@gmail.com"],
    ["Claudia","claudia@gmail.com"],
    ["Rodrigo","rodrigo@gmail.com"]
]

# for contacto in contactos:
#     for elemento in contacto:
#         print(elemento)
#     print("\n")
#     # print(contacto[0])
# # print(contactos[1][0])

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")
