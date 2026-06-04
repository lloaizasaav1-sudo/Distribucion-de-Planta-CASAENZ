# --- SECCIÓN: PREGUNTA 1 ---
elif opcion == "1. Factores Críticos":
    st.header("1. Factores Críticos de Localización de Plantas")
    st.markdown("Definición cualitativa y cuantitativa de los criterios ponderados para los centros de operaciones.")
    
    st.success("""
    **Criterio de Selección:** Se determinaron 6 factores esenciales bajo la metodología analítica, asignando un peso porcentual de acuerdo con su impacto directo en los costos de operación y el nivel de servicio al cliente.
    """)
    
    # Tabla de factores basada en tu Word
    factores = {
        "Factor Crítico de Localización": [
            "Proximidad a Proveedores de Materia Prima",
            "Infraestructura Vial y Conectividad",
            "Cercanía al Mercado Objetivo / Clientes",
            "Costos Operativos (Arriendos, Servicios)",
            "Disponibilidad de Mano de Obra Calificada",
            "Seguridad y Entorno Comercial"
        ],
        "Peso Asignado (%)": [25, 20, 25, 20, 10, 15]
    }
    df_f = pd.DataFrame(factores)
    
    # Corrección de columnas y alineación estricta de bloques
    col1, col2 = st.columns([4, 5])
    with col1:
        st.write("### Matriz de Priorización")
        st.dataframe(df_f, hide_index=True, use_container_width=True)
        
    with col2:
        st.write("### Gráfico de Peso Relativo")
        fig = px.bar(
            df_f, 
            x="Peso Asignado (%)", 
            y="Factor Crítico de Localización", 
            orientation="h",
            color="Peso Asignado (%)",
            color_continuous_scale=["#A3B899", "#1E3F20"]
        )
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
