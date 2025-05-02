import sqlite3
import pandas as pd
from datetime import datetime

# ──────────────────────────────────────────────
# 🔹 ETAPA 1: Conexión a base de datos y lectura
# ──────────────────────────────────────────────

def conectar_bd(nombre_bd):
    return sqlite3.connect(nombre_bd)

def obtener_productos(conn):
    consulta = "SELECT * FROM productos"
    return pd.read_sql_query(consulta, conn)

# ──────────────────────────────────────────────
# 🔹 ETAPA 2: Análisis de datos con pandas
# ──────────────────────────────────────────────

def generar_métricas(df):
    resumen = {
        "Cantidad total de productos": len(df),
        "Stock total": df["stock"].sum(),
        "Precio promedio": round(df["precio"].mean(), 2),
        "Producto más caro": df.loc[df["precio"].idxmax(), "nombre"],
        "Producto más barato": df.loc[df["precio"].idxmin(), "nombre"],
        "Stock bajo (<5)": df[df["stock"] < 5].shape[0],
        "Productos > $5000": df[df["precio"] > 5000].shape[0]
    }
    return resumen

# ──────────────────────────────────────────────
# 🔹 ETAPA 3: Guardar a Excel
# ──────────────────────────────────────────────

def exportar_excel(df, resumen):
    fecha_actual = datetime.now().strftime("%Y-%m-%d_%H-%M")
    nombre_archivo = f"reporte_avanzado_{fecha_actual}.xlsx"
    with pd.ExcelWriter(nombre_archivo) as writer:
        df.to_excel(writer, sheet_name="Productos", index=False)
        resumen_df = pd.DataFrame(list(resumen.items()), columns=["Métrica", "Valor"])
        resumen_df.to_excel(writer, sheet_name="Resumen", index=False)
    return nombre_archivo

# ──────────────────────────────────────────────
# 🔹 ETAPA 4: Menú interactivo
# ──────────────────────────────────────────────

def main():
    while True:
        print("\n📋 MENÚ DE OPCIONES")
        print("1 - Ver métricas en pantalla")
        print("2 - Generar y guardar reporte Excel")
        print("3 - Buscar productos por categoría")
        print("4 - Buscar productos por rango de precios")
        print("5 - Buscar productos con stock bajo")
        print("0 - Salir")
        opcion = input("Elegí una opción: ")

        conn = conectar_bd("productos_ventas.db")
        df_productos = obtener_productos(conn)
        conn.close()

        if opcion == "1":
            resumen = generar_métricas(df_productos)
            print("\n📊 MÉTRICAS:")
            for k, v in resumen.items():
                print(f"🔸 {k}: {v}")

        elif opcion == "2":
            resumen = generar_métricas(df_productos)
            archivo = exportar_excel(df_productos, resumen)
            print(f"✅ Reporte guardado como {archivo}")

        elif opcion == "3":
            categorias = df_productos["categoria"].unique()
            print("\n📂 Categorías disponibles:")
            for cat in categorias:
                print(f"🔹 {cat}")
            cat_input = input("Escribí una categoría: ")
            resultado = df_productos[df_productos["categoria"] == cat_input]
            print("\n📋 Productos en esa categoría:")
            print(resultado if not resultado.empty else "❌ No se encontraron productos.")

        elif opcion == "4":
            try:
                min_p = float(input("Precio mínimo: "))
                max_p = float(input("Precio máximo: "))
                resultado = df_productos[(df_productos["precio"] >= min_p) & (df_productos["precio"] <= max_p)]
                print("\n💰 Productos en ese rango de precios:")
                print(resultado if not resultado.empty else "❌ No se encontraron productos.")
            except:
                print("❌ Entrada inválida. Asegurate de escribir números.")

        elif opcion == "5":
            try:
                limite = int(input("Mostrar productos con stock menor a: "))
                resultado = df_productos[df_productos["stock"] < limite]
                print("\n📦 Productos con stock bajo:")
                print(resultado if not resultado.empty else "❌ No se encontraron productos.")
            except:
                print("❌ Entrada inválida. Asegurate de escribir un número entero.")

        elif opcion == "0":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción inválida. Intentá de nuevo.")

# ──────────────────────────────────────────────

if __name__ == "__main__":
    main()

