nombre = "Pilar"

# Funciones generales
print(type(nombre))

# Detectar el tipado
comprobar = isinstance(nombre,int)

if comprobar:
    print("Esta variable es un string")
else:
      print("Esta variable NO es un string")

if not isinstance(nombre,float):
       print("Esta variable NO es un número decimal")

# Limpiar espacios
frase = "     mi contenido"
print(frase)
print(frase.strip())

# Eliminar variables
year= 2022
print(year)
del year
# print(year)

# Comprobar variable vacía
texto = "   ff   "

if len(texto) <= 0:
    print("La variable está vacía")
else:
    print("La variable tiene cotenido",str(len(texto)) + " " + "caracteres")

# Encontrar Caracteres
frase = "La vida es bella"
print(frase.find("vida")) #Comienza en el tercer caracter partiendo de 0

# Reemplazar palabras en un string
nueva_frase = frase.replace("vida","muerte")
print(nueva_frase)

# Mayússculas y minúsculas
print(nombre)
print(nombre.lower())
print(nombre.upper())

