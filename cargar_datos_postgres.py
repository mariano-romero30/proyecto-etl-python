import psycopg2
import pandas as pd

# Conexión a PostgreSQL
conexion = psycopg2.connect(
    host="mainline.proxy.rlwy.net",
    user="postgres",
    password="aMXOyaWISfYRCwepuGzYhixwRCzqqKZe",
    dbname="railway",
    port=52657
)

cursor = conexion.cursor()

# Leer CSV
df = pd.read_csv("productos_ecommerce.csv")

# Insertar datos (sin usar la columna id)
for _, fila in df.iterrows():
    cursor.execute("""
        INSERT INTO productos (nombre, precio, stock, categoria)
        VALUES (%s, %s, %s, %s)
    """, (
        fila["nombre"],
        float(fila["precio"]),
        int(fila["stock"]),
        fila["categoria"]
    ))

conexion.commit()
conexion.close()

print("📦 Datos cargados exitosamente en PostgreSQL.")
