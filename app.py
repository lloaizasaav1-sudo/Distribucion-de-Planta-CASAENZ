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
# PERSONALIZACIÓN LOGO (DISEÑO VISUAL AVANZADO)
# ==============================================================================
# Nota: Puedes cambiar las URLs por los enlaces directos de tus propias imágenes
URL_LOGO = "https://github.com/lloaizasaav1-sudo/Distribucion-de-Planta-CASAENZ/blob/main/logo.png" 
URL_FONDO = "https://https://github.com/lloaizasaav1-sudo/Distribucion-de-Planta-CASAENZ/blob/main/fondo.png"

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
    
    /* Tarjetas decorativas para KPI */
    .kpi-card {{
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        border-left: 5px solid #8B5A2B;
        text-align: center;
    }}
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# SIDEBAR / NAVEGACIÓN
# ==============================================================================
with st.sidebar:
    # Desplegar el Logo de la Empresa en la parte superior del menú
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
            "6. Balanceo de Línea y Asignación de Puestos"
            "7. Conclusión"
            
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
elif opcion == "2. Técnicas de Localización":
    st.header("🧮 2. Técnicas de Localización Aplicadas")
    
    tab1, tab2, tab3 = st.tabs(["Costo-Volumen-Utilidad", "Calificación de Factores", "Centro de Gravedad"])
    
    with tab1:
        st.subheader("📊 Método Costo - Volumen - Utilidad (CVU)")
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
        fig_cvu.add_vline(x=q_slider, line_dash="dash", line_color="red", annotation_text=f"Q actual")
        fig_cvu.update_layout(title="Curvas de Costo Total por Localización", xaxis_title="Volumen (Q)", yaxis_title="Costo Total ($)")
        st.plotly_chart(fig_cvu, use_container_width=True)

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

    with tab3:
        st.subheader("📍 Método del Centro de Gravedad")
        df_cg = pd.DataFrame({
            "Ciudad Destino": ["Cali", "Palmira", "Buga"],
            "Coordenada X": [100, 115, 120],
            "Coordenada Y": [200, 215, 280],
            "Demanda Vi (kg)": [5000, 4100, 3200],
            "Costo fi ($)": [3500, 2800, 2100]
        })
        st.dataframe(df_cg, use_container_width=True)
        x_opt, y_opt = 108.59, 219.83
        st.metric("Coordenada Óptima Calculada", f"X: {x_opt}, Y: {y_opt}")

# ==============================================================================
# PÁGINA 3: RED DE SUMINISTROS
# ==============================================================================
elif opcion == "3. Red de Suministros y Modelo Matemático":
    st.header("🌐 3. Diseño de la Red de Suministros")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🌾 Oferta de Proveedores")
        st.table(pd.DataFrame({"Proveedor": ["Yotoco", "Tuluá", "Ginebra"], "Oferta (kg)": [700, 500, 400]}))
    with col2:
        st.markdown("### 🏪 Demanda del Mercado")
        st.table(pd.DataFrame({"Destino": ["Cali", "Palmira", "Buga", "Tuluá"], "Demanda (kg)": [400, 500, 300, 400]}))

# ==============================================================================
# PÁGINA 4: SIMULACIÓN EN FLEXSIM
# ==============================================================================
elif opcion == "4. Simulación en FlexSim":
    st.header("🏭 4. Modelación y Simulación en FlexSim")
    st.info("💡 Usa esta sección como soporte visual mientras proyectas el archivo de FlexSim real en tu clase.")
    st.markdown("""
    * **Distribución Adoptada:** Por Producto / En Línea de Flujo Continuo.
    * **Flujo del Simulador:** Source (Café Pergamino) ➔ Queues (Almacenamiento temporal) ➔ Processors (Tostadora, Molino, Selladora) ➔ Sink (Despacho final).
    """)
    st.progress(100)

