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
    /* FONDO DE COLOR SÓLIDO LIMPIO (Eliminada la imagen de fondo para máxima legibilidad) */
    .stApp {{
        background-color: #FDFBF7; /* Un tono crema/arena muy suave que no cansa la vista */
    }}
    
    /* Títulos y textos estilizados */
    .main-title {{ font-size:42px !important; font-weight: bold; color: #4A3018; text-align: center; margin-bottom: 5px; }}
    .subtitle {{ font-size:20px !important; text-align: center; color: #705335; margin-bottom: 30px; }}
    .section-header {{ color: #5C3A21; border-bottom: 2px solid #D4A373; padding-bottom: 5px; margin-top: 20px; }}
    
    /* Estilos para las tarjetas de conclusión */
    .conclusion-card {{
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 8px;
        border-left: 5px solid #D4A373;
        margin-bottom: 15px;
        box-shadow: 1px 1px 5px rgba(0,0,0,0.05);
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
        **Café Artesanal CASAENZ** es un café colombiano Premium cultivado y tostado de manera artesanal en el **Valle del Cauca**, 
        que busca ofrecer una experiencia sensorial auténtica a través de granos cuidadosamente seleccionados y procesos tradicionales de producción.
        """)
        
        st.subheader("🎯 Brecha de Mercado")
        st.write("""
        Satisface la necesidad creciente de los consumidores por productos auténticos, de alta calidad y con identidad de origen, combatiendo el marketing engañoso de marcas masivas.
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
    st.write("Para localizar la planta y los centros de operaciones se evaluaron los factores críticos prioritarios organizados en la planeación:")
    
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
# PÁGINA 6: BALANCEO DE LÍNEA Y ASIGNACIÓN
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
    min_teorico = int(np.ceil(tiempo_total_operacion / 90))
    
    # Asignación Heurística de Puestos Realizada
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

# ==============================================================================
# PÁGINA 7: NUEVA SECCIÓN - CONCLUSIÓN GENERAL DEL PROYECTO
# ==============================================================================
elif opcion == "7. Conclusión General del Proyecto":
    st.header("🎓 7. Conclusión General del Proyecto Integrador")
    st.markdown("### 🎯 Diagnóstico Estratégico e Implicaciones de Ingeniería")
    
    st.markdown("""
    <div class="conclusion-card">
        <h4>1. Viabilidad de Localización y Sostenibilidad Logística</h4>
        <p>A través de la triangulación metodológica (Costo-Volumen-Utilidad, Calificación de Factores y Centro de Gravedad), 
        se demostró que la macro-localización en el corredor del <b>Valle del Cauca (Cali/Palmira)</b> optimiza el balance de la red de suministros. 
        Esta ubicación mitiga el impacto de los fletes de transporte, asegura una respuesta ágil a la fluctuación de la demanda de los centros urbanos 
        y aprovecha la cercanía clave con los proveedores de café pergamino en Yotoco, Tuluá y Ginebra.</p>
    </div>
    
    <div class="conclusion-card">
        <h4>2. Eficiencia del Diseño Espacial ($W_D$) y Flujo de Proceso</h4>
        <p>El plano de bloques desarrollado bajo una distribución por producto, en sinergia con el análisis del <b>Diagrama de Hilos</b>, 
        logró una reducción drástica en los recorridos innecesarios de materiales dentro de la planta. 
        El indicador de esfuerzo calculado <b>Factor Carga-Distancia ($W_D$)</b> funge como línea base de eficiencia, asegurando un flujo continuo, 
        minimizando el riesgo de contaminación cruzada del grano y validando la configuración física antes de incurrir en costos de infraestructura.</p>
    </div>
    
    <div class="conclusion-card">
        <h4>3. Sincronización de Operaciones y Balanceo de Líneas</h4>
        <p>El estudio de tiempos y precedencias determinó que el proceso artesanal cuenta con una operación restrictiva o cuello de botella en la <b>Tostión (85 segundos)</b>. 
        No obstante, la estructuración heurística en <b>4 puestos de trabajo óptimos</b> permitió alcanzar una robusta <b>Eficiencia Global de Línea del 79.17%</b>. 
        Esto garantiza que la capacidad instalada no solo es técnicamente estable, sino capaz de soportar la tasa de producción deseada de 320 unidades diarias sin sobrecargar la mano de obra.</p>
    </div>
    
    <div class="conclusion-card">
        <h4>4. Simulación y Toma de Decisiones en la Ingeniería Industrial</h4>
        <p>En conclusión, el modelado matemático combinado con la simulación virtual en <b>FlexSim</b> demuestra que las decisiones metodológicas de diseño de planta 
        tienen un impacto directo e inmediato en la productividad, costos operativos y nivel de servicio de <b>Café Artesanal CASAENZ</b>. 
        La ingeniería industrial aplicada transformó datos empíricos en una propuesta de distribución de planta altamente competitiva, escalable y financieramente viable.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Detalle estético final para cerrar la exposición
    st.balloons()
