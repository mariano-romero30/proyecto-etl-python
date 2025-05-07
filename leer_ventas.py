import psycopg2
import os
from dotenv import load_dotenv

# Cargar las variables desde el archivo .env
load_dotenv()

# Obtener las variables de entorno
host = os.getenv("PGHOST")
database = os.getenv("PGDATABASE")
user = os.getenv("PGUSER")
password = os.getenv("PGPASSWORD")

# Conexión a la base de datos
conexion = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password
)

cursor = conexion.cursor()

# Consultamos todas las ventas
cursor.execute("SELECT * FROM ventas;")
ventas = cursor.fetchall()

# Mostramos los resultados en consola
for venta in ventas:
    print(venta)

# Cerramos conexión
cursor.close()
conexion.close()
