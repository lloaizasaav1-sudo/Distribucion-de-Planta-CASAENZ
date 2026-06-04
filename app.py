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
# CONFIGURACIÓN DE ESTILOS LIMPIOS (LETRA OSCURA Y FONDO BLANCO ESTÁNDAR)
# ==============================================================================
URL_LOGO = "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?q=80&w=200&auto=format&fit=crop" 

st.markdown("""
    <style>
    /* Títulos y textos estilizados con colores oscuros de alta legibilidad */
    .main-title { font-size:42px !important; font-weight: bold; color: #4A3018; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:20px !important; text-align: center; color: #705335; margin-bottom: 30px; }
    .section-header { color: #5C3A21; border-bottom: 2px solid #D4A373; padding-bottom: 5px; margin-top: 20px; }
    
    /* Tarjetas decorativas para KPI y Conclusiones */
    .kpi-card {
        background-color: white;
        padding: 22px;
        border-radius: 10px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
        border-left: 5px solid #8B5A2B;
        margin-bottom: 15px;
    }
    .kpi-card h3 { color: #4A3018 !important; margin-top: 0; }
    .kpi-card p { color: #1a1a1a !important; text-align: justify; line-height: 1.5; font-size: 15px; }
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
            "1. Técnicas de Localización (Tus Ejercicios)",
            "2. Red de Suministros y Distribución",
            "3. Balanceo de Línea y Asignación de Puestos",
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
        Este aplicativo web interactivo presenta las decisiones de **Ingeniería Industrial** tomadas para el diseño del sistema logístico y productivo de la empresa basándose en los ejercicios matemáticos de modelación:
        * Análisis de Punto de Equilibrio de Localización por Regiones.
        * Determinación del Centro de Gravedad Óptimo (Cedi).
        * Evaluación multicriterio de alternativas mediante Ponderación AHP.
        """)

# ==============================================================================
# PÁGINA 1: TÉCNICAS DE LOCALIZACIÓN (TUS EJERCICIOS)
# ==============================================================================
elif opcion == "1. Técnicas de Localización (Tus Ejercicios)":
    st.header("🧮 Técnicas de Localización y Análisis Multicriterio")
    
    tab1, tab2, tab3 = st.tabs(["Punto de Equilibrio (CVU)", "Centro de Gravedad", "Ubicación CEDI (AHP/Ponderación)"])
    
    # --- TAB 1: PUNTO DE EQUILIBRIO ---
    with tab1:
        st.subheader("📊 Análisis de Costo-Volumen-Utilidad por Región")
        df_cvu = pd.DataFrame({
            "Ubicación": ["Región A", "Región B", "Región C"],
            "Costo Fijo (CF)": [100000, 200000, 350000],
            "Costo Variable (cv)": [30, 20, 12]
        })
        st.dataframe(df_cvu, use_container_width=True)
        
        q_slider = st.slider("Ajusta el volumen proyectado de producción al año (Q):", 0, 25000, 15000, step=500)
        df_cvu["Costo Total ($)"] = df_cvu["Costo Fijo (CF)"] + (df_cvu["Costo Variable (cv)"] * q_slider)
        
        st.write(f"### Resultados del Costo Total para Q = {q_slider:,} unidades")
        st.dataframe(df_cvu, use_container_width=True)
        
        q_range = np.linspace(0, 25000, 100)
        fig_cvu = go.Figure()
        fig_cvu.add_trace(go.Scatter(x=q_range, y=100000 + 30 * q_range, mode='lines', name='Región A'))
        fig_cvu.add_trace(go.Scatter(x=q_range, y=200000 + 20 * q_range, mode='lines', name='Región B'))
        fig_cvu.add_trace(go.Scatter(x=q_range, y=350000 + 12 * q_range, mode='lines', name='Región C'))
        fig_cvu.add_vline(x=q_slider, line_dash="dash", line_color="red", annotation_text=f"Q actual")
        fig_cvu.update_layout(title="Gráfico de Punto de Equilibrio de Localización", xaxis_title="Volumen Anual (Q)", yaxis_title="Costo Total ($)")
        st.plotly_chart(fig_cvu, use_container_width=True)

    # --- TAB 2: CENTRO DE GRAVEDAD ---
    with tab2:
        st.subheader("📍 Método del Centro de Gravedad para Planta/CEDI")
        df_cg = pd.DataFrame({
            "Ciudad": ["Cali", "Tuluá", "Palmira"],
            "Coordenada X (Km)": [90, 130, 170],
            "Coordenada Y (Km)": [220, 240, 310],
            "Demanda Vi (Ton/mes)": [6200, 4800, 3500],
            "Costo Flete fi (Cop/Ton-Km)": [3600, 30000, 2500]
        })
        st.dataframe(df_cg, use_container_width=True)
        
        x_opt, y_opt = 118.06, 243.66
        costo_total_opt = 3354773746.00
        
        col1, col2 = st.columns(2)
        col1.metric("Punto Óptimo Calculado (Centro de Gravedad)", f"X: {x_opt}, Y: {y_opt}")
        col2.metric("Costo Mínimo de Transporte Total", f"$ {costo_total_opt:,.2f} COP")
        
        fig_cg = go.Figure()
        fig_cg.add_trace(go.Scatter(x=df_cg["Coordenada X (Km)"], y=df_cg["Coordenada Y (Km)"], mode='markers+text', text=df_cg["Ciudad"], textposition="top center", marker=dict(size=12, color='brown'), name="Ciudades"))
        fig_cg.add_trace(go.Scatter(x=[x_opt], y=[y_opt], mode='markers+text', text=["CEDI IDEAL"], textposition="bottom center", marker=dict(size=15, color='red', symbol='star'), name="Cedi Ideal"))
        fig_cg.update_layout(title="Mapa de Coordenadas de Localización del CEDI", xaxis_title="Eje X (Km)", yaxis_title="Eje Y (Km)")
        st.plotly_chart(fig_cg, use_container_width=True)

    # --- TAB 3: MODELO MULTICRITERIO AHP ---
    with tab3:
        st.subheader("🏆 Evaluación de Distribución/Ubicación de Cedi mediante AHP")
        df_ahp = pd.DataFrame({
            "Alternativa de Distribución": ["A1 (Célula en U)", "A2 (Lineal)", "A3 (Por Proceso)"],
            "Costo de Materia Prima": [0.2014, 0.6479, 0.3395],
            "Flexibilidad Operativa": [0.6479, 0.2014, 0.4545],
            "Prioridad Global Ponderada": ["64.79 %", "20.14 %", "33.95 %"]
        })
        st.dataframe(df_ahp, use_container_width=True)

