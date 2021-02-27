"""
SET es un tipo de dato, para tener una colección de valores, pero no tiene índice ni orden
"""

personas ={"Pili","Victor", "Mario", "Nayi"}

# Va cambiando el orden con cada impresión
print(personas)

print(type(personas))

personas.add("paty")
print(personas)

personas.remove("Victor")
print(personas)