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
# CONFIGURACIÓN DEL LOGO REAL DESDE TU REPOSITORIO DE GITHUB Y FONDO
# ==============================================================================
URL_LOGO = "https://raw.githubusercontent.com/lloaizasaav1-sudo/Distribucion-de-Planta-CASAENZ/main/logo.png" 
URL_FONDO = "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?q=80&w=1600&auto=format&fit=crop"

st.markdown(f"""
    <style>
    /* Fondo personalizado para toda la aplicación con opacidad para lectura clara */
    .stApp {{
        background: linear-gradient(rgba(255, 255, 255, 0.92), rgba(245, 235, 224, 0.95)), 
                    url("{URL_FONDO}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* Títulos y textos estilizados */
    .main-title {{ font-size:42px !important; font-weight: bold; color: #4A3018; text-align: center; margin-bottom: 5px; }}
    .subtitle {{ font-size:20px !important; text-align: center; color: #705335; margin-bottom: 30px; }}
    .section-header {{ color: #5C3A21; border-bottom: 2px solid #D4A373; padding-bottom: 5px; margin-top: 20px; }}
    
    /* Tarjetas decorativas para KPI o Conclusiones */
    .kpi-card {{
        background-color: white;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 2px 2px 12px rgba(0,0,0,0.06);
        border-left: 5px solid #8B5A2B;
        margin-bottom: 20px;
    }}
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# SIDEBAR / NAVEGACIÓN
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
        
        st.subheader("🎯 Brecha de Mercado")
        st.write("Satisface el nicho de consumidores que buscan cafés de especialidad de origen regional real, combatiendo el marketing engañoso de marcas masivas que usan el término 'artesanal' sin serlo.")
    
    with col2:
        st.info("### 🏭 Objetivos Estratégicos de la Exposición\nEste aplicativo web interactivo presenta las decisiones de **Ingeniería Industrial** tomadas para el diseño del sistema logístico
