from auto import Auto

carro = Auto("Verde","Renault","Clio",150,200,4)
carro1 = Auto("Rojo","Renault","Clio",150,200,4)
carro2 = Auto("Azul","Renault","Laguna",150,200,4)
carro3 = Auto("Amarillo","citroen","Xara",200,200,4)
print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

# Detectar tipado

if type(carro3) == Auto:
    print("Es un objeto correcto")
else: 
    print("No es un objeto!!!")