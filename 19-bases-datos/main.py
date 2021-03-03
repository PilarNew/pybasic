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

cursor = database.cursor()
cursor.execute("CREATE DATABASE IF not EXISTS master_python")

# Para saber en el códgo si existe la base de datos
cursor.execute("SHOW DATABASES")
# Muestra todas las bases de datos existentes
for bd in cursor:
    print(bd)