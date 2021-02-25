"""
Ejercicio 7

- Hacer un programa que muestre todos los números impares entre dos números que decida el usuario
"""

numero_uno = int(input("Introduce un número: "))
numero_dos = int(input("Introduce otro número: "))

if numero_uno < numero_dos:

    for x in range(numero_uno,numero_dos + 1):
        if x % 2 == 0:
            print(f"{x} es PAR")
        else:
            print(f"{x} es IMPAR")
else:
    print("El primer número debe ser menor al segundo")