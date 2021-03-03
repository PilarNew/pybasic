import mysql.connector
# database= mysql.connector.connect(host='localhost',database='mysql',user='root',password='')
database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='master_python'
)

# La conexión ha sido correcta?
# print(database)

# Cursor - Nos permite ejecutar la consulta
cursor = database.cursor()

"""
# Crear base de datos
cursor.execute("CREATE DATABASE IF not EXISTS master_python")

# Para saber en el códgo si existe la base de datos
cursor.execute("SHOW DATABASES")
# Muestra todas las bases de datos existentes
for bd in cursor:
    print(bd)
"""

# # Crear tablas
# cursor.execute("""
# CREATE TABLE vehiculos(
#     id int(10) auto_increment not null,
#     marca varchar(40) not null,
#     modelo varchar(40) not null,
#     precio float(10,2) not null,
#     CONSTRAINT pk_vehiculo PRIMARY KEY(id)
# )
# """)

# # Para saber en el códgo si existe la tabla recién creada para no ir al administrador
# cursor.execute("SHOW TABLES")
# # Muestra todas las bases de datos existentes
# for table in cursor:
#     print(table)

# cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500)")
coches = [
    ('Seat', 'Ibiza',5000),
    ('Renault', 'Clio',15000),
    ('Citroen', 'Saxo',2000),
    ('Mercedes', 'Clase C',35000)
]

cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)",coches)

database.commit() # Guarda los cambios en la base de datos que tenemos dentro del cursor