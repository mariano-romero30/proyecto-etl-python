import psycopg2
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

conexion = psycopg2.connect(
    host=os.getenv("PGHOST"),
    database=os.getenv("PGDATABASE"),
    user=os.getenv("PGUSER"),
    password=os.getenv("PGPASSWORD")
)

df = pd.read_csv("ventas.csv")

cursor = conexion.cursor()
for _, fila in df.iterrows():
    cursor.execute("""
        INSERT INTO ventas (producto, cantidad, precio, fecha)
        VALUES (%s, %s, %s, %s)
    """, (fila["producto"], fila["cantidad"], fila["precio"], fila["fecha"]))

conexion.commit()
cursor.close()
conexion.close()

print("📦 Datos cargados exitosamente en PostgreSQL.")
