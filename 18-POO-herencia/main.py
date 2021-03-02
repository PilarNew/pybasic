import clases

persona = clases.Persona()

persona.setNombre("Pilar")
persona.setApellidos("González")
persona.setEdad("30 años")
persona.setAltura("151 cm")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}, tiene {persona.getEdad()} y mide {persona.getAltura()}")
