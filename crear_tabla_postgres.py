import psycopg2

# Conectar a la base de datos PostgreSQL en Railway
conexion = psycopg2.connect(
    dbname="railway",
    user="postgres",
    password="aMXOyaWISfYRCwepuGzYhixwRCzqqKZe",
    host="mainline.proxy.rlwy.net",
    port=52657
)

cursor = conexion.cursor()

# Crear tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    precio NUMERIC,
    stock INTEGER,
    categoria VARCHAR(50)
)
""")

conexion.commit()
print("✅ Tabla 'productos' creada correctamente (si no existía).")

cursor.close()
conexion.close()
