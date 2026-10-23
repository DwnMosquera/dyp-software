import csv
import os
import random
from datetime import datetime, timedelta

# Asegurar que la carpeta 'datos' exista
os.makedirs("datos", exist_ok=True)
ruta_csv = "datos/registros.csv"

# Datos simulados del negocio (Ej: Heladería La Esquina)
sabores = ["Chocolate", "Vainilla", "Fresa", "Arequipe", "Maracuyá"]
tamanos = ["Pequeño", "Mediano", "Grande"]
medios_pago = ["Efectivo", "Tarjeta", "Nequi"]
estados = ["Completado", "Completado", "Completado", "Cancelado"]

filas = []
fecha_base = datetime(2026, 10, 1)

# 1. Generar 100 registros válidos
for i in range(1, 101):
    id_venta = i
    fecha = (fecha_base + timedelta(days=random.randint(0, 20), hours=random.randint(10, 21))).strftime("%Y-%m-%d")
    sabor = random.choice(sabores)
    tamano = random.choice(tamanos)
    cantidad = random.randint(1, 3)
    valor = cantidad * random.choice([4000, 5000, 7000, 10000])
    medio = random.choice(medios_pago)
    estado = random.choice(estados)
    filas.append([id_venta, fecha, sabor, tamano, cantidad, valor, medio, estado])

# 2. Agregar las 5 filas dañadas a propósito para probar el try/except del Ticket 2
filas.append([101, "2026-10-10", "Chocolate", "Grande", 1, "", "Nequi", "Completado"]) # Valor vacío
filas.append([102, "2026-10-11", "Vainilla", "Pequeño", 2, "cinco_mil", "Efectivo", "Completado"]) # Texto en valor
filas.append([103, "30-10-2026", "Fresa", "Mediano", 1, 5000, "Tarjeta", "Completado"]) # Fecha mal escrita
filas.append([104, "2026-10-12", "Arequipe", "Grande", 1, "", "Efectivo", "Completado"]) # Valor vacío
filas.append([105, "2026-10-13", "Maracuyá", "Pequeño", 1, "diez_mil", "Nequi", "Completado"]) # Texto en valor

# Escribir el archivo CSV
with open(ruta_csv, mode="w", newline="", encoding="utf-8") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["id", "fecha", "sabor", "tamano", "cantidad", "valor", "medio_de_pago", "estado"])
    writer.writerows(filas)

print(f"Archivo generado exitosamente en '{ruta_csv}' con 105 registros totales.")