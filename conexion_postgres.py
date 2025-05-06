import psycopg2

# Cadena de conexión proporcionada por Railway
conexion = psycopg2.connect(
    dbname="railway",
    user="postgres",
    password="aMXOyaWISfYRCwepuGzYhixwRCzqqKZe",
    host="mainline.proxy.rlwy.net",
    port=52657
)

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

# ✅ Ejemplo de consulta simple
cursor.execute("SELECT NOW();")  # Obtener la fecha y hora actual del servidor
resultado = cursor.fetchone()
print("📅 Fecha y hora actual del servidor:", resultado[0])

# Cerrar conexión
cursor.close()
conexion.close()
