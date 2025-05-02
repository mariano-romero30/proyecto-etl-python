import sqlite3

def mostrar_menu():
    print("\n📋 MENÚ DE CONSULTAS SQL")
    print("1 - Ver todos los productos")
    print("2 - Ver productos con precio mayor a $10.000")
    print("3 - Ordenar productos por precio (mayor a menor)")
    print("4 - Ver los primeros 3 productos")
    print("5 - Ver productos por categoría (Tecnología)")
    print("6 - Ver productos con stock bajo (< 5)")
    print("7 - Ver los 3 productos más baratos")
    print("8 - Buscar productos por categoría (ingresada por el usuario)")
    print("0 - Salir")

def ejecutar_consulta(sql):
    conn = sqlite3.connect("productos_ventas.db")
    cursor = conn.cursor()
    cursor.execute(sql)
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    conn.close()

# Bucle principal del menú
while True:
    mostrar_menu()
    opcion = input("Elegí una opción: ")

    if opcion == "1":
        ejecutar_consulta("SELECT * FROM productos")
    elif opcion == "2":
        ejecutar_consulta("SELECT * FROM productos WHERE precio > 10000")
    elif opcion == "3":
        ejecutar_consulta("SELECT * FROM productos ORDER BY precio DESC")
    elif opcion == "4":
        ejecutar_consulta("SELECT * FROM productos LIMIT 3")
    elif opcion == "5":
        ejecutar_consulta("SELECT * FROM productos WHERE categoria = 'Tecnología'")
    elif opcion == "6":
        ejecutar_consulta("SELECT * FROM productos WHERE stock < 5")
    elif opcion == "7":
        ejecutar_consulta("SELECT nombre, precio FROM productos ORDER BY precio ASC LIMIT 3")
    elif opcion == "8":
        # Mostrar categorías disponibles
        print("\n📂 Categorías disponibles:")
        conn = sqlite3.connect("productos_ventas.db")
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT categoria FROM productos")
        categorias = cursor.fetchall()
        conn.close()

        if categorias:
            for cat in categorias:
                print(f"🔹 {cat[0]}")
        else:
            print("❌ No hay categorías disponibles.")

        # Pedir categoría al usuario
        categoria = input("Escribí una categoría exactamente como aparece arriba: ")
        consulta = f"SELECT * FROM productos WHERE categoria = '{categoria}'"
        ejecutar_consulta(consulta)

    elif opcion == "0":
        print("👋 Saliendo del sistema de consultas...")
        break
    else:
        print("❌ Opción inválida. Intentá de nuevo.")


