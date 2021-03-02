# Programación orientada a objetos
"""
Una clase es una plantilla para cear más objetos de ese tipo (auto) con características similares
"""
class Auto:
    # Atributos o propiedades
    # Características del auto
    color = "Rojo"
    marca = "Ferrari"
    modelo ="Station"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # Métodos, son acciones que realiza el objeto (auto)(funciones)

    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

# Fin definición clase

# Crear objetos / Instanciar la clase

auto = Auto()
print(auto.marca,auto.color)
print("Velocidad actual: ", auto.velocidad)

auto.acelerar()
auto.acelerar()
auto.acelerar()
auto.acelerar()

print("Velocidad nueva: ", auto.velocidad)

auto.frenar()
print("Velocidad nueva: ", auto.velocidad)
