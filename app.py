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

# Estilos personalizados para mejorar la estética (Colores cálidos originales)
st.markdown("""
    <style>
    .main-title { font-size:42px !important; font-weight: bold; color: #4A3018; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:20px !important; text-align: center; color: #705335; margin-bottom: 30px; }
    .section-header { color: #5C3A21; border-bottom: 2px solid #D4A373; padding-bottom: 5px; }
    
    /* Estilos para las tarjetas de conclusión */
    .conclusion-card {
        background-color: #FDFBF7;
        padding: 20px;
        border-radius: 8px;
        border-left: 5px solid #5C3A21;
        margin-bottom: 15px;
        box-shadow: 1px 1px 5px rgba(0,0,0,0.05);
    }
    .conclusion-card h4 {
        color: #4A3018 !important;
        font-weight: bold;
        margin-top: 0;
    }
    .conclusion-card p {
        color: #333333 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# CONFIGURACIÓN AUTOMÁTICA DEL LOGO DESDE TU REPOSITORIO DE GITHUB
# ==============================================================================
USER_GITHUB = "lloaizasaav1-sudo"
REPO_GITHUB = "Distribucion-de-Planta-CASAENZ"
URL_LOGO = f"https://raw.githubusercontent.com/{USER_GITHUB}/{REPO_GITHUB}/main/logo.png"

# ==============================================================================
# SIDEBAR / NAVEGACIÓN
# ==============================================================================
with st.sidebar:
    # Desplegar tu Logo Real de GitHub
    st.image(URL_LOGO, caption="☕ Café Artesanal CASAENZ", use_container_width=True)
    st.markdown("### 📋 Navegación del Proyecto")
    opcion = st.radio(
        "Selecciona la sección a exponer:",
        [
            "0. Introducción y Concepto",
            "1. Factores Críticos de Localización",
            "2. Técnicas de Localización (CVU, Factor Rating, Centro de Gravedad)",
            "3. Red de Suministros y Modelo Matemático",
            "4. Simulación en FlexSim",
            "5. Distribución de Planta (Diagrama de Hilos, Bloques y WD)",
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
        **Café Artesanal CASAENZ** es un café colombiano Premium cultivado y tostado de manera artesanal en el **Valle del Cauca**. 
        Garantiza una experiencia sensorial auténtica mediante granos seleccionados y procesos tradicionales, alejados de la masificación industrial.
        """)
        
        st.subheader("🎯 Brecha de Mercado")
        st.write("""
        Satisface el nicho de consumidores que buscan cafés de especialidad de origen regional real, combatiendo el marketing engañoso de marcas masivas que usan el término 'artesanal' sin serlo.
        """)
    
    with col2:
        st.info("""
        ### 🏭 Objetivos Estratégicos de la Exposición
        Este aplicativo web interactivo presenta las decisiones de **Ingeniería Industrial** tomadas para el diseño del sistema logístico y productivo de la empresa:
        * Localización macro y micro industrial.
        * Modelación matemática de transporte.
        * Distribución física y cálculo de esfuerzos de manejo de materiales ($W_D$).
        * Balanceo óptimo de la línea de producción.
        """)

# ==============================================================================
# PÁGINA 1: FACTORES CRÍTICOS DE LOCALIZACIÓN
# ==============================================================================
elif opcion == "1. Factores Críticos de Localización":
    st.header("📌 1. Factores Críticos de Localización")
    st.write("Para localizar la planta y los centros de operaciones se evaluaron 6 factores críticos prioritarios:")
    
    factores = {
        "Proximidad a Proveedores": "Asegura la frescura del grano (café pergamino de Yotoco, Tuluá, Ginebra) y reduce costos de transporte de entrada.",
        "Infraestructura Vial": "Conexión directa con los corredores logísticos principales del Valle del Cauca para mitigar tiempos muertos.",
        "Cercanía al Mercado": "Acceso rápido a los principales centros de consumo urbano del departamento (Cali, Palmira, Buga).",
        "Costos Operativos": "Evaluación del impacto financiero en arriendos, servicios públicos, impuestos locales y mano de obra.",
        "Disponibilidad de Mano de Obra": "Acceso a personal operativo capacitado en técnicas de producción, tostión y empaque.",
        "Seguridad y Entorno Comercial": "Mitigación de riesgos operacionales y fomento de alianzas estratégicas regionales."
    }
    
    for f, desc in factores.items():
        with st.expander(f"🔹 {f}"):
            st.write(desc)

