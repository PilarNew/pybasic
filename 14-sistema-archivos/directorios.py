import os,shutil

# Crear una carpeta

if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Ya existe el directorio")


# Eliminar carpeta

# os.rmdir("./mi_carpeta")

"""
# COPIAR
ruta_original = "./14-sistema-archivos/mi_carpeta"
ruta_nueva = "./14-sistema-archivos/mi_carpeta_COPIADA"
shutil.copytree(ruta_original,ruta_nueva)
"""
"""
# ELIMINAR CARPETA
os.rmdir("./14-sistema-archivos/mi_carpeta_COPIADA")
"""

print("::::::  CONTENIDO DE MI CARPETA ::::::::")

contenido = os.listdir("./14-sistema-archivos/mi_carpeta")

for carpeta in contenido:
    print("Archivo: ",carpeta)