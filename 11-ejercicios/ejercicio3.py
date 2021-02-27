"""
EJERCICIO 3
- Crear programa que compruebe si una variable está vacía, y si está vacía, rellenarla con texto en minúsculas y mostrarlo en mayúaculas
"""

texto = " "

# Método strip para eliminar espacios

if len(texto.strip()) <= 0:
    texto = "hola soy un texto en minúsculas"
    print(texto.upper())
else:
    print(f"La variable tiene contenido {texto}")