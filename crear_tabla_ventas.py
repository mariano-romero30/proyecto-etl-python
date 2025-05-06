import psycopg2

# Conexión a tu base de datos
conexion = psycopg2.connect(
    host="mainline.proxy.rlwy.net",
    port=52657,
    dbname="railway",
    user="postgres",
    password="aMXOyaWISfYRCwepuGzYhixwRCzqqKZe"
)

cursor = conexion.cursor()

# Crear la tabla 'ventas'
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
