"""
Ejercicio 8

- Calcular el x% de x número
"""

numero = int(input("Introduce el número: "))
porcentaje = int(input(f"¿Qué porcentaje quieres sacar de {numero}?: "))

calculo = numero*porcentaje/100
print(f"El {porcentaje}% de {numero} es {calculo}")