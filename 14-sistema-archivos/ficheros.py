from io import open

import pathlib

# Abrir archivo
# Se crea archivo
archivo = open("14-sistema-archivos/archivo_texto.txt","a+")
# Se abren en el diretorio principal
archivo_uno = open("archivo_texto1.txt","a+")
ruta = str(pathlib.Path().absolute())+"/archivo_texto2.txt"

print(ruta)
archivo_dos = open(ruta,"a+")

# Escribir un archivo
archivo.write("*****Soy un texto escrito desde Python*****\n")

# Cerra archivo

archivo.close()
archivo_uno.close()
archivo_dos.close()

ruta = str(pathlib.Path().absolute())+"/14-sistema-archivos/archivo_texto.txt"
archivo_lectura = open(ruta,"r")

# Leer contenido
# contenido = archivo_lectura.read()
# print(contenido)

# Leer contenido y guardarlo en una lista
lista = archivo_lectura.readlines()
archivo_lectura.close()
for elemento in lista:
    # if not elemento.isnumeric():
    # elemento es cada una de las frases
        print(" - " + elemento.upper())

# SPLIT para convertir una frase en una lista de palabras que conforman la frases
for elemento in lista:
    lista_frase = elemento.split()
    print(lista_frase)

# Centrar contenido

for elemento in lista:
    print("-" + elemento.center(100))