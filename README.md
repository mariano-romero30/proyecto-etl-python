# 🛠️ Proyecto ETL de Productos con Python y Pandas

Este proyecto simula un sistema ETL básico orientado a un escenario de e-commerce.  
Forma parte de mi portafolio profesional como Data Engineer Junior.

---

## 📌 Objetivo del proyecto

Desarrollar un flujo completo de extracción, transformación y carga de datos utilizando Python, Pandas y Excel, siguiendo buenas prácticas y mostrando métricas útiles para la toma de decisiones.

---

## 🧰 Tecnologías y herramientas utilizadas

- Python 3.13
- Pandas
- Openpyxl
- Visual Studio Code
- Git + GitHub

---

## 📦 Funcionalidades principales

✅ Lectura de archivo CSV (`productos_ecommerce.csv`)  
✅ Filtros: productos caros, stock bajo  
✅ Cálculos automáticos de métricas (promedio, máximos, mínimos, stock total)  
✅ Exportación a Excel profesional con 4 hojas  
✅ Menú interactivo por consola para uso simple  
✅ Código limpio, modular y documentado

---

## 📊 Estructura del Excel generado

El archivo `reporte_productos.xlsx` incluye:

- **productos_completos**: tabla original  
- **stock_bajo**: productos con stock menor a 5  
- **productos_caros**: productos con precio mayor a 5000  
- **resumen**: métricas clave del negocio

---

## 🧠 ¿Por qué es relevante para un rol de Data Engineer?

Este proyecto refleja capacidades esenciales para el rol:

- Automatización de procesos ETL  
- Análisis exploratorio de datos  
- Generación de reportes  
- Uso de estructuras de control y lógica condicional  
- Buenas prácticas de versionado con Git

---

## 📈 Ejecución del proyecto

1. Clonar el repositorio  
2. Instalar dependencias:

```bash
pip install pandas openpyxl
