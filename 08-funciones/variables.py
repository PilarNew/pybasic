"""
Variables locales: 
Se definen dentro de la función y no se pueden usar fuera de ella, sólo están disponibles dentro.
A no ser que se haga un return

Variables globales:
Son las que se declaran fuera de un fn y están disponibles dentro y fuera de ellas 

"""

# Variable Local

frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"

print(frase)

def holaMundo():
  #  frase = "Hola Mundo"
  # Al comentar frase local el print local toma la frase global
    print(frase)

    year = 2021
    print(year)
    
    global website
    website = "udemy.com"
    print("Dentro: ", website)
    
    return "Dato regresado " + str(year)



print(holaMundo())
print("FUERA: ", website)