# ==============================================================================
# PÁGINA 2: TÉCNICAS DE LOCALIZACIÓN
# ==============================================================================
elif opcion == "2. Técnicas de Localización (CVU, Factor Rating, Centro de Gravedad)":
    st.header("🧮 2. Técnicas de Localización Aplicadas")
    
    tab1, tab2, tab3 = st.tabs(["Costo-Volumen-Utilidad", "Calificación de Factores", "Centro de Gravedad"])
    
    # 2.1 CVU
    with tab1:
        st.subheader("📊 Método Costo - Volumen - Utilidad (CVU)")
        st.write("Fórmula utilizada:  $$CT = CF + (CV \\cdot Q)$$")
        
        df_cvu = pd.DataFrame({
            "Ciudad": ["Cali", "Palmira", "Buga"],
            "Costos Fijos ($)": [4500000, 3200000, 2800000],
            "Costo Variable Unitario ($)": [3500, 4200, 4800]
        })
        
        st.dataframe(df_cvu, use_container_width=True)
        q_slider = st.slider("Ajusta la cantidad de producción mensual (Q):", 1000, 15000, 10000, step=500)
        
        df_cvu["Costo Total ($)"] = df_cvu["Costos Fijos ($)"] + (df_cvu["Costo Variable Unitario ($)"] * q_slider)
        st.write(f"### Resultados para Q = {q_slider:,} unidades")
        st.dataframe(df_cvu, use_container_width=True)
        
        q_range = np.linspace(0, 15000, 100)
        fig_cvu = go.Figure()
        for idx, row in df_cvu.iterrows():
            fig_cvu.add_trace(go.Scatter(x=q_range, y=row["Costos Fijos ($)"] + row["Costo Variable Unitario ($)"] * q_range, mode='lines', name=row["Ciudad"]))
        fig_cvu.add_vline(x=q_slider, line_dash="dash", line_color="red", annotation_text="Q actual")
        fig_cvu.update_layout(title="Curvas de Costo Total por Localización", xaxis_title="Volumen (Q)", yaxis_title="Costo Total ($)")
        st.plotly_chart(fig_cvu, use_container_width=True)
        st.success("💡 **Conclusión CVU:** Cali representa la alternativa más económica a altos volúmenes gracias a su bajo costo variable unitario.")

    # 2.2 Factor Rating
    with tab2:
        st.subheader("🎯 Método de Calificación de Factores (Factor Rating)")
        
        peso = [0.25, 0.20, 0.25, 0.20, 0.10]
        factores_labels = ["Cercanía a proveedores", "Infraestructura vial", "Cercanía al mercado", "Costos operativos", "Mano de obra"]
        calif_cali = [8, 9, 10, 7, 9]
        calif_palmira = [8, 8, 8, 8, 8]
        calif_buga = [9, 7, 7, 9, 7]
        
        df_fr = pd.DataFrame({
            "Factor Crítico": factores_labels,
            "Peso (W)": peso,
            "Cali": calif_cali,
            "Palmira": calif_palmira,
            "Buga": calif_buga
        })
        st.dataframe(df_fr, use_container_width=True)
        
        score_cali = sum(w*c for w, c in zip(peso, calif_cali))
        score_palmira = sum(w*c for w, c in zip(peso, calif_palmira))
        score_buga = sum(w*c for w, c in zip(peso, calif_buga))
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Puntuación Cali", f"{score_cali:.2f}", delta="Ganador")
        col2.metric("Puntuación Palmira", f"{score_palmira:.2f}")
        col3.metric("Puntuación Buga", f"{score_buga:.2f}")
        
        fig_fr = px.bar(x=["Cali", "Palmira", "Buga"], y=[score_cali, score_palmira, score_buga], labels={'x': 'Ciudad', 'y': 'Puntuación Ponderada'}, title="Comparación de Puntajes de Factores")
        st.plotly_chart(fig_fr, use_container_width=True)

    # 2.3 Centro
