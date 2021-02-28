"""
Ejercicio 1
- Crear una lista que contenga 8 números enteros y haga lo sigiente
- Recorrer la lista y mostrarla
- Hacer una función que recorra lista de números y devuelva un string
- Mostrar su longitud
- Ordenarla y mostrarla
- Buscar algún elemento que el usuario diga por teclado
"""

"""
# Se crea lista
numeros = [100,20,15,4000,56,88]

# Se recorre y se muestra los números
def mostrarLista(listas):
    resultado = ""
    for lista in listas:
        resultado += "Elemento: " + str(lista)
        resultado += "\n"
    return resultado      

print(mostrarLista(numeros))
print(mostrarLista(["Hugo", "Paco", "Luis"]))
# Recorrer y mostrar
# print("\n############## Recorrer y Mostrar ###############")
# for numero in numeros:
#     print(numero)

# Se muestra longitud
print(len(numeros))

# Ordenar y mostrar
numeros.sort()
print(mostrarLista(numeros))

# Búsqueda en la lista
buscado = int(input("Ingresa número: "))

comprobar = isinstance(buscado,int)

while not comprobar or buscado <= 0:
    buscado = int(input("Ingresa número: "))
else:
    print(f"Has introducido el {buscado}")

print(f"########## Buscar en la lista {buscado} ###########")

search = numeros.index(buscado)
print(f"El número buscado existe en la lista es el ínice {search}; {numeros[search]}")

"""

# Múltiples excepciones
try:
    numero = int(input("Número para calcular el cuadrado: "))
    print("Esl cuadrado es: " + str(numero*numero))
except TypeError:
    print("Debes convertir tus cadenas a enteros!!!")
# except ValueError:
#     print("Introduce un número correcto!!!")
except Exception as e:
    print("Ha ocurrido un error: ", type(e).__name__)





