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

# Ejemplo tablas de multiplicar
print("\n##################### EJEMPLO ######################")

numero_usuario = int(input("¿De qué número quieres la tabla?: "))

if numero_usuario < 1:
   numero_usuario = 1
print(f"\n############### Tabla de multiplicar del número {numero_usuario}")

for numero_tabla in range(1,11):
    if numero_usuario == 45:
        print("No se puede mostrar. El número ingresado está prohibido!!")
        break
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("Tabla finzalizada")