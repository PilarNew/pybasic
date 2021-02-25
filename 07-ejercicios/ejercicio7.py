"""
Ejercicio 4
- Pedir dos números al usuario 
- Hacer todas las operaciones básicas de una calculadora mostrar por pantalla
"""
numero_uno = int(input("Ingresa un número: "))
numero_dos = int(input("ingresa otro número: "))

suma = numero_uno + numero_dos
resta = numero_uno - numero_dos
division = numero_uno / numero_dos
multiplicacion = numero_uno * numero_dos

print("##########CALCULADORA#########")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")