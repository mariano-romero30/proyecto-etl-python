import psycopg2
import csv

# Conexión a PostgreSQL
conexion = psycopg2.connect(
    host="localhost",
    database="mi_base_datos",
    user="postgres",
    password="admin123"
)

cursor = conexion.cursor()

# Ejecutar la consulta
cursor.execute("SELECT * FROM ventas")
ventas = cursor.fetchall()

# Obtener los nombres de las columnas
columnas = [desc[0] for desc in cursor.description]

# Exportar a archivo CSV
with open("ventas_exportadas.csv", mode="w", newline="", encoding="utf-8") as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerow(columnas)      # Escribir encabezado
    escritor.writerows(ventas)       # Escribir datos

print("✅ Archivo 'ventas_exportadas.csv' creado con éxito.")

# Cerrar conexión
cursor.close()
conexion.close()
