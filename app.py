import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="CASAENZ - Dashboard Ejecutivo",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. ESTILOS CSS E IDENTIDAD CORPORATIVA INTEGRADA
st.markdown("""
<style>
    /* Fondo beige claro institucional */
    .stApp {
        background-color: #F5F1E8;
    }
    
    /* Efecto de Marca de Agua con el logotipo */
    .stApp::before {
        content: "";
        position: fixed;
        top: 50%;
        left: 50%;
        width: 500px;
        height: 500px;
        transform: translate(-50%, -50%);
        background-image: url("https://raw.githubusercontent.com/tu-usuario/tu-repositorio/main/assets/logo.png");
        background-repeat: no-repeat;
        background-position: center;
        background-size: contain;
        opacity: 0.04;
        z-index: -1;
    }
    
    /* Estilos de títulos y métricas */
    h1, h2, h3 {
        color: #1E3F20 !important; /* Verde profundo de CASAENZ */
        font-family: 'Arial', sans-serif;
    }
    
    .stMetric {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 2px 4px 10px rgba(0,0,0,0.04);
        border-left: 5px solid #8C1D40; /* Rojo cereza de café */
    }
</style>
""", unsafe_allow_html=True)

# 3. MENÚ DE NAVEGACIÓN LATERAL
st.sidebar.markdown("# ☕ CASAENZ")
st.sidebar.markdown("### Distribución de Planta")
st.sidebar.markdown("---")

opcion = st.sidebar.radio(
    "Seleccione la Sección a Exponer:",
    [
        "Inicio / Presentación",
        "1. Factores Críticos",
        "2. Técnicas de Localización",
        "3. Red de Suministro",
        "4. Simulación FlexSim",
        "5. Distribución y Balanceo",
        "Conclusiones"
    ]
)

# --- PÁGINA: INICIO ---
if opcion == "Inicio / Presentación":
    st.title("☕ Proyecto Integrador: Diseño y Distribución de Planta")
    st.subheader("Caso de Estudio: Café Artesanal CASAENZ")
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            st.image("assets/logo.png", use_container_width=True)
        except:
            st.info("💡 Coloca tu logo en `assets/logo.png` para visualizarlo aquí.")
            
    with col2:
        st.markdown("""
        ### **Ficha Técnica de la Sustentación**
        * **Institución:** Corporación Universitaria Minuto de Dios - UNIMINUTO
        * **Programa:** Ingeniería Industrial
        * **Autora:** Laura Juliana Loaiza Saavedra (ID: 428429)
        
        ### **Propósito Ejecutivo**
        Esta aplicación interactiva funciona como un **Dashboard de Decisiones Estratégicas** para sustentar la viabilidad técnica, operativa y logística del procesamiento y empaque de café premium en el departamento del Valle del Cauca.
        """)

# --- PÁGINA: PREGUNTA 1 ---
elif opcion == "1. Factores Críticos":
    st.header("1. Factores Críticos de Localización de Plantas")
    st.markdown("Definición cualitativa y cuantitativa de los criterios ponderados para los centros de operaciones.")
    
    st.success("""
    **Criterio de Selección:** Se determinaron 6 factores esenciales bajo la metodología analítica, asignando un peso porcentual de acuerdo con su impacto directo en los costos de operación y el nivel de servicio al cliente.
    """)
    
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

# --- PÁGINA: PREGUNTA 2 ---
elif opcion == "2. Técnicas de Localización":
    st.header("2. Técnicas Cuantitativas de Localización")
    st.markdown("Resultados de la aplicación de los métodos de Factores Ponderados, Centro de Gravedad y Análisis CVU.")
    
    col1,
