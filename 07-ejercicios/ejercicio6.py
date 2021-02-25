"""
Ejercicio 6
- Mostrar todas las tablas de multiplicar del 1 al 10.
- Mostrando el título de la tabla y luego
"""
for titulo in range(1,11):
    print("################################")
    print(f"######TABLA DEL {titulo} #######")
    print("################################")

    for numero in range(1,11):
        print(f"{numero} * {titulo} = {numero*titulo}")
    
    print("\n")