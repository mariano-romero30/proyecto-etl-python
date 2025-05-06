import psycopg2

# Conexión a la base de datos
conexion = psycopg2.connect(
    host="localhost",
    database="mi_base_datos",
    user="postgres",
    password="admin123"  # Cambialo si usaste otra clave
)

cursor = conexion.cursor()

# Crear tabla ventas si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS ventas (
        id SERIAL PRIMARY KEY,
        producto TEXT NOT NULL,
        cantidad INTEGER NOT NULL,
        precio NUMERIC NOT NULL
    );
""")

# Insertar datos de prueba
cursor.execute("""
    INSERT INTO ventas (producto, cantidad, precio)
    VALUES
        ('Camisa', 2, 2500.00),
        ('Pantalón', 1, 4500.00),
        ('Zapatos', 1, 6500.00)
    ON CONFLICT DO NOTHING;  -- evita duplicados si ya existen
""")

conexion.commit()  # Guardar cambios
cursor.close()
conexion.close()

print("Tabla y datos de prueba creados con éxito.")
