"""
DICCIONARIO
Un tipo de datos que almacena un conjunto de datos. En formato clave > valor
Es parecido a un array asociativo o un objeto JSON
Índice alfanumérico
"""

persona ={
"nombre": "Pili",
"apellido": "González",
"edad": "?"
}

print(persona)
print(type(persona))
print(persona["apellido"])


# Lista con diccinarios (Objeto JSON)

contactos = [
    {
        "nombre":"Antonio",
        "email":"antonio@gmail.com"
    },
    {    
        "nombre":"Juan",
        "email":"juan@gmail.com"
    },
    {
        "nombre":"Mario",
        "email":"mario@gmail.com"
    },
    {   "nombre":"Claudio",
        "email":"claudio@gmail.com"
    }
]
contactos[0]["nombre"]="Toñito"
print(contactos[0]["nombre"])

print("\nLista de Contactos")

print("--------------------------------------")
for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("--------------------------------------")