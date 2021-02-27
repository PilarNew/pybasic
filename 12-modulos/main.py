"""
Módulos: Son funcionalidades ya hechas para reutilizar
Consulta en https://docs.python.org/3/py-modindex.html

Podemos conseguir módulos que ya vienen en el lenguaje,
módulos en Internet y también puedes crear tus propios módulos

Programa principal más limpio y mayor abstravvión

"""

# Importar módulo propio (Se traen todas las funciones )
# import mimodulo
# Utiizando 
# print(mimodulo.holaMundo("Pili"))
# print(mimodulo.calculadora(5,5))

# Importar una función no requiere nombrar al módulo
# from mimodulo import holaMundo
# print(holaMundo("Pili"))

# Para no nombrar el módulo se puede utilizar la siguiente instrucción:

from mimodulo import *

# Utiizando 
print(holaMundo("Pili"))
print(calculadora(5,5))
