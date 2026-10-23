import csv
import os
from datetime import datetime
from grafica import crear_grafica

def generar_reporte():
    ruta_csv = "datos/registros.csv"
    ruta_reporte = "salida/reporte.md"
    ruta_grafica = "salida/grafica.html"
    
    os.makedirs("salida", exist_ok=True)

    if not os.path.exists(ruta_csv):
        print(f"Error: No se encontró {ruta_csv}. Ejecute primero 'generar_datos.py'.")
        return

    filas_leidas = 0
    registros_validos = 0
    filas_descartadas = 0
    valor_total = 0
    ventas_por_categoria = {}

    # Lectura del CSV con manejo de errores try/except exigido por la guía
    with open(ruta_csv, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            filas_leidas += 1
            try:
                # Validar que el valor sea numérico y no esté vacío
                valor_str = fila["valor"].strip()
                if not valor_str:
                    raise ValueError("Valor vacío")
                valor = float(valor_str)
                
                # Validar formato de fecha (YYYY-MM-DD)
                fecha_str = fila["fecha"].strip()
                datetime.strptime(fecha_str, "%Y-%m-%d")

                # Si es válido, se acumula
                registros_validos += 1
                valor_total += valor

                sabor = fila["sabor"].strip()
                if sabor not in ventas_por_categoria:
                    ventas_por_categoria[sabor] = {"registros": 0, "valor": 0}
                
                ventas_por_categoria[sabor]["registros"] += 1
                ventas_por_categoria[sabor]["valor"] += valor

            except (ValueError, KeyError, TypeError):
                # Si hay error de formato o dato sucio, se descarta y cuenta sin detener el programa
                filas_descartadas += 1

    # Extraer categorías y valores para la gráfica
    categorias = list(ventas_por_categoria.keys())
    valores = [info["valor"] for info in ventas_por_categoria.values()]
    
    # Llamar a la función de la gráfica (Ticket 3)
    crear_grafica(categorias, valores, ruta_grafica)

    # Escribir el reporte en Markdown (salida/reporte.md)
    fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    
    contenido_md = f"""# Reporte del mes: Heladería La Esquina
Generado el: {fecha_hoy}

## Resumen
| Dato | Valor |
|---|---|
| Filas leídas | {filas_leidas} |
| Registros válidos | {registros_validos} |
| Filas descartadas | {filas_descartadas} |
| Valor total | ${valor_total:,.0f} |

## Por categoría
| Categoría | Registros | Valor |
|---|---|---|
"""
    for cat, info in ventas_por_categoria.items():
        contenido_md += f"| {cat} | {info['registros']} | ${info['valor']:,.0f} |\n"

    contenido_md += f"""
## Gráfica
Ver `salida/grafica.html` ([Abrir Gráfica](grafica.html))
"""

    with open(ruta_reporte, mode="w", encoding="utf-8") as f:
        f.write(contenido_md)

    print(f"Reporte generado exitosamente en '{ruta_reporte}'")

if __name__ == "__main__":
    generar_reporte()