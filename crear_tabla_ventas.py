import psycopg2
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Conexión segura a la base de datos usando variables del entorno
conexion = psycopg2.connect(
    host=os.getenv("PGHOST"),
    port=os.getenv("PGPORT"),
    dbname=os.getenv("PGDATABASE"),
    user=os.getenv("PGUSER"),
    password=os.getenv("PGPASSWORD")
)

cursor = conexion.cursor()

# Crear la tabla 'ventas' si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS ventas (
        id SERIAL PRIMARY KEY,
        producto_id INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        precio_unitario NUMERIC(10, 2) NOT NULL,
        fecha_venta TIMESTAMP NOT NULL
    );
""")

conexion.commit()
cursor.close()
conexion.close()

print("✅ Tabla 'ventas' creada correctamente.")
