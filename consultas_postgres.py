import psycopg2

# Función para conectarse a PostgreSQL
def conectar_postgres():
    return psycopg2.connect(
        host="mainline.proxy.rlwy.net",
        user="postgres",
        password="aMXOyaWISfYRCwepuGzYhixwRCzqqKZe",
        dbname="railway",
        port=52657
    )

# Función para ejecutar una consulta y mostrar resultados
def ejecutar_consulta(sql):
    conexion = conectar_postgres()
    cursor = conexion.cursor()
    cursor.execute(sql)
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    conexion.close()

# Menú interactivo
def mostrar_menu():
    print("\n📊 CONSULTAS DISPONIBLES")
    print("1 - Ver todos los productos")
    print("2 - Ver productos con precio > $10.000")
    print("3 - Ver productos por categoría")
    print("4 - Ver promedio de precios por categoría")
    print("5 - Ver productos ordenados por precio (desc)")
    print("0 - Salir")

# Bucle del menú
while True:
    mostrar_menu()
    opcion = input("Elegí una opción: ")

    if opcion == "1":
        ejecutar_consulta("SELECT * FROM productos")
    elif opcion == "2":
        ejecutar_consulta("SELECT * FROM productos WHERE precio > 10000")
    elif opcion == "3":
        categoria = input("Ingresá una categoría (ej: Tecnología, Audio, etc.): ")
        ejecutar_consulta(f"SELECT * FROM productos WHERE categoria = '{categoria}'")
    elif opcion == "4":
        ejecutar_consulta("SELECT categoria, ROUND(AVG(precio), 2) FROM productos GROUP BY categoria")
    elif opcion == "5":
        ejecutar_consulta("SELECT * FROM productos ORDER BY precio DESC")
    elif opcion == "0":
        print("👋 Saliendo del sistema de consultas...")
        break
    else:
        print("❌ Opción inválida. Intentá de nuevo.")
