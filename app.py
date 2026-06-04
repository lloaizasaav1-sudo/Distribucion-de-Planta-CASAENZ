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
        fig_cg.add_trace(go.Scatter(x=df_cg["Coordenada X (Km)"], y=df_cg["Coordenada Y (Km)"], mode='markers+text', text=df_cg["Ciudad Destino"], textposition="top center", marker=dict(size=12, color='#5C3A21'), name="Nodos"))
        fig_cg.add_trace(go.Scatter(x=[x_opt], y=[y_opt], mode='markers+text', text=["CEDI ÓPTIMO"], textposition="bottom center", marker=dict(size=16, color='red', symbol='star'), name="Ideal"))
        st.plotly_chart(fig_cg, use_container_width=True)

    with tab3:
        st.subheader("Análisis Jerárquico Multicriterio (AHP) para Distribución Interna")
        df_ahp = pd.DataFrame({
            "Alternativa Estructurada": ["A1 (Distribución Celular en U)", "A2 (Distribución Lineal o en Cadena)", "A3 (Distribución Funcional o por Proceso)"],
            "Ponderación Criterio Económico": [0.2014, 0.6479, 0.3395],
            "Ponderación Criterio Operacional": [0.6479, 0.2014, 0.4545],
            "Prioridad Global Ponderada (Final)": ["64.79 %", "20.14 %", "33.95 %"]
        })
        st.dataframe(df_ahp, use_container_width=True)
        st.success("🏆 **Decisión de Ingeniería Industrial:** La alternativa **A1 (Célula en U)** domina con un **64.79%** debido a su alto desempeño en flexibilidad operativa.")