# ==============================================================================
# PÁGINA 5: DISTRIBUCIÓN DE PLANTA
# ==============================================================================
elif opcion == "5. Distribución de Planta (WD)":
    st.header("📐 5. Diseño Espacial y Factor Carga-Distancia ($W_D$)")
    df_wd = pd.DataFrame({
        "Ruta (Flujo)": ["A - C (Recepción a Stock)", "C - D (Stock a Tostión)", "D - E (Tostión a Empaque)", "E - F (Empaque a Listo)", "F - G (Listo a Despacho)"],
        "Distancia D_i (m)": [8, 12, 6, 5, 10],
        "Carga W_i (kg/sem)": [500, 500, 480, 480, 480]
    })
    df_wd["Esfuerzo WD (kg·m)"] = df_wd["Distancia D_i (m)"] * df_wd["Carga W_i (kg/sem)"]
    st.dataframe(df_wd, use_container_width=True)
    st.metric("Factor WD Total Semanal", f"{df_wd['Esfuerzo WD (kg·m)'].sum():,} kg·m/semana")

# ==============================================================================
# PÁGINA 6: BALANCEO DE LÍNEA Y ASIGNACIÓN (SITUACIÓN RESUELTA)
# ==============================================================================
elif opcion == "6. Balanceo de Línea y Asignación de Puestos":
    st.header("⚡ 6. Ingeniería de Métodos: Balanceo de Líneas de Producción")
    
    st.markdown("""
    Para responder con rigor al requerimiento académico, se estructuró un análisis completo de balanceo para una línea de producción dedicada al empaque de **Café de 500g**.
    
    ### 📊 Parámetros de Entrada del Sistema
    * **Jornada Laboral Única:** 8 horas/día = 480 minutos/día = **28,800 segundos/día**.
    * **Tasa de Producción Deseada ($R$):** **320 unidades/día**.
    * **Tiempo de Ciclo Máximo ($T_c$):** """)
    st.latex(r"T_c = \frac{\text{Tiempo Disponible}}{\text{Tasa de Producción}} = \frac{28800 \text{ seg}}{320 \text{ und}} = 90 \text{ segundos/unidad}")

    # Tabla de Tiempos y Precedencias Reales
    st.subheader("📋 1. Análisis de Precedencias y Tiempos de Tarea")
    df_tareas = pd.DataFrame({
        "Tarea": ["A", "B", "C", "D", "E", "F", "G"],
        "Descripción de la Operación": [
            "Recepción, pesado y limpieza del grano verde",
            "Tostión artesanal (Operación Crítica)",
            "Enfriamiento controlado en bandeja",
            "Molienda fina/media automatizada",
            "Dosificación exacta en báscula (500g)",
            "Sellado térmico y fechado de la bolsa",
            "Etiquetado manual e inspección de calidad"
        ],
        "Tiempo (seg)": [40, 85, 30, 50, 25, 35, 20],
        "Precedencia": ["-", "A", "B", "C", "D", "E", "F"]
    })
    st.dataframe(df_tareas, use_container_width=True)
    
    tiempo_total_operacion = df_tareas["Tiempo (seg)"].sum()
    
    # Cálculos Teóricos de Ingeniería
    min_teorico = int(np.ceil(tiempo_total_operacion / 90))
    
    # Asignación Heurística de Puestos Realizada (Regla de Mayor Tiempo de Tarea)
    st.subheader("🛠️ 2. Diseño Estructural de los Puestos de Trabajo (Asignación Óptima)")
    st.write("Aplicando las restricciones de precedencia y cuidando no exceder el $T_c = 90$ segundos por puesto, la configuración ideal es:")
    
    df_puestos = pd.DataFrame({
        "Estación (Puesto)": ["Puesto 1", "Puesto 2", "Puesto 3", "Puesto 4"],
        "Tareas Asignadas": ["A + C (Pesado + Enfriamiento)", "B (Tostión - Cuello de Botella)", "D + E (Molienda + Dosificación)", "F + G (Sellado + Etiquetado)"],
        "Tiempo de Ciclo Real (seg)": [40 + 30, 85, 50 + 25, 35 + 20],
    })
    df_puestos["Tiempo de Ocio (seg)"] = 90 - df_puestos["Tiempo de Ciclo Real (seg)"]
    st.dataframe(df_puestos, use_container_width=True)
    
    # Indicadores de Desempeño Económico-Operativo
    st.subheader("📈 3. Indicadores de Eficiencia del Balanceo")
    
    n_estaciones = len(df_puestos)
    eficiencia = (tiempo_total_operacion / (n_estaciones * 90)) * 100
    retraso_balanceo = 100 - eficiencia
    tiempo_ocio_total = df_puestos["Tiempo de Ocio (seg)"].sum()
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Mínimo Teórico de Operarios", f"{min_teorico} operarios")
    with col2:
        st.metric("Eficiencia Global de Línea", f"{eficiencia:.2f} %")
    with col3:
        st.metric("Retraso de Balanceo", f"{retraso_balanceo:.2f} %")
    with col4:
        st.metric("Tiempo Muerto Total por Unidad", f"{tiempo_ocio_total} seg")

    # Gráfico interactivo de balance de cargas
    fig_linea = go.Figure()
    fig_linea.add_trace(go.Bar(
        x=df_puestos["Estación (Puesto)"],
        y=df_puestos["Tiempo de Ciclo Real (seg)"],
        name="Tiempo Utilizado",
        marker_color='#5C3A21'
    ))
    fig_linea.add_trace(go.Bar(
        x=df_puestos["Estación (Puesto)"],
        y=df_puestos["Tiempo de Ocio (seg)"],
        name="Tiempo Muerto (Ocio)",
        marker_color='#D4A373'
    ))
    fig_linea.add_hline(y=90, line_dash="dash", line_color="red", annotation_text="Límite del Ciclo (90 seg)")
    fig_linea.update_layout(
        title="Distribución de la Carga de Trabajo por Puesto de Operario",
        barmode='stack',
        xaxis_title="Puestos de Trabajo",
        yaxis_title="Segundos"
    )
    st.plotly_chart(fig_linea, use_container_width=True)
    
    st.success("""
    💡 **Conclusión del Balanceo:** La línea quedó balanceada con **4 estaciones** de trabajo estables. 
    El **Puesto 2 (Tostión)** es el cuello de botella físico del sistema productivo con 85 segundos. 
    Contamos con una excelente eficiencia operativa del **79.17%**, minimizando costos de mano de obra ocio.
    """)
    
    # ==============================================================================
