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
# 🛠️ CONFIGURACIÓN AUTOMÁTICA DEL LOGO DESDE TU REPOSITORIO DE GITHUB
# ==============================================================================
USER_GITHUB = "lloaizasaav1-sudo"
REPO_GITHUB = "Distribucion-de-Planta-CASAENZ"

# Ruta en formato Raw para enlazar directamente tu logo subido
URL_LOGO = f"https://raw.githubusercontent.com/{USER_GITHUB}/{REPO_GITHUB}/main/logo.png"

st.markdown(f"""
    <style>
    /* Fondo de color sólido limpio para máxima legibilidad */
    .stApp {{
        background-color: #FDFBF7; 
    }}
    
    /* LETRA NEGRA EN TODO EL APLICATIVO */
    h1, h2, h3, h4, h5, h6, p, li, span, label {{
        color: #000000 !important;
    }}
    
    /* Títulos y textos estilizados con color negro */
    .main-title {{ 
        font-size:42px !important; 
        font-weight: bold; 
        color: #000000 !important; 
        text-align: center; 
        margin-bottom: 5px; 
    }}
    .subtitle {{ 
        font-size:20px !important; 
        text-align: center; 
        color: #1A1A1A !important; 
        margin-bottom: 30px; 
    }}
    .section-header {{ 
        color: #000000 !important; 
        border-bottom: 2px solid #000000; 
        padding-bottom: 5px; 
        margin-top: 20px; 
    }}
    
    /* Estilos para las tarjetas de conclusión (Fondo blanco, texto negro) */
    .conclusion-card {{
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 8px;
        border-left: 5px solid #000000;
        margin-bottom: 15px;
        box-shadow: 1px 1px 5px rgba(0,0,0,0.1);
    }}
    .conclusion-card h4 {{
        color: #000000 !important;
        font-weight: bold;
        margin-top: 0;
    }}
    .conclusion-card p {{
        color: #000000 !important;
    }}
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# SIDEBAR / NAVEGACIÓN
# ==============================================================================
with st.sidebar:
    # Desplegar el Logo de la Empresa en la parte superior del menú lateral
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
            "7. Conclusión General del Proyecto"
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
        st.write("""
        Café Artesanal CASAENZ es un café colombiano Premium cultivado y tostado de manera artesanal en el Valle del Cauca, 
        que busca ofrecer una experiencia sensorial auténtica a través de granos cuidadosamente seleccionados y procesos tradicionales de producción.
        """)
        
        st.subheader("🎯 Brecha de Mercado")
        st.write("""
        Satisface la necesidad creciente de los consumidores por productos auténticos, de alta calidad y con identidad de origen, combatiendo el marketing engañoso de marcas masivas.
        """)
    
    with col2:
        st.info("""
        ### 🏭 Objetivos Estratégicos de la Exposición
        Este aplicativo web interactivo presenta las decisiones de Ingeniería Industrial tomadas para el diseño del sistema logístico y productivo de la empresa:
        * Localización macro y micro industrial.
        * Modelación matemática de transporte.
        * Distribución física y cálculo de esfuerzos de manejo de materiales (W_D).
        * Balanceo óptimo de la línea de producción.
        """)

# ==============================================================================
# PÁGINA 1: FACTORES CRÍTICOS DE LOCALIZACIÓN
# ==============================================================================
elif opcion == "1. Factores Críticos de Localización":
    st.header
