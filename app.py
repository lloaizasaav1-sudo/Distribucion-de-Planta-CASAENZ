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
    # Intenta cargar el archivo local logo.png si existe en la misma carpeta
    try:
        st.image("logo.png", caption="☕ Café Artesanal CASAENZ", use_container_width=True)
    except:
        st.warning("⚠️ No se encontró el archivo 'logo.png' en la carpeta. Verifica el nombre.")
        
    st.markdown("---")
    st.markdown("### 📋 Secciones del Proyecto")
    opcion = st.radio(
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
# PÁGINA 0: INTRODUCCIÓN Y CONCEPTO
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

# ==============================================================================
# PÁGINA 1: IDENTIFICACIÓN DE FACTORES CRÍTICOS
# ==============================================================================
elif opcion == "1. Factores Críticos de Localización":
    st.markdown('<div class="section-header">📌 1. Factores Críticos de Localización de Planta y Centros</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    Para el diseño de la red logística de **Café CASAENZ**, se determinaron **6 Factores Críticos de Localización (FCL)**, 
    esenciales para asegurar la viabilidad comercial y la reducción de costos operativos en los centros de operaciones:
    """)
    
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

# ==============================================================================
# PÁGINA 2: TÉCNICAS DE LOCALIZACIÓN (TUS EJERCICIOS REALES)
# ==============================================================================
elif opcion == "2. Técnicas de Localización Matemática":
    st.markdown('<div class="section-header">🧮 2. Modelación y Técnicas de Localización Aplicadas</div>', unsafe_allow_html=True)
    st.write("")
    
    tab1, tab2, tab3 = st.tabs(["📊 Punto de Equilibrio (CVU)", "📍 Centro de Gravedad (CEDI)", "🏆 Ponderación Multicriterio (AHP)"])
    
    with tab1:
        st.subheader("Análisis de Costo-Volumen-Utilidad (CVU) para Expansión de Capacidad")
        st.markdown("""
        Este método evalúa los factores económicos para identificar la localización de menor costo total en función del volumen de producción anual (Q).
        Los datos del ejercicio corresponden a tres regiones candidatas:
        """)
        
        df_cvu = pd.DataFrame({
            "Ubicación": ["Región A", "Región B", "Región C"],
            "Costo Fijo Anual (CF)": [100000, 200000, 350000],
            "Costo Variable Unitario (cv)": [30, 20, 12]
        })
        st.dataframe(df_cvu, use_container_width=True)
        
        q_slider = st.slider("Modifica la cantidad de producción anual proyectada (Q):", 0, 25000, 15000, step=500)
        
        # Cálculos económicos dinámicos
        df_cvu["Costo Total ($)"] = df_cvu["Costo Fijo Anual (CF)"] + (df_cvu["Costo Variable Unitario (cv)"] * q_slider)
        
        st.write(f"### Resultados de Costo Total para Q = {q_slider:,} unidades/año")
        st.dataframe(df_cvu, use_container_width=True)
        
        # Graficar curvas matemáticas
        q_range = np.linspace(0, 25000, 100)
        fig_cvu = go.Figure()
        fig_cvu.add_trace(go.Scatter(x=q_range, y=100000 + 30 * q_range, mode='lines', name='Región A (CF:100k, cv:30)', line=dict(color='#8B5A2B')))
        fig_cvu.add_trace(go.Scatter(x=q_range, y=200000 + 20 * q_range, mode='lines', name='Región B (CF:200k, cv:20)', line=dict(color='#D4A373')))
        fig_cvu.add_trace(go.Scatter(x=q_range, y=350000 + 12 * q_range, mode='lines', name='Región C (CF:350k, cv:12)', line=dict(color='#5C3A21')))
        fig_cvu.add_vline(x=q_slider, line_dash="dash", line_color="red", annotation_text=f"Q evaluado")
        
        fig_cvu.update_layout(xaxis_title="Volumen Anual (Q)", yaxis_title="Costo Total ($)", legend_title="Alternativas")
        st.plotly_chart(fig_cvu, use_container_width=True)
        
        st.info("💡 **Análisis de Indiferencia de Ingeniería:** Para volúmenes menores a 10,000 unidades la Región A es óptima. Entre 10,000 y 18,750 unidades, la **Región B** es la más económica. Para producciones masivas superiores a 18,750 unidades, la Región C minimiza los costos globales.")

    with tab2:
        st.subheader("Optimización de Ubicación de CEDI mediante Centro de Gravedad")
        st.markdown("Busca la localización óptima minimizando los costos de transporte combinando coordenadas geográficas ($X_i, Y_i$), volumen de demanda ($V_i$) y tarifas de flete ($f_i$).")
        
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
        fig_cg.add_trace(go.Scatter(x=df_cg["Coordenada X (Km)"], y=df_cg["Coordenada Y (Km)"], mode='markers+text', text=df_cg["Ciudad Destino"], textposition="top center", marker=dict(size=12, color='#5C3A21'), name="Nodos de Demanda"))
        fig_cg.add_trace(go.Scatter(x=[x_opt], y=[y_opt], mode='markers+text', text=["CEDI ÓPTIMO"], textposition="bottom center", marker=dict(size=16, color='red', symbol='star'), name="Localización Ideal"))
        fig_cg.update_layout(xaxis_title="Eje Coordenadas X (Km)", yaxis_title="Eje Coordenadas Y (Km)")
        st.plotly_chart(fig_cg, use_container_width=True)

    with tab3:
        st.subheader("Análisis Jerárquico Multicriterio (AHP) para Distribución Interna")
        st.markdown("Basado en tus matrices normalizadas de ponderación (Costo MP, Flexibilidad Operativa y Seguridad), los resultados globales consolidados determinan el mejor ordenamiento estructural:")
        
        df_ahp = pd.DataFrame({
            "Alternativa Estructurada": ["A1 (Distribución Celular en U)", "A2 (Distribución Lineal o en Cadena)", "A3 (Distribución Funcional o por Proceso)"],
            "Ponderación Criterio Económico": [0.2014, 0.6479, 0.3395],
            "Ponderación Criterio Operacional": [0.6479, 0.2014, 0.4545],
            "Prioridad Global Ponderada (Final)": ["64.79 %", "20.14 %", "33.95 %"]
        })
        st.dataframe(df_ahp, use_container_width=True)
        st.success("🏆 **Decisión de Ingeniería Industrial:** La alternativa **A1 (Célula en U)** domina con un **64.79%** de prioridad general debido a su alto desempeño en flexibilidad frente a variaciones de demanda y óptima ergonomía de seguridad para el operario.")

# ==============================================================================
# PÁGINA 3: RED DE SUMINISTROS
# ==============================================================================
elif opcion == "3. Red de Suministros y Modelo":
    st.markdown('<div class="section-header">🌐 3. Configuración del Modelo de Red de Suministros</div>', unsafe_allow_html=True)
    st.write("")
    
    st.markdown("""
    La configuración matemática óptima de la red de suministros de **Café CASAENZ** se modela mediante programación lineal (Problema de Transporte), 
    cuyo objetivo es minimizar el costo global de distribución de materias primas asegurando las restricciones de capacidad de oferta y requerimientos de demanda.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 🌾 Capacidad de Oferta (Nodos Proveedores)")
        st.table(pd.DataFrame({"Municipio Origen": ["Yotoco", "Tuluá", "Ginebra"], "Disponibilidad Máxima (kg/mes)": [700, 500, 400]}))
    with col2:
        st.markdown("#### 🏪 Requerimiento de Demanda (Nodos Clientes)")
        st.table(pd.DataFrame({"Nodo Destino": ["Cali", "Palmira", "Buga", "Tuluá"], "Demanda Comercial (kg/mes)": [400, 500, 300, 400]}))
        
    st.info("📊 **Estructuración Matemática del Modelo:**\n\n"
            "$$\min Z = \sum_{i} \sum_{j} c_{ij} \cdot x_{ij}$$\n\n"
            "**Sujeto a:**\n"
            "* $\sum_{j} x_{ij} \le \text{Oferta}_i$ \quad (Restricción de origen para cada proveedor)\n"
            "* $\sum_{i} x_{ij} \ge \text{Demanda}_j$ \quad (Restricción de cumplimiento de mercado)")

# ==============================================================================
# PÁGINA 4: SIMULACIÓN EN FLEXSIM
# ==============================================================================
elif opcion == "4. Simulación de Operaciones (FlexSim)":
    st.markdown('<div class="section-header">🏭 4. Modelación y Simulación en FlexSim</div>', unsafe_allow_html=True)
    st.write("")
    
    st.info("💡 **Guía de Sustentación:** Utiliza este espacio como soporte metodológico conceptual en la pantalla mientras proyectas el software de FlexSim activo en tu clase.")
    
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

# ==============================================================================
# PÁGINA 5: DIAGRAMA DE HILOS, PLANO DE BLOQUES Y FACTOR WD
# ==============================================================================
elif opcion == "5. Distribución de Planta y Factor Wd":
    st.markdown('<div class="section-header">📐 5. Distribución Física, Diagrama de Hilos y Carga-Distancia</div>', unsafe_allow_html=True)
    st.write("")
    
    st.markdown("""
    #### 🔹 Diagrama de Hilos y Plano de Bloques Conceptual
    El flujo físico se diseñó siguiendo la metodología SLP *(Systematic Layout Planning)* implementando un flujo en **Célula en U** para reducir retrocesos. 
    La secuencia establecida entre las áreas funcionales de la planta es la siguiente:
    
    **[Recepción y Pesado] ➔ [Silos de Stock] ➔ [Área de Tostión] ➔ [Área de Molienda] ➔ [Línea de Empaque] ➔ [Inspección y Etiquetado] ➔ [Bodega de Producto Terminado]**
    """)
    
    st.markdown("#### 📊 Cálculo Analítico del Factor Carga-Distancia ($W_D$)")
    st.markdown("El indicador $W_D$ cuantifica la eficiencia del layout miendo los esfuerzos mecánicos de transporte interno por semana:")
    
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
    
    st.success("🎯 **Conclusión del Layout:** La cercanía física entre las áreas críticas de Tostión y Empaque (6 metros) permite mitigar el esfuerzo de acarreo del café en caliente, optimizando el indicador logístico de planta.")

# ==============================================================================
# PÁGINA 6: BALANCEO DE LÍNEA Y ASIGNACIÓN COMPLETA
# ==============================================================================
elif opcion == "6. Balanceo de Línea y Puestos":
    st.markdown('<div class="section-header">⚡ 6. Ingeniería de Métodos: Balanceo Analítico de Línea de Producción</div>', unsafe_allow_html=True)
    st.write("")
    
    st.markdown("""
    <div class="theory-box">
        <b>Parámetros Operativos del Sistema de Producción (Línea de Empaque Café 500g):</b><br>
        • <b>Jornada Laboral Efectiva (Tiempo Disponible):</b> 1 Turno de 8 horas / día = 480 min = <b>28,800 segundos / día</b>.<br>
        • <b>Tasa de Producción Objetivo (R):</b> <b>320 unidades / día</b>.
    </div>
    """, unsafe_allow_html=True)
    
    # Cálculo formal del Tiempo de Ciclo de Ingeniería
    st.markdown("#### 📋 Paso 1: Cálculo del Tiempo de Ciclo Crítico ($T_c$)")
    st.latex(r"T_c = \frac{\text{Tiempo Disponible}}{\text{Tasa de Producción Target}} = \frac{28800 \text{ segundos}}{320 \text{ unidades}} = 90 \text{ segundos/unidad}")
    st.write("Ningún puesto operativo individual o agrupado puede exceder un tiempo de procesamiento de **90 segundos**.")

    # Datos base
    
