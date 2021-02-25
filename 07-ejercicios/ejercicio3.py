"""
Ejercicio 3

- Escribir un programa que muestre los cuadrados (un número  multiplicado por sí mismo) de los 60 primeros números naturales.
- Resolverlo con for y con while

"""
# FOR
contador = 1
for contador in range(1,61):
    multiplicacion = contador*contador
    print(multiplicacion)

# WHILE
# contador = 1

# while contador < 61:
#     multiplicacion = contador * contador
#     print(multiplicacion)
#     contador += 1