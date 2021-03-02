# HERENCIA:  Es la posibilidad de compartr atributos y métodos entre clases y
# que diferentes clases hereden de otras
# Molde para crear personas
class Persona:
    """
    nombre
    apellidos
    altura
    edad
    """
    def setNombre(self,nombre):
       self.nombre = nombre

    def setApellidos(self,apellidos):
        self.apellidos = apellidos
    
    def setAltura(self,altura):
        self.altura = altura
    
    def setEdad(self,edad):
        self.edad = edad
        
    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos
    
    def getAltura(self):
        return self.altura
    
    def getEdad(self):
        return self.edad
    
    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "Estoy caminando"

    def dormir(self):
        return "Estoy durmiendo"
# Fin de la definición de la clase principal

class Informatico(Persona):
    # lenguajes
    # experiencia

    def __init__(self):
        self.lenguajes = "HTML, CSS, Javascript, PHP"
        self.experiencia = 5
    
    def getLenguajes(self):
        return self.lenguajes

    def aprender(self,lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def programar(self):
        return "Estoy programando"
    
    def repararPC(self):
        return "He reparado el PC"

class TecnicoRedes(Informatico):

    def __init__(self):
        super().__init__() # Aquí se cargan también se cargan los datos del constructor en la clase padre
        self.auditarRedes="experto"
        self.experienciaRedes = 15
    
    def auditoria(self):
        return "Estoy realizando una auditoria"