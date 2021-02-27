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