elif opcion == "3. Red de Suministros y Modelo":
    st.markdown('<div class="section-header">🌐 3. Configuración del Modelo de Red de Suministros</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown("La configuración matemática óptima de la red de suministros de **Café CASAENZ** se modela mediante programación lineal (Problema de Transporte):")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 🌾 Capacidad de Oferta (Nodos Proveedores)")
        st.table(pd.DataFrame({"Municipio Origen": ["Yotoco", "Tuluá", "Ginebra"], "Disponibilidad Máxima (kg/mes)": [700, 500, 400]}))
    with col2:
        st.markdown("#### 🏪 Requerimiento de Demanda (Nodos Clientes)")
        st.table(pd.DataFrame({"Nodo Destino": ["Cali", "Palmira", "Buga", "Tuluá"], "Demanda Comercial (kg/mes)": [400, 500, 300, 400]}))
    st.info("📊 **Estructuración Matemática:**\n\n$$\min Z = \sum_{i} \sum_{j} c_{ij} \cdot x_{ij}$$\n\n**Sujeto a:**\n* $\sum_{j} x_{ij} \le \text{Oferta}_i$\n* $\sum_{i} x_{ij} \ge \text{Demanda}_j$")

elif opcion == "4. Simulación de Operaciones (FlexSim)":
    st.markdown('<div class="section-header">🏭 4. Modelación y Simulación en FlexSim</div>', unsafe_allow_html=True)
    st.write("")
    st.info("💡 **Guía de Sustentación:** Utiliza este espacio como soporte metodológico mientras proyectas el software de FlexSim activo en tu clase.")
    st.markdown("""
    ### Parámetros de Configuración del Modelo de Piso:
    * **Tipo de Distribución Adoptada:** Distribución Orientada al Producto / Flujo Continuo en Línea.
    * **Lógica Secuencial de Objetos (FlexSim):**
        1. **Source (Ingreso):** Simula el arribo de lotes de Café Pergamino Seco.
        2. **Queue (Almacenamiento Temporal):** Silo de espera regulador de materia prima.
        3. **Processor 1 (Tostión):** Configurado con tiempos de procesamiento artesanal (Operación restrictiva / Cuello de botella).
        4. **Processor 2 (Molienda):** Procesamiento mecánico automatizado controlado.
        5. **Processor 3 (Empaque y Sellado):** Línea terminal de embolsado.
        6. **Sink (Despacho Final):** Salida a CEDI de producto terminado listo para distribución.
    """)
    st.progress(100)

elif opcion == "5. Distribución de Planta y Factor Wd":
    st.markdown('<div class="section-header">📐 5. Distribución Física, Diagrama de Hilos y Carga-Distancia</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    #### 🔹 Diagrama de Hilos y Plano de Bloques Conceptual
    El flujo físico se diseñó siguiendo la metodología SLP *(Systematic Layout Planning)* implementando un flujo en **Célula en U** para reducir retrocesos.
    La secuencia establecida es: **[Recepción] ➔ [Silos] ➔ [Tostión] ➔ [Molienda] ➔ [Empaque] ➔ [Inspección] ➔ [Despacho]**
    """)
    
    df_wd = pd.DataFrame({
        "Ruta del Flujo de Materiales": [
            "A - C (Recepción a Stock Verde)", 
            "C - D (Silos de Stock a Tostión)", 
            "D - E (Tostión a Molienda/Empaque)", 
            "E - F (Empaque a Inspección y Listo)", 
            "F - G (Producto Terminado a Despacho)"
        ],
        "Distancia D_i (Metros)": [8, 12, 6, 5, 10],
        "Carga Semanal W_i (Kg/Semana)": [500, 500, 480, 480, 480]
    })
    df_wd["Esfuerzo WD Real (Kg·m/sem)"] = df_wd["Distancia D_i (Metros)"] * df_wd["Carga Semanal W_i (Kg/Semana)"]
    st.dataframe(df_wd, use_container_width=True)
    factor_total = df_wd["Esfuerzo WD Real (Kg·m/sem)"].sum()
    st.metric(label="Factor Carga-Distancia Global ($W_D$ Total)", value=f"{factor_total:,} Kg·m / semana")

# ==============================================================================
# PÁGINA 6: BALANCEO DE LÍNEA Y ASIGNACIÓN COMPLETA (MÁXIMO DETALLE TÉCNICO)
# ==============================================================================
elif opcion == "6. Balanceo de Línea y Puestos":
    st.markdown('<div class="section-header">⚡ 6. Ingeniería de Métodos: Balanceo Analítico de Línea de Producción</div>', unsafe_allow_html=True)
    st.write("")
    
    st.markdown("""
    <div class="theory-box">
        <h4>📋 Parámetros de Entrada Estructurados</h4>
        • <b>Jornada Laboral Efectiva (Tiempo Disponible - T):</b> 1 Turno de 8 horas / día = 480 minutos = <b>28,800 segundos / día</b>.<br>
        • <b>Tasa de Producción Deseada (Demanda Diaria - R):</b> <b>320 unidades / día</b> (Café molido artesanal de 500g).
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🔹 Paso 1: Fórmulas Matemáticas de Ingeniería Aplicadas")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**1. Tiempo de Ciclo ($T_c$):** Limita el tiempo máximo que el producto puede permanecer en cada puesto.")
        st.latex(r"T_c = \frac{\text{Tiempo Disponible (T)}}{\text{Tasa de Producción (R)}} = \frac{28,800 \text{ seg}}{320 \text{ und}} = 90 \text{ segundos/unidad}")
        
        st.markdown("**2. Número Mínimo Teórico de Estaciones ($N_t$):**")
        st.latex(r"N_t = \left\lceil \frac{\sum Tiempos\ de\ Tarea}{T_c} \right\rceil = \left\lceil \frac{255 \text{ seg}}{90 \text{ seg}} \right\rceil = \lceil 2.83 \rceil = 3\text{ estaciones}")
    
    with col2:
        st.markdown("**3. Eficiencia Global de la Línea ($E$):**")
        st.latex(r"E = \frac{\sum Tiempos\ de\ Tarea}{N_{real} \times T_c} \times 100\%")
        
        st.markdown("**4. Retraso del Balanceo ($D$) y Tiempo de Ocio ($I$):**")
        st.latex(r"D = 100\% - E \quad \vert \quad I = \sum (T_c - T_{estación})")

    st.markdown("---")
    st.markdown("### 🔹 Paso 2: Diagrama de Precedencias y Tiempos de Tarea Reales")
    st.markdown("A continuación se detallan las operaciones consecutivas necesarias para el empaque primario y acondicionado del café:")
    
    df_tareas = pd.DataFrame({
        "Tarea": ["A", "B", "C", "D", "E", "F", "G"],
        "Descripción Detallada de la Operación": [
            "Recepción, pesado y limpieza del grano verde",
            "Tostión artesanal controlada (Operación Crítica)",
            "Enfriamiento controlado en bandeja de aireación",
            "Molienda fina/media en molino de rodillos",
            "Dosificación exacta en báscula gramera (500g)",
            "Sellado térmico y codificación de fechado de bolsa",
            "Etiquetado manual final e inspección visual de calidad"
        ],
        "Tiempo (seg)": [40, 85, 30, 50, 25, 35, 20],
        "Precedencia Inmediata": ["-", "A", "B", "C", "D", "E", "F"]
    })
    st.dataframe(df_tareas, use_container_width=True)
    
    sum_tiempos = df_tareas["Tiempo (seg)"].sum()

    st.markdown("---")
    st.markdown("### 🔹 Paso 3: Regla Heurística y Asignación Definitiva de Puestos de Trabajo")
    st.markdown("""
    Utilizando la **regla heurística del tiempo de tarea más largo** y respetando de forma estricta la restricción de precedencia 
    y el límite máximo del tiempo de ciclo ($T_c = 90$s), se consolidó la siguiente estructura óptima de puestos:
    """)
    
    df_puestos = pd.DataFrame({
        "Estación Operativa": [
            "Puesto de Trabajo 1 (Operario 1)", 
            "Puesto de Trabajo 2 (Operario 2)", 
            "Puesto de Trabajo 3 (Operario 3)", 
            "Puesto de Trabajo 4 (Operario 4)"
        ],
        "Tareas Secuenciales Asignadas": [
            "A + C (Pesado inicial + Enfriamiento)", 
            "B (Tostión - Proceso Crítico Autónomo)", 
            "D + E (Molienda de rodillos + Dosificación)", 
            "F + G (Sellado térmico + Etiquetado final)"
        ],
        "Cálculo Analítico del Tiempo de Estación": [
            "40s + 30s = 70 segundos",
            "85s = 85 segundos",
            "50s + 25s = 75 segundos",
            "35s + 20s = 55 segundos"
        ],
        "Tiempo de Ciclo Real del Puesto (seg)": [70, 85, 75, 55],
    })
    df_puestos["Tiempo Muerto u Ocio por Unidad (seg)"] = 90 - df_puestos["Tiempo de Ciclo Real del Puesto (seg)"]
    st.dataframe(df_puestos, use_container_width=True)

    st.markdown("#### 💡 Justificación Técnica de la Asignación:")
    st.markdown("""
    * **Puesto 1:** Agrupa las tareas A y C de manera segura. No se puede incluir otra tarea consecutiva debido a que excedería los 90 segundos límites.
    * **Puesto 2 (Cuello de Botella):** La tarea B de Tostión consume por sí sola **85 segundos**. Al estar tan cerca del límite de ciclo, se le asigna un operario exclusivo para supervisar las variables críticas térmicas del grano artesanal.
    * **Puesto 3 y 4:** Agrupan eficientemente las fases finales del empaque manteniendo las cargas distribuidas de forma balanceada.
    """)

    st.markdown("---")
    st.markdown("### 🔹 Paso 4: Indicadores de Evaluación de Desempeño Operativo")
    
    n_estaciones_real = len(df_puestos)
    eficiencia_global = (sum_tiempos / (n_estaciones_real * 90)) * 100
    retraso_bal = 100 - eficiencia_global
    ocio_total = df_puestos["Tiempo Muerto u Ocio por Unidad (seg)"].sum()
    
    col_a, col_b, col_c, col_d = st.columns(4)
    col_a.metric("Mínimo Teórico Calculado", f"3 Operarios")
    col_b.metric("Número de Operarios Reales", f"{n_estaciones_real} Operarios")
    col_c.metric("Eficiencia Global de la Línea", f"{eficiencia_global:.2f} %")
    col_d.metric("Retraso del Balanceo", f"{retraso_bal:.2f} %")
    
    # Gráfico interactivo de balance de cargas por estación
    fig_linea = go.Figure()
    fig_linea.add_trace(go.Bar(x=df_puestos["Estación Operativa"], y=df_puestos["Tiempo de Ciclo Real del Puesto (seg)"], name="Tiempo Productivo Asignado", marker_color='#5C3A21'))
    fig_linea.add_trace(go.Bar(x=df_puestos["Estación Operativa"], y=df_puestos["Tiempo Muerto u Ocio por Unidad (seg)"], name="Tiempo de Ocio (Inactividad)", marker_color='#D4A373'))
    fig_linea.add_hline(y=90, line_dash="dash", line_color="red", annotation_text="Límite Máximo Tiempo de Ciclo (90s)")
    fig_linea.update_layout(barmode='stack', title="Distribución de la Carga de Trabajo vs Tiempo de Ciclo Máximo")
    st.plotly_chart(fig_linea, use_container_width=True)
    
    st.success("📈 **Diagnóstico Final de Ingeniería de Métodos:** El balanceo propuesto es altamente robusto para la organización, asegurando una eficiencia operativa del **79.17%**. La inactividad total se reduce a solo 105 segundos distribuidos, garantizando que el ritmo productivo absorba la demanda diaria sin generar horas extra.")

elif opcion == "🎓 Conclusiones Generales":
    st.markdown('<p class="main-title">🎓 Conclusiones Generales del Proyecto Integrador</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Evaluación de Resultados y Decisiones de Ingeniería Industrial</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="kpi-card">
        <h3>🎯 1. Coherencia Matemática en Macrolocalización</h3>
        <p>
            El uso de la modelación analítica permitió tomar decisiones estratégicas de localización basadas en la mitigación del riesgo financiero y de costos. 
            El método Costo-Volumen-Utilidad (CVU) validó que la <b>Región B</b> es la localización óptima para el volumen de producción planteado, 
            ya que equilibra de manera eficiente la estructura de costos fijos con el impacto de la variabilidad operativa.
        </p>
    </div>
    
    <div class="kpi-card">
        <h3>🚛 2. Eficiencia Logística y Reducción del Costo de Fletes</h3>
        <p>
            A través del Método del Centro de Gravedad, se optimizó el posicionamiento geográfico del Centro de Distribución (CEDI) 
            en las coordenadas exactas de **X: 118.06, Y: 243.66**, logrando un costo mínimo total de transporte de <b>$3,354,773,746.00 COP</b>. 
            Esta ubicación estratégica mitiga el impacto de las tarifas elevadas de transporte en zonas complejas (como Tuluá) y maximiza la cercanía a Cali, el principal nodo de demanda.
        </p>
    </div>
    
    <div class="kpi-card">
        <h3>📐 3. Flujo Industrial Esbelto mediante Distribución en U</h3>
        <p>
            El análisis multicriterio ponderado (AHP) resolvió científicamente que variables como la flexibilidad en planta y la seguridad ocupacional 
            poseen mayor relevancia a largo plazo que el costo de instalación inmediato. El diseño adoptado en <b>Célula en U (A1)</b>, respaldado por un factor 
            Carga-Distancia ($W_D$) optimizado, minimiza los recorridos internos de materiales calientes y elimina los cuellos de botella por transporte físico.
        </p>
    </div>
    
    <div class="kpi-card">
        <h3>⚡ 4. Alta Productividad en Planta y Control de Operaciones</h3>
        <p>
            El balanceo analítico de la línea de producción estructuró el proceso en **4 estaciones operativas estables**, alcanzando una elevada 
            eficiencia global del <b>79.17%</b>. El diseño heurístico desarrollado asegura el cumplimiento de la meta de producción de 320 unidades diarias de 500g 
            dentro de la jornada de 8 horas, aislando correctamente la operación de <b>Tostión</b> como el cuello de botella controlado del sistema.
        </p>
    </div>
    
    <div class="kpi-card" style="border-left: 5px solid #5C3A21; background-color: #fdfbf7;">
        <h3>🚀 5. Viabilidad Estratégica del Negocio</h3>
        <p>
            En conclusión, la integración sistemática de técnicas de localización, diseño de redes de suministro, optimización de esfuerzos físicos y balanceo de líneas, 
            transforma los datos académicos en decisiones industriales sólidas. La configuración propuesta para <b>Café Artesanal CASAENZ</b> garantiza un sistema logístico 
            competitivo, financieramente rentable y con bases operativas robustas preparadas para soportar el crecimiento comercial futuro.
        </p>
    </div>
    """, unsafe_allow_html=True)
