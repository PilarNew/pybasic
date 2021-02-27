"""
EJERCICIO 5
- Crear una lista con el contenido de la tabla:
ACCIÓN  AVENTURA    DEPORTES
GTA     ASSINS      FIFA 21
COD     CRASH       PRO 21
PUGB    POP         MOTO GP 21

- Mostrar información ordenada
"""

tabla = [
    {
    "categoria": "ACCIÖN",
    "juegos":["GTA","COD","PUGB"]
    },
    {
    "categoria": "AVENTURA",
    "juegos":["GTA","COD","PUGB"]
    },
    {
    "categoria": "ACCIÖN",
    "juegos":["GTA","COD","PUGB"]
    }
]

for elemento in tabla:
    print(f"---------- CATEGORIA {elemento['categoria']} ---------")
    for juego in elemento['juegos']:
        print(juego)
