
# Importar módulo
import sqlite3
# Conexión

conn = sqlite3.connect('pruebas.db')
cursor = conn.cursor()
# Crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT,"+
"titulo varchar(255), "+
"descripcion text, "+
"precio int(255)"+
")")

# Guardar cambios
conn.commit()
# Cerrar conexión
conn.close()