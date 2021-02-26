cantantes = ['2pac','Drake', 'Jennifer López',"Phill"]
numeros = [1,2,5,8,3,4,0]

# Ordenar lista
numeros.sort()
print(numeros)

# Añadir elementos
cantantes.append("Ricky")
print(cantantes)

cantantes.insert(1,"Bisbal")
print(cantantes)

# Eliminar elementos
cantantes.pop(1)
print(cantantes)
cantantes.remove("Drake")
print(cantantes)

# Dar la vuelta
numeros.reverse()
print(numeros)

# Buscar dentro de una lista
# Para saber si un elemento se encuentra dentro de una lista
print("2pac" in cantantes)
# Rsponde tru or false

# Contar elementos
print(len(cantantes))

# Cuámtas veces aparece en la lista un elemento
numeros.append(8)
print(numeros.count(8))

# Conseguir índice
print(cantantes.index("2pac"))

# Unir listas
cantantes.extend(numeros)
print(cantantes)