import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Configuración inicial de la página
st.set_page_config(
    page_title="Proyecto Integrador - Café CASAENZ",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
# CONFIGURACIÓN DE ESTILOS LIMPIOS (SIN NINGÚN FONDO PERSONALIZADO)
# ==============================================================================
URL_LOGO = "https://raw.githubusercontent.com/lloaizasaav1-sudo/Distribucion-de-Planta-CASAENZ/main/logo.png" 

st.markdown("""
    <style>
    /* Títulos y textos estilizados con colores oscuros de alta legibilidad */
    .main-title { font-size:42px !important; font-weight: bold; color: #4A3018; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:20px !important; text-align: center; color: #705335; margin-bottom: 30px; }
    .section-header { color: #5C3A21; border-bottom: 2px solid #D4A373; padding-bottom: 5px; margin-top: 20px; }
    
    /* Tarjetas decorativas para KPI o Conclusiones con fondo blanco y texto negro puro */
    .kpi-card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0px 4px 16px rgba(0,0,0,0.08);
        border-left: 5px solid #8B5A2B;
        margin-bottom: 20px;
        color: #000000 !important;
    }
    .kpi-card h3 {
        color: #1a1a1a !important;
    }
    .kpi-card p {
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# SIDEBAR / NAVEGACIÓN (CON TU LOGO)
# ==============================================================================
with st.sidebar:
    st.image(URL_LOGO, caption="☕ Café Artesanal CASAENZ", use_container_width=True)
    st.markdown("---")
    st.markdown("### 📋 Navegación del Proyecto")
    opcion = st.radio(
        "Selecciona la sección a exponer:",
        [
            "0. Introducción y Concepto",
            "1. Factores Críticos de Localización",
            "2. Técnicas de Localización",
            "3. Red de Suministros y Modelo Matemático",
            "4. Simulación en FlexSim",
            "5. Distribución de Planta (WD)",
            "6. Balanceo de Línea y Asignación de Puestos",
            "🎓 Conclusiones Generales"
        ]
    )
    st.sidebar.markdown("---")
    st.sidebar.info("**Autor:** Laura Juliana Loaiza Saavedra\n\n**ID:** 428429\n\n*Ingeniería Industrial*")

# ==============================================================================
# PÁGINA 0: INTRODUCCIÓN Y CONCEPTO
# ==============================================================================
if opcion == "0. Introducción y Concepto":
    st.markdown('<p class="main-title">Café Artesanal CASAENZ</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Desarrollo del Concepto del Producto y Distribución de Planta</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("☕ Propuesta de Valor")
        st.write("**Café Artesanal CASAENZ** es un café colombiano Premium cultivado y tostado de manera artesanal en el **Valle del Cauca**. Garantiza una experiencia sensorial auténtica mediante granos seleccionados y procesos tradicionales, alejados de la masificación industrial.")
        
        st.subheader