# ==============================================================================
# PÁGINA 2: RED DE SUMINISTROS Y DISTRIBUCIÓN
# ==============================================================================
elif opcion == "2. Red de Suministros y Distribución":
    st.header("🌐 Red de Suministros y Manejo de Materiales")
    df_wd = pd.DataFrame({
        "Ruta (Flujo Interno)": ["A - C (Recepción a Stock)", "C - D (Stock a Tostión)", "D - E (Tostión a Empaque)", "E - F (Empaque a Listo)", "F - G (Listo a Despacho)"],
        "Distancia D_i (m)": [8, 12, 6, 5, 10],
        "Carga W_i (kg/sem)": [500, 500, 480, 480, 480]
    })
    df_wd["Esfuerzo WD (kg·m)"] = df_wd["Distancia D_i (m)"] * df_wd["Carga W_i (kg/sem)"]
    st.dataframe(df_wd, use_container_width=True)
    st.metric("Factor WD Total Semanal", f"{df_wd['Esfuerzo WD (kg·m)'].sum():,} kg·m/semana")

# ==============================================================================
# PÁGINA 3: BALANCEO DE LÍNEA Y ASIGNACIÓN
# ==============================================================================
elif opcion == "3. Balanceo de Línea y Asignación de Puestos":
    st.header("⚡ Ingeniería de Métodos: Balanceo de Línea")
    st.markdown("### Parámetros de Entrada de la Línea de Empaque (Café de 500g)")
    st.markdown("* **Jornada Laboral:** 8 horas/día = 28,800 segundos/día.\n* **Tasa de Producción Deseada:** 320 unidades/día.")
    st.latex(r"T_c = \frac{28800 \text{ seg}}{320 \text{ und}} = 90 \text{ segundos/unidad}")

    df_tareas = pd.DataFrame({
        "Tarea": ["A", "B", "C", "D", "E", "F", "G"],
        "Operación": ["Recepción y limpieza", "Tostión artesanal", "Enfriamiento controlado", "Molienda automatizada", "Dosificación exacta", "Sellado térmico", "Etiquetado manual"],
        "Tiempo (seg)": [40, 85, 30, 50, 25, 35, 20]
    })
    st.dataframe(df_tareas, use_container_width=True)
    
    df_puestos = pd.DataFrame({
        "Estación": ["Puesto 1", "Puesto 2", "Puesto 3", "Puesto 4"],
        "Tareas": ["A + C", "B (Cuello de botella)", "D + E", "F + G"],
        "Tiempo Real (seg)": [70, 85, 75, 55],
        "Tiempo de Ocio (seg)": [20, 5, 15, 35]
    })
    st.dataframe(df_puestos, use_container_width=True)
    
    fig_linea = go.Figure()
    fig_linea.add_trace(go.Bar(x=df_puestos["Estación"], y=df_puestos["Tiempo Real (seg)"], name="Tiempo Productivo", marker_color='#5C3A21'))
    fig_linea.add_trace(go.Bar(x=df_puestos["Estación"], y=df_puestos["Tiempo de Ocio (seg)"], name="Tiempo de Ocio", marker_color='#D4A373'))
    fig_linea.add_hline(y=90, line_dash="dash", line_color="red", annotation_text="Límite Ciclo (90s)")
    fig_linea.update_layout(barmode='stack', title="Carga de Trabajo por Operario vs Tiempo de Ciclo Máximo")
    st.plotly_chart(fig_linea, use_container_width=True)

