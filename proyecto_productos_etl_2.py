import pandas as pd

# Leer archivo CSV
df = pd.read_csv("productos_ecommerce.csv")

# Mostrar todos los productos
print("\n🟩 LISTA COMPLETA DE PRODUCTOS:")
print(df)

# Productos caros
print("\n🟨 PRODUCTOS CON PRECIO MAYOR A $5000:")
productos_caros = df[df["precio"] > 5000]
print(productos_caros[["nombre", "precio"]])

# Stock bajo
print("\n🟥 PRODUCTOS CON STOCK BAJO (menos de 5):")
stock_bajo = df[df["stock"] < 5]
print(stock_bajo[["nombre", "stock"]])

# ================================
# MÉTRICAS DEL NEGOCIO
# ================================

# Agregamos un salto de línea y mostramos el título con emoji
print("\n📊 MÉTRICAS GENERALES:")
# print("MÉTRICAS GENERALES:")  # ← SIN \n ni emoji

# Calculamos promedio de precios
precio_promedio = df["precio"].mean()

# Suma total del stock
stock_total = df["stock"].sum()

# Producto más caro (filtrando el valor máximo)
producto_mas_caro = df[df["precio"] == df["precio"].max()]

# Producto más barato (filtrando el valor mínimo)
producto_mas_barato = df[df["precio"] == df["precio"].min()]

# Mostramos el promedio con f-string y 2 decimales
print(f"🔹 Precio promedio: ${precio_promedio:.2f}")
# print("Precio promedio:", round(precio_promedio, 2))  # ← Sin f-string

# Mostramos el stock total con f-string
print(f"🔹 Stock total: {stock_total} unidades")
# print("Stock total:", stock_total, "unidades")  # ← Sin f-string

# Mostramos el producto más caro con título decorativo
print("\n💎 Producto más caro:")
# print("Producto más caro:")  # ← Sin salto de línea ni emoji
print(producto_mas_caro[["nombre", "precio"]])

# Mostramos el producto más barato
print("\n🧊 Producto más barato:")
# print("Producto más barato:")  # ← Sin salto de línea ni emoji
print(producto_mas_barato[["nombre", "precio"]])

# ================================
# PRODUCTO CON MÁS STOCK
# ================================

# Mostramos un título bonito con un salto de línea
print("\n📦 Producto con más stock disponible:")
# print("Producto con más stock disponible:")  # ← SIN salto ni emoji

# Buscamos el stock más alto
stock_maximo = df["stock"].max()

# Filtramos la fila donde el stock sea igual al máximo
producto_con_mas_stock = df[df["stock"] == stock_maximo]

# Mostramos el nombre y cantidad de stock
print(producto_con_mas_stock[["nombre", "stock"]])

# ================================
# EXPORTAR PRODUCTOS CON POCO STOCK
# ================================

# Creamos una nueva tabla solo con los que tienen stock menor a 5
productos_stock_bajo = df[df["stock"] < 5]

# Guardamos esa tabla en un nuevo archivo CSV
productos_stock_bajo.to_csv("stock_bajo.csv", index=False)

# Mostramos un mensaje para confirmar
print("\n✅ Archivo 'stock_bajo.csv' generado con los productos de bajo stock.")
# print("Archivo stock_bajo.csv listo.")  # ← versión sin emoji y sin \n

print(producto_con_mas_stock[["nombre", "stock"]])

# ================================
# EXPORTAR REPORTE COMPLETO A EXCEL
# ================================

# Filtros que ya conocés
productos_stock_bajo = df[df["stock"] < 5]
productos_caros = df[df["precio"] > 5000]

# Métricas simples
precio_promedio = df["precio"].mean()
stock_total = df["stock"].sum()
producto_mas_caro = df[df["precio"] == df["precio"].max()]["nombre"].values[0]
producto_mas_barato = df[df["precio"] == df["precio"].min()]["nombre"].values[0]
producto_mas_stock = df[df["stock"] == df["stock"].max()]["nombre"].values[0]

# Creamos un resumen como tabla (DataFrame)
resumen = pd.DataFrame({
    "Métrica": [
        "Cantidad total de productos",
        "Stock total disponible",
        "Precio promedio",
        "Producto más caro",
        "Producto más barato",
        "Producto con más stock",
        "Productos con stock bajo (<5)",
        "Productos con precio > 5000"
    ],
    "Valor": [
        len(df),
        stock_total,
        f"${precio_promedio:.2f}",
        producto_mas_caro,
        producto_mas_barato,
        producto_mas_stock,
        len(productos_stock_bajo),
        len(productos_caros)
    ]
})

# Exportar a Excel con múltiples hojas
with pd.ExcelWriter("reporte_productos.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="productos_completos", index=False)
    productos_stock_bajo.to_excel(writer, sheet_name="stock_bajo", index=False)
    productos_caros.to_excel(writer, sheet_name="productos_caros", index=False)
    resumen.to_excel(writer, sheet_name="resumen", index=False)

# Mensaje de éxito
print("\n📁 Archivo 'reporte_productos.xlsx' generado con 4 hojas.")

# ================================
# MENÚ INTERACTIVO
# ================================

while True:
    print("\n📋 MENÚ DE OPCIONES")
    print("1 - Ver resumen de métricas")
    print("2 - Ver productos con stock bajo")
    print("3 - Ver productos caros")
    print("4 - Generar reporte Excel")
    print("0 - Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        print("\n📊 MÉTRICAS GENERALES:")
        print(resumen)

    elif opcion == "2":
        print("\n🟥 PRODUCTOS CON STOCK BAJO (<5):")
        print(productos_stock_bajo)

    elif opcion == "3":
        print("\n🟨 PRODUCTOS CON PRECIO MAYOR A $5000:")
        print(productos_caros)

    elif opcion == "4":
        with pd.ExcelWriter("reporte_productos.xlsx", engine="openpyxl") as writer:
            df.to_excel(writer, sheet_name="productos_completos", index=False)
            productos_stock_bajo.to_excel(writer, sheet_name="stock_bajo", index=False)
            productos_caros.to_excel(writer, sheet_name="productos_caros", index=False)
            resumen.to_excel(writer, sheet_name="resumen", index=False)
        print("\n✅ Archivo 'reporte_productos.xlsx' generado correctamente.")

    elif opcion == "0":
        print("👋 ¡Hasta luego, Mariano!")
        break

    else:
        print("❌ Opción inválida. Probá de nuevo.")



