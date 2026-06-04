import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. CONFIGURACIÓN DE LA PÁGINA (SIEMPRE DEBE IR AL PRINCIPIO)
st.set_page_config(
    page_title="CASAENZ - Dashboard Ejecutivo",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. ESTILOS CSS E IDENTIDAD CORPORATIVA INTEGRADA
st.markdown("""
<style>
    /* Fondo beige claro institucional */
    .stApp {
        background-color: #F5F1E8;
    }
    
    /* Efecto de Marca de Agua con el logotipo */
    .stApp::before {
        content: "";
        position: fixed;
        top: 50%;
        left: 50%;
        width: 500px;
        height: 500px;
        transform: translate(-50%, -50%);
        background-image: url("https://raw.githubusercontent.com/tu-usuario/tu-repositorio/main/assets/logo.png");
        background-repeat: no-repeat;
        background-position: center;
        background-size: contain;
        opacity: 0.04;
        z-index: -1;
    }
    
    /* Estilos de títulos y métricas */
    h1, h2, h3 {
        color: #1E3F20 !important; /* Verde profundo de CASAENZ */
        font-family: 'Arial', sans-serif;
    }
    
    .stMetric {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 2px 4px 10px rgba(0,0,0,0.04);
        border-left: 5px solid #8C1D40; /* Rojo cereza de café */
    }
</style>
""", unsafe_allow_html=True)

# 3. MENÚ DE NAVEGACIÓN LATERAL
st.sidebar.markdown("# ☕ CASAENZ")
st.sidebar.markdown("### Distribución de Planta")
st.sidebar.markdown("---")

opcion = st.sidebar.radio(
    "Seleccione la Sección a Exponer:",
    [
        "Inicio / Presentación",
        "1. Factores Críticos",
        "2. Técnicas de Localización",
        "3. Red de Suministro",
        "4. Simulación FlexSim",
        "5. Distribución y Balanceo",
        "Conclusiones"
    ]
)

# --- PÁGINA: INICIO ---
if opcion == "Inicio / Presentación":
    st.title("☕ Proyecto Integrador: Diseño y Distribución de Planta")
    st.subheader("Caso de Estudio: Café Artesanal CASAENZ")
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            st.image("assets/logo.png", use_container_width=True)
        except:
            st.info("💡 Coloca tu logo en `assets/logo.png` para visualizarlo aquí.")
            
    with col2:
        st.markdown("""
        ### **Ficha Técnica de la Sustentación**
        * **Institución:** Corporación Universitaria Minuto de Dios - UNIMINUTO
        * **Programa:** Ingeniería Industrial
        * **Autora:** Laura Juliana Loaiza Saavedra (ID: 428429)
        
        ### **Propósito Ejecutivo**
        Esta aplicación interactiva funciona como un **Dashboard de Decisiones Estratégicas** para sustentar la viabilidad técnica, operativa y logística del procesamiento y empaque de café premium en el departamento del Valle del Cauca.
        """)

# --- PÁGINA: PREGUNTA 1 ---
elif opcion == "1. Factores Críticos":
    st.header("1. Factores Críticos de Localización de Plantas")
    st.markdown("Definición cualitativa y cuantitativa de los criterios ponderados para los centros de operaciones.")
    
    st.success("""
    **Criterio de Selección:** Se determinaron 6 factores esenciales bajo la metodología analítica, asignando un peso porcentual de acuerdo con su impacto directo en los costos de operación y el nivel de servicio al cliente.
    """)
    
    factores = {
        "Factor Crítico de Localización": [
            "Proximidad a Proveedores de Materia Prima",
            "Infraestructura Vial y Conectividad",
            "Cercanía al Mercado Objetivo / Clientes",
            "Costos Operativos (Arriendos, Servicios)",
            "Disponibilidad de Mano de Obra Calificada",
            "Seguridad y Entorno Comercial"
        ],
        "Peso Asignado (%)": [25, 20, 25, 20, 10, 15]
    }
    df_f = pd.DataFrame(factores)
    
    col1, col2 = st.columns([4, 5])
    with col1:
        st.write("### Matriz de Priorización")
        st.dataframe(df_f, hide_index=True, use_container_width=True)
    with col2:
        st.write("### Gráfico de Peso Relativo")
        fig = px.bar(
            df_f, 
            x="Peso Asignado (%)", 
            y="Factor Crítico de Localización", 
            orientation="h",
            color="Peso Asignado (%)",
            color_continuous_scale=["#A3B899", "#1E3F20"]
        )
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

# --- PÁGINA: PREGUNTA 2 ---
elif opcion == "2. Técnicas de Localización":
    st.header("2. Técnicas Cuantitativas de Localización")
    st.markdown("Resultados de la aplicación de los métodos de Factores Ponderados, Centro de Gravedad y Análisis CVU.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            label="📍 Ubicación de la Planta de Fabricación", 
            value="Cali", 
            help="Elegida por el método de factores ponderados gracias a su infraestructura y disponibilidad de servicios."
        )
    with col2:
        st.metric(
            label="🚚 Ubicación del Centro de Distribución (CD)", 
            value="Palmira", 
            help="Punto óptimo obtenido mediante el análisis de Centro de Gravedad para minimizar distancias hacia el mercado del Valle."
        )
        
    st.write("### Matriz de Posicionamiento Geográfico Regional")
    st.markdown("Representación del plano cartesiano de gravedad basado en las distancias e índices de demanda del Valle del Cauca:")
    
    coordenadas = pd.DataFrame({
        'Nodo Logístico': ['Cali', 'Palmira', 'Buga', 'Tuluá', 'Yotoco', 'Ginebra'],
        'Eje X (Lat)': [3.4516, 3.5394, 3.9009, 4.0847, 3.8625, 3.7258],
        'Eje Y (Lon)': [-76.5320, -76.3036, -76.2978, -76.1986, -76.3853, -76.2662],
        'Clasificación': ['Planta de Fabricación', 'Centro de Distribución (CD)', 'Punto de Demanda', 'Punto de Demanda', 'Origen Materia Prima', 'Origen Materia Prima']
    })
    
    fig_geo = px.scatter(
        coordenadas, x='Eje Y (Lon)', y='Eje X (Lat)', color='Clasificación', text='Nodo Logístico',
        color_discrete_map={
            'Planta de Fabricación': '#8C1D40', 
            'Centro de Distribución (CD)': '#1E3F20', 
            'Punto de Demanda': '#D4AF37', 
            'Origen Materia Prima': '#A3B899'
        }
    )
    fig_geo.update_traces(textposition='top center', marker=dict(size=14, line=dict(width=1, color='DarkSlateGrey')))
    st.plotly_chart(fig_geo, use_container_width=True)

# --- PÁGINA: PREGUNTA 3 ---
elif opcion == "3. Red de Suministro":
    st.header("3. Diseño de la Red de Suministros")
    st.markdown("Estructuración del modelo matemático de optimización lineal de transporte.")
    
    st.write("### Formulación del Modelo Matemático")
    st.markdown("El modelo busca la **minimización global de los costos logísticos de transporte** entre los centros de suministro, transformación y consumo:")
    
    st.latex(r"Min \quad Z = \sum_{i=1}^{m} \sum_{j=1}^{n} C_{ij} X_{ij}")
    
    st.markdown("**Sujeto a las siguientes restricciones de ingeniería:**")
    st.latex(r"\sum_{j=1}^{n} X_{ij} \le Capacidad_{i} \quad \forall i \quad \text{(Restricción de Capacidad de Fincas)}")
    st.latex(r"\sum_{i=1}^{m} X_{ij} = Demanda_{j} \quad \forall j \quad \text{(Restricción de Satisfacción del Cliente)}")
    st.latex(r"X_{ij} \ge 0 \quad \text{(Garantía de No Negatividad de Flujos)}")
    
    st.write("### Estructura de Flujo Físico")
    st.code("""
    [ Proveedores de Grano ]                [ Centro de Transformación ]            [ Nodo Logístico ]            [ Mercado Final ]
       - Yotoco (Café MP)   ───┐
       - Tuluá (Café MP)    ───┼───────►    PLANTA DE FABRICACIÓN    ───────►      CENTRO DE       ───────►   Consumidores Valle
       - Ginebra (Café MP)  ───┘                    (Cali)                      DISTRIBUCIÓN (Palmira)
    """, language="text")

# --- PÁGINA: PREGUNTA 4 ---
elif opcion == "4. Simulación FlexSim":
    st.header("4. Simulación Dinámica de Operaciones de Piso")
    st.markdown("Validación del comportamiento físico del sistema productivo ante variaciones de la demanda.")
    
    col1, col2 = st.columns([3, 2])
    with col1:
        st.write("### Representación en FlexSim de Eventos Discretos")
        try:
            st.image("assets/flexsim_1.png", caption="Modelación en 3D de las estaciones de procesamiento CASAENZ", use_container_width=True)
        except:
            st.warning("Para mostrar la simulación en el dashboard, sube tu captura de pantalla a la ruta: `assets/flexsim_1.png`")
            
        try:
            with open("assets/flexsim.mp4", "rb") as v_file:
                st.video(v_file.read())
        except:
            st.info("💡 Nota: Si tienes un video en formato `.mp4` de tu simulación corriendo en FlexSim, puedes guardarlo como `assets/flexsim.mp4` para reproducirlo aquí.")
            
    with col2:
        st.write("### Indicadores de Desempeño Operativo (KPIs)")
        st.metric(label="📊 Eficiencia de Utilización de Maquinaria", value="85.20 %")
        st.metric(label="📦 Rendimiento de Producción (Throughput)", value="320 Bolsas / Día")
        st.metric(label="⏳ Tiempo Promedio de Permanencia en Cola", value="42 segundos")
        
        st.info("""
        **Tipo de Distribución Empleada:**
        Se seleccionó una **Distribución por Producto (Línea de Flujo)**. El análisis de simulación demostró que esta configuración lineal optimiza el paso entre Tostión, Molienda y Empaque, evitando cuellos de botella por acumulación de Inventario en Proceso (WIP).
        """)

# --- PÁGINA: PREGUNTA 5 ---
elif opcion == "5. Distribución y Balanceo":
    st.header("5. Distribución de Planta y Balanceo Analítico de Línea")
    st.markdown("Detalle técnico de ingeniería para los recorridos, cargas y balanceo secuencial de estaciones.")
    
    pestana1, pestana2, pestana3 = st.tabs(["📐 Layout y Carga-Distancia", "⚙️ Balanceo Analítico", "👥 Asignación de Puestos"])
    
    with pestana1:
        st.write("### Planos Técnicos del Proceso")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### Plano de Bloques Industrial")
            try: st.image("assets/plano_bloques.png", use_container_width=True)
            except: st.error("Falta cargar el archivo en: `assets/plano_bloques.png`")
        with c2:
            st.markdown("#### Diagrama de Hilos Metodológico")
            try: st.image("assets/diagrama_hilos.png", use_container_width=True)
            except: st.error("Falta cargar el archivo en: `assets/diagrama_hilos.png`")
            
        st.write("### Modelo de Minimización de Recorridos")
        st.latex(r"WD = \sum_{i=1}^{M} \sum_{j=1}^{M} W_{ij} D_{ij}")
        st.
