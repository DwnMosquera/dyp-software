import os
import plotly.express as px

def crear_grafica(categorias, valores, ruta):
    """
    Crea una gráfica de barras interactiva ordenada de mayor a menor,
    con diseño limpio y formato de pesos.
    """
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    
    # Ordenar las barras de mayor a menor para gerencia
    datos_ordenados = sorted(zip(categorias, valores), key=lambda x: x[1], reverse=True)
    cat_ordenadas = [item[0] for item in datos_ordenados]
    val_ordenados = [item[1] for item in datos_ordenados]
    
    # Calcular porcentajes para mostrar al pasar el mouse
    total = sum(val_ordenados) if val_ordenados else 1
    porcentajes = [f"{(v / total) * 100:.1f}%" for v in val_ordenados]

    # Crear figura con Plotly Express
    fig = px.bar(
        x=cat_ordenadas,
        y=val_ordenados,
        color=cat_ordenadas,
        text=[f"${v:,.0f} ({p})" for v, p in zip(val_ordenados, porcentajes)],
        title="<b>Ventas Totales por Sabor - Heladería La Esquina</b><br><sup>Reporte Mensual</sup>",
        labels={"x": "Sabor", "y": "Valor Total ($)"},
        template="plotly_white"
    )

    fig.update_traces(textposition='outside')
    fig.update_layout(
        xaxis_title="Sabor",
        yaxis_title="Valor en Pesos (COP)",
        showlegend=False,
        margin=dict(t=80, b=40, l=40, r=40)
    )

    fig.write_html(ruta)
    print(f"Gráfica interactiva guardada en '{ruta}'.")