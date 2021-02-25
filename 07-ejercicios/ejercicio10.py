"""
Ejercicio 10

- El programa tiene que pedir la nota de 15 alumnos y sacar por pantalla cuántos han aprobado y cuántos has suspendido

"""

contador = 1
aprobados = 0
reprobados = 0

numero_alumnos = int(input("¿Cuántos alumnos tienes?: "))

while contador <= numero_alumnos:
    nota = int(input(f'¿Qué nota quieres ponerle al \"alumno {contador}\" ?: '))

    if nota >= 4:
        aprobados +=1
    else:
        reprobados +=1

    contador += 1

print(f"Tienes {aprobados} alumnos aprobados y {reprobados} alumnos reprobados")