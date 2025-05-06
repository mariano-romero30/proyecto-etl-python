import psycopg2

conexion = psycopg2.connect(
    host="mainline.proxy.rlwy.net",
    port=52657,
    dbname="railway",
    user="postgres",
    password="aMXOyaWISfYRCwepuGzYhixwRCzqqKZe"
)

cursor = conexion.cursor()

cursor.execute("""
    SELECT v.id, p.nombre, v.cantidad, v.precio_unitario, v.fecha_venta
    FROM ventas v
    JOIN productos p ON v.producto_id = p.id
""")

ventas = cursor.fetchall()

for venta in ventas:
    print(f"ID: {venta[0]}, Producto: {venta[1]}, Cantidad: {venta[2]}, Precio Unitario: {venta[3]}, Fecha: {venta[4]}")

cursor.close()
conexion.close()

