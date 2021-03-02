import clases

persona = clases.Persona()

persona.setNombre("Pilar")
persona.setApellidos("González")
persona.setEdad("30 años")
persona.setAltura("151 cm")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}, tiene {persona.getEdad()} y mide {persona.getAltura()}")
print(persona.hablar())
print("-------------------------------")
informatico = clases.Informatico()

informatico.setNombre("Nayi")
informatico.setApellidos("González")
informatico.setEdad("30 años")
informatico.setAltura("151 cm")

print(f"\nLa persona es: {informatico.getNombre()} {persona.getApellidos()}, tiene {informatico.getEdad()} y mide {informatico.getAltura()}")
print(informatico.programar())
print(informatico.getLenguajes())
print(informatico.caminar())

print("-------------------------------")
tecnico = clases.TecnicoRedes()
tecnico.setNombre("Claudio")
print(tecnico.auditarRedes,tecnico.getNombre())
print(informatico.getLenguajes())