# ==============================================================================
# PÁGINA 4: CONCLUSIONES GENERALES (SECCIÓN NUEVA AGREGADA)
# ==============================================================================
elif opcion == "🎓 Conclusiones Generales":
    st.markdown('<p class="main-title">Conclusiones del Análisis de Ingeniería</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Sustentación de Decisiones Basadas en Datos Matemáticos</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="kpi-card">
        <h3>📊 1. Optimización Financiera (Punto de Equilibrio)</h3>
        <p>
            El análisis Costo-Volumen-Utilidad determinó con precisión que el volumen de producción proyectado anual 
            dictamina de manera directa la mejor macro-localización geográfica. Para el escenario base de 15,000 unidades anuales, 
            la <b>Región B</b> representa la alternativa óptima con un costo total mínimo de $500,000, superando los sobrecostos variables 
            de la Región A y mitigando los elevados costos fijos de la Región C.
        </p>
    </div>
    
    <div class="kpi-card">
        <h3>📍 2. Eficiencia Logística y de Transporte (Centro de Gravedad)</h3>
        <p>
            Al evaluar el peso de la demanda y el impacto tarifario de los fletes para Cali, Tuluá y Palmira, el modelo matemático localiza 
            el Centro de Distribución (CEDI) ideal en las coordenadas <b>X: 118.06, Y: 243.66</b>. Ubicar la infraestructura logística en este 
            punto estratégico minimiza el gasto en transporte a un costo óptimo total de <b>$3,354,773,746.00 COP</b> mensuales, contrarrestando la criticidad del flete en Tuluá.
        </p>
    </div>
    
    <div class="kpi-card">
        <h3>🏆 3. Diseño del Flujo de Planta (Ponderación Multicriterio AHP)</h3>
        <p>
            La matriz de priorización analítica (AHP) resolvió que los criterios de flexibilidad operativa y seguridad del operario superaban la variable estricta de costo inicial. 
            Con una prioridad global dominante del <b>64.79%</b>, la configuración de la distribución física en <b>A1 (Célula en U)</b> se consolida como el diseño ganador para los flujos internos del Cedi, asegurando un sistema adaptable y esbelto.
        </p>
    </div>
    
    <div class="kpi-card">
        <h3>⚡ 4. Productividad y Balanceo Operativo de Línea</h3>
        <p>
            Con una jornada laboral de 8 horas y un requerimiento de 320 unidades diarias, se estableció un tiempo de ciclo estricto de 90 segundos. 
            La distribución balanceada en 4 estaciones de trabajo alcanza una elevada eficiencia global del <b>79.17%</b>, identificando la operación de 
            <b>Tostión (Puesto 2)</b> como el cuello de botella físico del proceso productivo con 85 segundos utilizados, sobre el cual se deben enfocar los esfuerzos de control de calidad.
        </p>
    </div>
    """, unsafe_allow_html=True)
