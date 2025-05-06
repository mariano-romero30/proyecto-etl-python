import psycopg2

# Conexión a la base de datos con tus datos
conexion = psycopg2.connect(
    host="localhost",
    database="mi_base_datos",
    user="postgres",
    password="admin123"  # ⚠️ Reemplazá esto si tu contraseña es otra
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
