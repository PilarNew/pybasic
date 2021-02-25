"""
Ejercicio 5
- Hacer un programa que muestre todos los números entre dos números que ingrese el usuario
"""
numero_1 = int(input("Ingrese primer número: "))
numero_2 = int(input("Ingrese segundo número: "))
contador = numero_1 + 1

if numero_1 < numero_2:
    contador = numero_1 + 1
    while contador < numero_2:
            print(contador)
            contador += 1

else:
    print("El primer número tiene que ser menor que el segundo número" )