# PÁGINA: CONCLUSIONES GENERALES DEL PROYECTO
# ==============================================================================
elif opcion == "🎓 Conclusiones Generales":
    st.header("🎓 Conclusiones Generales del Proyecto Integrador")
    st.write("Cierre estratégico y académico sobre las decisiones de diseño para **Café Artesanal CASAENZ**:")
    
    st.markdown("""
    <div class="kpi-card">
        <h3 style='color: #000000; margin-top:0;'>📐 Perspectiva de la Ingeniería Industrial</h3>
        <p style='color: #000000; text-align: justify; line-height: 1.6;'>
            El proyecto evidencia que las decisiones relacionadas con la localización, distribución de planta y diseño de operaciones 
            tienen un impacto directo sobre los costos, la productividad, el nivel de servicio y la competitividad empresarial. 
            La integración de herramientas de análisis, modelación matemática y simulación permitió desarrollar una propuesta técnicamente viable 
            para Café Artesanal CASAENZ, alineada con criterios de eficiencia operativa, sostenibilidad logística y crecimiento empresarial.
        </p>
    </div>
    
    <div class="kpi-card" style="border-left: 5px solid #D4A373;">
        <h3 style='color: #000000; margin-top:0;'>🚀 Viabilidad del Negocio y Soportes Futuros</h3>
        <p style='color: #000000; text-align: justify; line-height: 1.6;'>
            Finalmente, se concluye que la configuración propuesta para la planta y la red de suministro de Café Artesanal CASAENZ constituye una alternativa adecuada para 
            soportar el desarrollo y expansión del negocio, proporcionando una base sólida para futuras decisiones relacionadas con la capacidad productiva, 
            distribución logística y optimización de procesos. La aplicación de metodologías propias de la Ingeniería Industrial permitió transformar 
            información en decisiones estratégicas, demostrando la importancia de la planeación y el análisis técnico en el diseño de sistemas productivos modernos.
        </p>
    </div>
    """, unsafe_allow_html=True)
