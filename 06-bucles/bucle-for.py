"""
# FOR

for variable in elemento_iterable (lista, rango, etc)
    BLOQUE DE INSTRUCCIONES
"""
contador = 0
resultado = 0

for contador in range(0,5):
    print(f"voy en el {str(contador)}")
    resultado += contador
# Por la identación sólo se muestra el último valor de la variable resultado
print(f"El resultado es: {resultado}")