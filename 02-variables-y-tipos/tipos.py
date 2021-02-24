# Indica que la variable tiene nada
nada = None
cadena = "Hola soy Pilar"
entero = 99
flotante = 4.2
booleano = False
lista = [10,20,"hola"] #array de diferentes tipos de datos
tupla = (10,20,30) # Es como una lista que deben ser del mismo tipo
diccionario = {
    "nombre": "Pilar",
    "apellido": "González",
    "edad": "?"
}

rango = range(9)

dato_byte = b"Probando"
# Se imprimen variables
print(nada)
print(cadena)
print(entero)
print(flotante)
print(booleano)
print(lista)
print(tupla)
print(diccionario)
print(rango)
print(dato_byte)

# Mostrar tipo de dato
print(type(nada)) # NoneType
print(type(cadena)) # str
print(type(entero)) # int
print(type(flotante)) # float
print(type(booleano)) # bool
print(type(lista)) # list
print(type(tupla)) # tuple
print(type(diccionario)) # dict
print(type(rango)) # range
print(type(dato_byte)) # bytes