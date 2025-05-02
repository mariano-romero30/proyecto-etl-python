import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Conectar a la base de datos
conn = sqlite3.connect("productos_ventas.db")
df = pd.read_sql_query("SELECT * FROM productos", conn)
conn.close()

# 📊 Gráfico de barras (stock por producto)
plt.figure(figsize=(10, 6))
plt.barh(df["nombre"], df["stock"], color="skyblue")
plt.xlabel("Cantidad en stock")
plt.ylabel("Producto")
plt.title("📦 Stock por producto")
plt.tight_layout()
plt.show()

# 🍕 Gráfico de torta (distribución por categoría)
categoria_counts = df["categoria"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(categoria_counts, labels=categoria_counts.index, autopct="%1.1f%%", startangle=140)
plt.title("📂 Distribución por categoría")
plt.axis("equal")  # Mantener forma circular
plt.show()

# 📈 Gráfico de líneas (evolución de precios simulada)
# Simulamos una variación de precios en 3 meses por cada producto
df_simulado = pd.DataFrame({
    "Producto": df["nombre"],
    "Mes 1": df["precio"],
    "Mes 2": df["precio"] * 1.05,  # aumento del 5%
    "Mes 3": df["precio"] * 0.95   # baja del 5%
})
df_simulado.set_index("Producto", inplace=True)
df_simulado = df_simulado.transpose()

plt.figure(figsize=(12, 6))
for producto in df_simulado.columns:
    plt.plot(df_simulado.index, df_simulado[producto], marker="o", label=producto)

plt.title("📈 Evolución de precios simulada")
plt.xlabel("Mes")
plt.ylabel("Precio ($)")
plt.xticks(df_simulado.index)
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()
