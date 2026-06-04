import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Configuración inicial de la página
st.set_page_config(
    page_title="Proyecto Integrador - Café CASAENZ",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
# CONFIGURACIÓN DE ESTILOS LIMPIOS (MÁXIMA LEGIBILIDAD ACADÉMICA)
# ==============================================================================
st.markdown("""
    <style>
    /* Estilos de títulos y textos en tonos oscuros y elegantes */
    .main-title { font-size:40px !important; font-weight: bold; color: #4A3018; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:19px !important; text-align: center; color: #705335; margin-bottom: 30px; }
    .section-header { color: #5C3A21; border-bottom: 2px solid #D4A373; padding-bottom: 5px; margin-top: 25px; font-size:24px; font-weight:bold; }
    
    /* Cajas y Tarjetas informativas con fondo blanco */
    .kpi-card {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0px 3px 10px rgba(0,0,0,0.05);
        border-left: 5px solid #8B5A2B;
        margin-bottom: 15px;
    }
    .kpi-card h3 { color: #4A3018 !important; margin-top: 0; font-size:18px; }
    .kpi-card p { color: #2b2b2b !important; text-align: justify; line-height: 1.6; font-size: 14.5px; margin-bottom: 0; }
    
    /* Alertas y bloques estéticos */
    .theory-box {
        background-color: #fdfbf7;
        padding: 15px;
        border: 1px solid #e6dfd3;
        border-radius: 6px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# SIDEBAR / MENÚ DE NAVEGACIÓN (CON ARCHIVO DE LOGO LOCAL)
# ==============================================================================
with st.sidebar:
    try:
        st.image("logo.png", caption="☕ Café Artesanal CASAENZ", use_container_width=True)
    except:
        st.warning("⚠️ No se encontró el archivo 'logo.png' en la carpeta.")
        
    st.markdown("---")
    st.markdown("### 📋 Secciones del Proyecto")
    opcion = st.sidebar.radio(
        "Selecciona el capítulo a sustentar:",
        [
            "0. Introducción y Concepto",
            "1. Factores Críticos de Localización",
            "2. Técnicas de Localización Matemática",
            "3. Red de Suministros y Modelo",
            "4. Simulación de Operaciones (FlexSim)",
            "5. Distribución de Planta y Factor Wd",
            "6. Balanceo de Línea y Puestos",
            "🎓 Conclusiones Generales"
        ]
    )
    st.sidebar.markdown("---")
    st.sidebar.info("**Autor:** Laura Juliana Loaiza Saavedra\n\n**ID:** 428429\n\n*Ingeniería Industrial*")

# ==============================================================================
# PÁGINAS DEL PROYECTO
# ==============================================================================
if opcion == "0. Introducción y Concepto":
    st.markdown('<p class="main-title">Café Artesanal CASAENZ</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Desarrollo del Concepto del Producto y Distribución de Planta</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("☕ Propuesta de Valor")
        st.write("""
        **Café Artesanal CASAENZ** es un modelo de negocio enfocado en la producción de café colombiano Premium cultivado, 
        procesado y tostado de manera tradicional en el departamento del **Valle del Cauca**. 
        Garantiza una trazabilidad total y una experiencia sensorial auténtica mediante granos estrictamente seleccionados, 
        mitigando las cadenas de intermediación comercial masivas.
        """)
        st.subheader("🎯 Brecha de Mercado Identificada")
        st.write("""
        El proyecto captura la demanda insatisfecha del nicho de consumidores locales y nacionales que buscan cafés de especialidad 
        de origen regional real, combatiendo el marketing industrial engañoso de marcas tradicionales que etiquetan sus productos 
        como 'artesanales' recurriendo a producciones masivas altamente automatizadas.
        """)
    with col2:
        st.info("""
        ### 🏭 Alcance Técnico del Proyecto Integrador
        Esta aplicación web interactiva compila de manera sistémica y fundamentada las decisiones de **Ingeniería Industrial** que definen el diseño logístico y de manufactura de la organización:
        * **Macrolocalización y Microlocalización** fundamentada en costos y matrices multicriterio.
        * **Modelación matemática de transporte** para optimización de fletes en la red.
        * **Cálculo de esfuerzos de manejo de materiales** mediante factor Carga-Distancia ($W_D$).
        * **Ingeniería de Métodos** aplicada al balanceo analítico de la línea de empaque primario.
        """)

elif opcion == "1. Factores Críticos de Localización":
    st.markdown('<div class="section-header">📌 1. Factores Críticos de Localización de Planta y Centros</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown("Para el diseño de la red logística de **Café CASAENZ**, se determinaron **6 Factores Críticos de Localización (FCL)**:")
    
    factores = {
        "🌾 Proximidad a los Proveedores de Materia Prima": "Garantiza el suministro inmediato de café pergamino seco proveniente de las zonas cafeteras del Valle (Yotoco, Ginebra, Tuluá). Minimiza el deterioro del grano por humedad durante el transporte inicial y reduce el costo del flete de entrada.",
        "🛣️ Infraestructura y Conectividad Vial": "Evaluación del acceso directo a la red vial principal del departamento (especialmente la doble calzada Buga-Tuluá y accesos a Cali). Permite mitigar tiempos muertos logísticos y asegurar canales rápidos de distribución.",
        "🏪 Cercanía al Mercado Objetivo y Clientes Potenciales": "Ubicación estratégica respecto a los principales nodos de consumo urbano y centros de distribución comercial masiva (Cali, Palmira y Buga), optimizando los tiempos de entrega del producto terminado.",
        "💰 Costos Operativos Locales (Arriendos, Impuestos y Servicios)": "Impacto financiero directo derivado de las tarifas de impuesto de Industria y Comercio (ICA), costos de arrendamiento por metro cuadrado industrial y disponibilidad de servicios públicos de alta capacidad.",
        "👷 Disponibilidad de Mano de Obra Calificada": "Acceso a personal técnico capacitado en la región para operar maquinaria crítica (tostadoras industriales, molinos de precisión y sistemas de sellado neumático) y expertos en catación artesanal.",
        "🔒 Seguridad de la Zona y Entorno Comercial": "Mitigación del riesgo operacional asociado a pérdidas en inventarios, orden público y facilidad para el establecimiento de alianzas estratégicas con cooperativas de caficultores locales."
    }
    for f, desc in factores.items():
        with st.expander(f, expanded=True):
            st.markdown(f"<p style='color:#2b2b2b; font-size:14.5px;'>{desc}</p>", unsafe_allow_html=True)

elif opcion == "2. Técnicas de Localización Matemática":
    st.markdown('<div class="section-header">🧮 2. Modelación y Técnicas de Localización Aplicadas</div>', unsafe_allow_html=True)
    st.write("")
    
    tab1, tab2, tab3 = st.tabs(["📊 Punto de Equilibrio (CVU)", "📍 Centro de Gravedad (CEDI)", "🏆 Ponderación Multicriterio (AHP)"])
    
    with tab1:
        st.subheader("Análisis de Costo-Volumen-Utilidad (CVU) para Expansión de Capacidad")
        df_cvu = pd.DataFrame({
            "Ubicación": ["Región A", "Región B", "Región C"],
            "Costo Fijo Anual (CF)": [100000, 200000, 350000],
            "Costo Variable Unitario (cv)": [30, 20, 12]
        })
        st.dataframe(df_cvu, use_container_width=True)
        q_slider = st.slider("Modifica la cantidad de producción anual proyectada (Q):", 0, 25000, 15000, step=500)
        df_cvu["Costo Total ($)"] = df_cvu["Costo Fijo Anual (CF)"] + (df_cvu["Costo Variable Unitario (cv)"] * q_slider)
        st.write(f"### Resultados de Costo Total para Q = {q_slider:,} unidades/año")
        st.dataframe(df_cvu, use_container_width=True)
        
        q_range = np.linspace(0, 25000, 100)
        fig_cvu = go.Figure()
        fig_cvu.add_trace(go.Scatter(x=q_range, y=100000 + 30 * q_range, mode='lines', name='Región A', line=dict(color='#8B5A2B')))
        fig_cvu.add_trace(go.Scatter(x=q_range, y=200000 + 20 * q_range, mode='lines', name='Región B', line=dict(color='#D4A373')))
        fig_cvu.add_trace(go.Scatter(x=q_range, y=350000 + 12 * q_range, mode='lines', name='Región C', line=dict(color='#5C3A21')))
        fig_cvu.add_vline(x=q_slider, line_dash="dash", line_color="red")
        st.plotly_chart(fig_cvu, use_container_width=True)
        st.info("💡 **Análisis de Indiferencia:** Entre 10,000 y 18,750 unidades, la **Región B** es la más económica. Para producciones superiores a 18,750 unidades, la Región C minimiza los costos globales.")

    with tab2:
        st.subheader("Optimización de Ubicación de CEDI mediante Centro de Gravedad")
        df_cg = pd.DataFrame({
            "Ciudad Destino": ["Cali", "Tuluá", "Palmira"],
            "Coordenada X (Km)": [90, 130, 170],
            "Coordenada Y (Km)": [220, 240, 310],
            "Demanda Vi (Ton/mes)": [6200, 4800, 3500],
            "Costo Flete fi ($/Ton-Km)": [3600, 30000, 2500]
        })
        st.dataframe(df_cg, use_container_width=True)
        x_opt, y_opt = 118.06, 243.66
        costo_total_opt = 3354773746.00
        
        col1, col2 = st.columns(2)
        col1.metric("Centro de Gravedad Óptimo", f"X: {x_opt}, Y: {y_opt}")
        col2.metric("Costo Mínimo de Flete de la Red", f"$ {costo_total_opt:,.2f} COP")
        
        fig_cg = go.Figure()
        fig_cg.add_trace(go.Scatter(x=df_cg["Coordenada X (Km)"], y=df_cg["Coordenada Y (Km)"], mode='markers+text', text=df_cg["Ciudad Destino"], textposition
