
# Importar módulo
import sqlite3
# Conexión

conn = sqlite3.connect('pruebas.db')
cursor = conn.cursor()
# Crear tabla
"""
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT,"+
"titulo varchar(255), "+
"descripcion text, "+
"precio int(255)"+
")")
"""
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo varchar(255),
    descripcion text,
    precio int(255)
);
""")




# Guardar cambios
conn.commit()
"""
# Insertar datos
cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'Descripción de primer producto', 1000)")
conn.commit()
"""

# Borrar registros
cursor.execute("DELETE FROM productos")
conn.commit()
# Insertar varios registros a la vez
productos = [
    ("Notebook","Buen PC", 100),
    ("Smart phone","Buen el teléfono", 10),
    ("Placa madre","Buena placa madre", 90),
    ("TV HD","Buen televisor", 200)
]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)",productos)
conn.commit()

#UPDATE
cursor.execute("UPDATE productos SET precio = 180 WHERE precio < 100")
# Listar datos
cursor.execute("SELECT * FROM productos WHERE precio >= 100;")
productos = cursor.fetchall()
for producto in productos:
    print("ID:",producto[0])
    print("Nombre:", producto[1])
    print("Descripción:", producto[2])
    print("Precio: $",producto[3])
    print("\n")
cursor.execute("SELECT titulo FROM productos;")
producto = cursor.fetchone() # Saca el primer producto
conn.commit()

# Cerrar conexión
conn.close()