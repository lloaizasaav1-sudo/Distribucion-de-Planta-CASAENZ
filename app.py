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

# Estilos personalizados para mejorar la estética
st.markdown("""
    <style>
    .main-title { font-size:42px !important; font-weight: bold; color: #4A3018; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:20px !important; text-align: center; color: #705335; margin-bottom: 30px; }
    .section-header { color: #5C3A21; border-bottom: 2px solid #D4A373; padding-bottom: 5px; }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# SIDEBAR / NAVEGACIÓN
# ==============================================================================
with st.sidebar:
    st.image("https://raw.githubusercontent.com/AnhellO/Capas-Geoserver/main/coffee_logo_placeholder.png", width=150, caption="Café Artesanal CASAENZ") # Placeholder si no carga la imagen
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
            "6. Balanceo de Línea y Asignación de Puestos"
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
        st.write("Fórmula utilizada:  $$CT = CF + (CV \cdot Q)$$")
        
        # Datos del problema
        df_cvu = pd.DataFrame({
            "Ciudad": ["Cali", "Palmira", "Buga"],
            "Costos Fijos ($)": [4500000, 3200000, 2800000],
            "Costo Variable Unitario ($)": [3500, 4200, 4800]
        })
        
        st.dataframe(df_cvu, use_container_width=True)
        
        q_slider = st.slider("Ajusta la cantidad de producción mensual (Q):", 1000, 15000, 10000, step=500)
        
        # Cálculos dinámicos
        df_cvu["Costo Total ($)"] = df_cvu["Costos Fijos ($)"] + (df_cvu["Costo Variable Unitario ($)"] * q_slider)
        st.write(f"### Resultados para Q = {q_slider:,} unidades")
        st.dataframe(df_cvu, use_container_width=True)
        
        # Gráfico dinámico de líneas de costo
        q_range = np.linspace(0, 15000, 100)
        fig_cvu = go.Figure()
        for idx, row in df_cvu.iterrows():
            fig_cvu.add_trace(go.Scatter(x=q_range, y=row["Costos Fijos ($)"] + row["Costo Variable Unitario ($)"] * q_range, mode='lines', name=row["Ciudad"]))
        fig_cvu.add_vline(x=q_slider, line_dash="dash", line_color="red", annotation_text=f"Q actual")
        fig_cvu.update_layout(title="Curvas de Costo Total por Localización", xaxis_title="Volumen (Q)", yaxis_title="Costo Total ($)")
        st.plotly_chart(fig_cvu, use_container_width=True)
        st.success("💡 **Conclusión CVU:** Cali representa la alternativa más económica a altos volúmenes gracias a su bajo costo variable unitario.")

    # 2.2 Factor Rating
    with tab2:
        st.subheader("🎯 Método de Calificación de Factores (Factor Rating)")
        
        # Matriz de datos originales
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
        
        # Resultados ponderados
        score_cali = sum(w*c for w, c in zip(peso, calif_cali))
        score_palmira = sum(w*c for w, c in zip(peso, calif_palmira))
        score_buga = sum(w*c for w, c in zip(peso, calif_buga))
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Puntuación Cali", f"{score_cali:.2f}", delta="Ganador")
        col2.metric("Puntuación Palmira", f"{score_palmira:.2f}")
        col3.metric("Puntuación Buga", f"{score_buga:.2f}")
        
        fig_fr = px.bar(x=["Cali", "Palmira", "Buga"], y=[score_cali, score_palmira, score_buga], labels={'x': 'Ciudad', 'y': 'Puntuación Ponderada'}, title="Comparación de Puntajes de Factores")
        st.plotly_chart(fig_fr, use_container_width=True)

    # 2.3 Centro de Gravedad
    with tab3:
        st.subheader("📍 Método del Centro de Gravedad")
        st.write("Determina las coordenadas ideales óptimas en función de la demanda ($V_i$) y costos de fletes ($f_i$).")
        
        df_cg = pd.DataFrame({
            "Ciudad Destino": ["Cali", "Palmira", "Buga"],
            "Coordenada X": [100, 115, 120],
            "Coordenada Y": [200, 215, 280],
            "Demanda Vi (kg)": [5000, 4100, 3200],
            "Costo fi ($)": [3500, 2800, 2100]
        })
        st.dataframe(df_cg, use_container_width=True)
        
        # Coordenadas calculadas fijas del informe
        x_opt = 108.59
        y_opt = 219.83
        
        st.metric("Coordenada Óptima Calculada", f"X: {x_opt}, Y: {y_opt}")
        
        # Gráfico de dispersión de ubicaciones
        fig_cg = px.scatter(df_cg, x="Coordenada X", y="Coordenada Y", text="Ciudad Destino", size="Demanda Vi (kg)", title="Mapa de Distribución del Centro de Gravedad")
        fig_cg.add_trace(go.Scatter(x=[x_opt], y=[y_opt], mode='markers+text', text=["📍 CENTRO GRAVEDAD ÓPTIMO"], marker=dict(color='red', size=15), name="Punto Óptimo"))
        st.plotly_chart(fig_cg, use_container_width=True)
        st.info("💡 El punto óptimo se localiza estratégicamente en el corredor vial entre **Cali y Palmira**.")

# ==============================================================================
# PÁGINA 3: RED DE SUMINISTROS
# ==============================================================================
elif opcion == "3. Red de Suministros y Modelo Matemático":
    st.header("🌐 3. Diseño de la Red de Suministros")
    
    st.write("Estructura logística balanceada de 3 eslabones: **Proveedores → Planta/CEDI → Clientes Finales**.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🌾 Oferta de Proveedores")
        df_oferta = pd.DataFrame({"Proveedor": ["Yotoco", "Tuluá", "Ginebra"], "Oferta (kg)": [700, 500, 400]})
        st.table(df_oferta)
        st.markdown("**Oferta Total:** 1,600 kg")
        
    with col2:
        st.markdown("### 🏪 Demanda del Mercado")
        df_demanda = pd.DataFrame({"Destino": ["Cali", "Palmira", "Buga", "Tuluá"], "Demanda (kg)": [400, 500, 300, 400]})
        st.table(df_demanda)
        st.markdown("**Demanda Total:** 1,600 kg (Modelo perfectamente Balanceado)")

    st.markdown("---")
    st.subheader("📋 Matriz de Costos Unitarios de Transporte ($c_{ij}$)")
    df_costos = pd.DataFrame({
        "Cali": [12, 14, 13],
        "Palmira": [10, 12, 11],
        "Buga": [15, 10, 12],
        "Tuluá": [18, 8, 16]
    }, index=["Yotoco (Origen)", "Tuluá (Origen)", "Ginebra (Origen)"])
    st.dataframe(df_costos, use_container_width=True)
    
    st.markdown("### ⚙️ Formulación Matemática de Programación Lineal")
    st.latex(r"\min Z = \sum_{i} \sum_{j} c_{ij} X_{ij}")
    st.latex(r"\text{Sujeto a: } \sum_{j} X_{ij} \le \text{Oferta}_i \quad \forall i")
    st.latex(r"\text{Sujeto a: } \sum_{i} X_{ij} = \text{Demanda}_j \quad \forall j")
    st.latex(r"X_{ij} \ge 0")

# ==============================================================================
# PÁGINA 4: SIMULACIÓN EN FLEXSIM
# ==============================================================================
elif opcion == "4. Simulación en FlexSim":
    st.header("🏭 4. Modelación y Simulación en FlexSim")
    
    st.warning("⚠️ **Nota de Presentación:** Esta sección sirve como el marco teórico y la guía visual de soporte para cuando abras tu software **FlexSim** en vivo ante tus evaluadores.")
    
    st.markdown("""
    ### 🪵 Configuración del Layout de Operaciones en Piso
    La simulación en FlexSim valida en un modelo virtual tridimensional el flujo logístico propuesto. La planta utiliza una **Distribución por Producto (Línea de Producción Flujo Continuo)** para maximizar la velocidad operativa de procesamiento de café artesanal.
    
    #### ⚙️ Elementos modelados en el Layout:
    1. **Source (Entradas):** Arribo de Café Verde (Sacos) y entrada de material de Empaque secundario (Bolsas).
    2. **Queues (Almacenamientos):** Buffers temporales de materia prima para mitigar cuellos de botella.
    3. **Processors (Estaciones de Trabajo):** Tostión, Molienda, Dosificación y Sellado Térmico.
    4. **Sink (Despacho):** Almacén final listo para la carga en camiones de distribución regional.
    """)
    
    # Simulación visual de barras de flujo
    st.subheader("🔄 Secuencia Lógica del Proceso Automatizado")
    pasos = ["Recepción", "Almacenamiento", "Tostión/Molienda", "Empaque", "Producto Terminado", "Despacho"]
    st.progress(100)
    st.write(" 👉 ".join([f"**[{p}]**" for p in pasos]))

# ==============================================================================
# PÁGINA 5: DISTRIBUCIÓN DE PLANTA
# ==============================================================================
elif opcion == "5. Distribución de Planta (Diagrama de Hilos, Bloques y WD)":
    st.header("📐 5. Diseño Espacial y Factor Carga-Distancia ($W_D$)")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("🏢 Plano de Bloques (Distribución de Áreas)")
        df_bloques = pd.DataFrame({
            "Código": ["A", "B", "C", "D", "E", "F", "G"],
            "Área Funcional": ["Recepción de Café Verde", "Recepción de Empaques (Bolsas)", "Almacenamiento Materia Prima", "Proceso de Tostión y Molienda", "Empaque y Dosificación", "Almacén de Producto Terminado", "Despacho"]
        })
        st.table(df_bloques)
        
        st.markdown("""
        **Rutas del Diagrama de Hilos:**
        * **Flujo 1 (Café):** A ➔ C ➔ D ➔ E ➔ F ➔ G
        * **Flujo 2 (Bolsas):** B ➔ E
        """)

    with col2:
        st.subheader("🏋️ Factor Carga-Distancia Semanal ($W_D$)")
        st.write("Fórmula: $$W_D = \sum (W_i \cdot D_i)$$")
        
        df_wd = pd.DataFrame({
            "Ruta (Flujo)": ["A - C", "C - D", "D - E", "E - F", "F - G", "B - E"],
            "Distancia D_i (m)": [8, 12, 6, 5, 10, 15],
            "Carga W_i (kg/sem)": [500, 500, 480, 480, 480, 200]
        })
        df_wd["Esfuerzo WD (kg·m)"] = df_wd["Distancia D_i (m)"] * df_wd["Carga W_i (kg/sem)"]
        st.dataframe(df_wd, use_container_width=True)
        
        total_wd = df_wd["Esfuerzo WD (kg·m)"].sum()
        st.metric("Factor WD Total Semanal", f"{total_wd:,} kg·m/semana", help="Un valor menor indica menores costos de transporte interno.")

# ==============================================================================
# PÁGINA 6: BALANCEO DE LÍNEA (COMPLETADA TÉCNICAMENTE)
# ==============================================================================
elif opcion == "6. Balanceo de Línea and Asignación de Puestos":
    st.header("⚡ 6. Balanceo de Líneas y Asignación de Puestos")
    st.write("Para una tasa requerida de **320 paquetes/día** en una jornada de **8 horas**, el Tiempo de Ciclo ($T_C$) límite es de **90 segundos/unidad**.")
    
    # Tabla de tiempos de actividades
    actividades = {
        "A": ["Recepción y selección", 30, "-"],
        "B": ["Tostión", 90, "A"],
        "C": ["Enfriamiento", 60, "B"],
        "D": ["Molienda", 45, "C"],
        "E": ["Dosificación", 40, "D"],
        "F": ["Empaque", 50, "E"],
        "G": ["Sellado", 35, "F"],
        "H": ["Etiquetado", 25, "G"]
    }
    
    df_act = pd.DataFrame.from_dict(actividades, orient='index', columns=["Descripción", "Tiempo (seg)", "Precedencia"])
    st.subheader("⏱️ Tiempos Estándar de Operación")
    st.dataframe(df_act, use_container_width=True)

    st.markdown("---")
    st.subheader("🛠️ Asignación Definitiva de Puestos de Trabajo (Línea de Producción)")
    st.write("Dado que algunas operaciones críticas individuales (como Tostión = 90 seg) saturan el ciclo por sí solas, la conformación óptima y matemática de las estaciones se estructuró de la siguiente forma:")

    # Estructura completada y optimizada técnicamente
    estaciones_datos = [
        {"Estación": "Estación 1", "Actividades Incluidas": "A (Recepción y Selección)", "Tiempo Estación (seg)": 30, "Tiempo Ocioso (seg)": 60},
        {"Estación": "Estación 2", "Actividades Incluidas": "B (Tostión)", "Tiempo Estación (seg)": 90, "Tiempo Ocioso (seg)": 0},
        {"Estación": "Estación 3", "Actividades Incluidas": "C (Enfriamiento)", "Tiempo Estación (seg)": 60, "Tiempo Ocioso (seg)": 30},
        {"Estación": "Estación 4", "Actividades Incluidas": "D + E (Molienda + Dosificación)", "Tiempo Estación (seg)": 85, "Tiempo Ocioso (seg)": 5},
        {"Estación": "Estación 5", "Actividades Incluidas": "F (Empaque)", "Tiempo Estación (seg)": 50, "Tiempo Ocioso (seg)": 40},
        {"Estación": "Estación 6", "Actividades Incluidas": "G + H (Sellado + Etiquetado)", "Tiempo Estación (seg)": 60, "Tiempo Ocioso (seg)": 30},
    ]
    df_estaciones = pd.DataFrame(estaciones_datos)
    st.dataframe(df_estaciones, use_container_width=True)

    # Gráfico del Balanceo vs el Tiempo de Ciclo Objetivo
    fig_bal = go.Figure()
    fig_bal.add_trace(go.Bar(x=df_estaciones["Estación"], y=df_estaciones["Tiempo Estación (seg)"], name="Tiempo de la Estación", marker_color='#8B5A2B'))
    fig_bal.add_hline(y=90, line_dash="dash", line_color="red", annotation_text="Tiempo de Ciclo Máximo (90s)")
    fig_bal.update_layout(title="Carga de Trabajo por Estación vs Tiempo de Ciclo Límite", yaxis_title="Segundos")
    st.plotly_chart(fig_bal, use_container_width=True)

    # Métricas de Desempeño
    col1, col2, col3 = st.columns(3)
    col1.metric("Eficiencia Total de la Línea", "69.44 %")
    col2.metric("Retraso del Balanceo (Balance Delay)", "30.56 %")
    col3.metric("Tiempo Muerto Total por Ciclo", "165 segundos")

    st.info("💡 **Análisis de Ingeniería:** La **Estación 2 (Tostión)** es la operación cuello de botella de la planta. Para incrementar la eficiencia global por encima del 69.44 %, se sugiere en el futuro automatizar el proceso de enfriamiento o duplicar la maquinaria de tostión para trabajar en paralelo.")
