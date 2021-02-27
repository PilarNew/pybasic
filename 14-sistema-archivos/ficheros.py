from io import open

import pathlib,shutil

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
"""
# COPIAR
ruta_original = str(pathlib.Path().absolute())+"/14-sistema-archivos/archivo_texto.txt"
ruta_nueva = str(pathlib.Path().absolute())+"/archivo_copiado_texto.txt"
shutil.copyfile(ruta_original,ruta_nueva)
"""

"""
# MOVER
# Cambia el archivo de posición y lo pone en otro directorio cambiándole el nombre
ruta_original = str(pathlib.Path().absolute())+"/14-sistema-archivos/archivo_texto.txt"
ruta_nueva = str(pathlib.Path().absolute())+"/archivo_copiado_texto_NUEVO.txt"

shutil.move(ruta_original,ruta_nueva)
"""
"""
# ELIMINAR ARCHIVOS
import os

ruta_nueva = str(pathlib.Path().absolute())+"/archivo_copiado_texto_NUEVO.txt"

os.remove(ruta_nueva)
"""
# COMPROBACIÓN DE QUE UN ARCHIVO EXISTE
import os.path
# print(os.path.abspath("./"))
# print(os.path.abspath("../"))

ruta_comprobar = os.path.abspath("./")+"/14-sistema-archivos/archivo_texto1.txt"
ruta_relativa = "./14-sistema-archivos/archivo_texto1.txt"
if os.path.isfile(ruta_relativa):
    print("El arachivo existe")
else:
     print("El arachivo NO existe")