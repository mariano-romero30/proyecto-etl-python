import psycopg2

# Conectarse a la base de datos
conn = psycopg2.connect(
    dbname="mi_proyecto",
    user="postgres",         # Cambiá si tu usuario es otro
    password="tu_contraseña",  # Reemplazá con tu contraseña real
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# Crear tabla ventas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS ventas (
        id SERIAL PRIMARY KEY,
        producto_id INTEGER REFERENCES productos(id),
        cantidad INTEGER NOT NULL,
        precio_unitario NUMERIC(10, 2) NOT NULL,
        fecha_venta DATE NOT NULL
    );
""")

conn.commit()
cursor.close()
conn.close()

print("Tabla 'ventas' creada exitosamente.")
