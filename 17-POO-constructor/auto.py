"""
Constructor: Método especial dentro de una clase y se acostumbra usar para darle un valor a los atributos del objeto al crearlo. Es el primer método que se ejecuta al crear el objeto y se llama automáticamente al crearlo.
Como cualquier otro método puede recibir parámetros. Se le pasan los parámetros cuando se invoca a la clase.

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

    soy_publico = "Hola soy un atributo público"
    __soy_privado = "Hola soy un atributo privado"
    def __init__(self,color, marca, modelo,velocidad,caballaje,plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas
# Métodos, son acciones que realiza el objeto (auto)(funciones)
    def getPrivado(self):
        return self.__soy_privado
        
    def setColor(self,color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def setModelo(self,modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo

    def setMarca(self,marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca

    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

    def getInfo(self):
        info = "------ Información del auto"
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getVelocidad())
        return info

# Fin definición clase

