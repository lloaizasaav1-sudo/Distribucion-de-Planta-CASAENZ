import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Configuración de la página
st.set_page_config(
    page_title="Café Artesanal CASAENZ - Planta y Logística",
    page_icon="☕",
    layout="wide"
)

# Estilo personalizado para emular la paleta de la marca (Verde, Dorado, Beige)
st.markdown("""
    <style>
    .main-title { font-size:42px !important; color:#1e4620; font-weight:bold; text-align:center; }
    .subtitle { font-size:24px !important; color:#d4af37; font-weight:bold; }
    .section-box { padding: 15px; border-radius: 10px; background-color: #fcfbfa; border-left: 5px solid #1e4620; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">☕ Proyecto Integrador: Diseño y Distribución de Planta</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-style:italic;">Caso de Estudio: Café Artesanal CASAENZ (Valle del Cauca)</p>', unsafe_allow_html=True)
st.write("---")

# Menú de navegación interactivo para la presentación
menu = st.sidebar.radio(
    "Navegación de la Exposición",
    [
        "Introducción y Concepto",
        "1. Factores Críticos",
        "2. Técnicas de Localización (Interactiva)",
        "3. Red de Suministros y Modelo Matemático",
        "4. Simulación en Piso (FlexSim)",
        "5. Distribución Interna y Balanceo"
    ]
)

# ==========================================
# SECCIÓN: INTRODUCCIÓN Y CONCEPTO
# ==========================================
if menu == "Introducción y Concepto":
    st.markdown('<p class="subtitle">Concepto del Producto y la Marca</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(
            """
            <div class="section-box">
            <b>¿Qué es Café CASAENZ?</b><br>
            Es un café colombiano Premium cultivado y tostado de manera artesanal en el Valle del Cauca. 
            Busca ofrecer una experiencia sensorial auténtica mediante granos seleccionados y procesos tradicionales.
            </div>
            """, unsafe_allow_html=True)
        
        st.subheader("Significado Semiótico del Naming")
        st.write("**CASA:** Representa origen, tradición, familia, calidez y cercanía.")
        st.write("**ENZ:** Representa la filosofía de la marca: **E**xcelencia, **N**aturaleza y **Z**en (bienestar/armonía).")
        
        st.subheader("Identidad Cromática")
        st.markdown("- **Verde Profundo/Medio:** Naturaleza, origen, frescura y sostenibilidad.")
        st.markdown("- **Dorado:** Sofisticación, calidad Premium y exclusividad.")
        st.markdown("- **Rojo Cereza:** El fruto del café en su estado óptimo de maduración.")
    
    with col2:
        st.info("💡 **Propuesta de Valor:** Mitigar el problema de los cafés masificados industriales, ofreciendo total transparencia en el origen, procesos artesanales reales y conexión con la cultura cafetera regional.")

# ==========================================
# SECCIÓN 1: FACTORES CRÍTICOS
# ==========================================
elif menu == "1. Factores Críticos":
    st.markdown('<p class="subtitle">1. Factores Críticos de Localización</p>', unsafe_allow_html=True)
    st.write("Para localizar la planta de procesamiento y los centros de distribución, se determinaron los siguientes pilares de la Ingeniería Industrial:")
    
    factors = {
        "Factor Crítico": [
            "Proximidad a Proveedores",
            "Infraestructura Vial",
            "Cercanía al Mercado",
            "Costos Operativos",
            "Disponibilidad de Mano de Obra",
            "Seguridad y Entorno"
        ],
        "Impacto Estratégico": [
            "Garantiza la frescura del grano y disminuye costos de flete de materia prima.",
            "Conexión clave con los corredores del Valle del Cauca (Cali, Palmira, Buga, Yotoco).",
            "Acceso rápido a centros urbanos de alto consumo de café Premium.",
            "Evaluación de arriendos, servicios públicos e impuestos locales.",
            "Acceso a personal capacitado para tareas de tostión, empaque y logística.",
            "Estabilidad comercial y mitigación de riesgos operativos en el transporte."
        ]
    }
    st.table(pd.DataFrame(factors))

# ==========================================
# SECCIÓN 2: TÉCNICAS DE LOCALIZACIÓN
# ==========================================
elif menu == "2. Técnicas de Localización (Interactiva)":
    st.markdown('<p class="subtitle">2. Análisis y Modelos de Localización</p>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["Costo-Volumen-Utilidad", "Calificación de Factores", "Centro de Gravedad (Dinámico)"])
    
    with tab1:
        st.subheader("Método CVU (Análisis de Costo Total)")
        st.write("Fórmula utilizada: $CT = CF + (CV \\times Q)$")
        
        q_prod = st.slider("Selecciona el volumen de producción mensual (Q):", 1000, 20000, 10000)
        
        # Datos del word
        df_cvu = pd.DataFrame({
            "Ciudad": ["Cali", "Palmira", "Buga"],
            "Costo Fijo (CF)": [4500000, 3200000, 2800000],
            "Costo Variable Unit (CV)": [3500, 4200, 4800]
        })
        
        df_cvu["Costo Total Calculado"] = df_cvu["Costo Fijo (CF)"] + (df_cvu["Costo Variable Unit (CV)"] * q_prod)
        st.dataframe(df_cvu.style.format({"Costo Fijo (CF)": "${:,.0f}", "Costo Variable Unit (CV)": "${:,.0f}", "Costo Total Calculado": "${:,.0f}"}))
        
        best_cvu = df_cvu.loc[df_cvu["Costo Total Calculado"].idxmin()]["Ciudad"]
        st.success(f"🏆 Para un volumen de {q_prod:,} unidades, la mejor alternativa económica es: **{best_cvu}**")
        
    with tab2:
        st.subheader("Método de Factor Rating (Ponderación de Factores)")
        # Matriz del word
        factors_data = pd.DataFrame({
            "Factor": ["Cercanía proveedores", "Infraestructura vial", "Cercanía mercado", "Costos operativos", "Mano de obra"],
            "Peso": [0.25, 0.20, 0.25, 0.20, 0.10],
            "Cali": [8, 9, 10, 7, 9],
            "Palmira": [8, 8, 8, 8, 8],
            "Buga": [9, 7, 7, 9, 7]
        })
        st.dataframe(factors_data)
        
        # Calcular puntajes
        p_cali = np.sum(factors_data["Peso"] * factors_data["Cali"])
        p_pal = np.sum(factors_data["Peso"] * factors_data["Palmira"])
        p_buga = np.sum(factors_data["Peso"] * factors_data["Buga"])
        
        st.write(f"**Puntuaciones Finales:** 📍 Cali: `{p_cali:.2f}` | 📍 Palmira: `{p_pal:.2f}` | 📍 Buga: `{p_buga:.2f}`")
        st.info("Conclusión del modelo: **Cali** obtiene la mayor puntuación debido a su infraestructura y concentración de mercado.")

    with tab3:
        st.subheader("📍 Localizador por Centro de Gravedad")
        st.write("Modifica las coordenadas o demandas de tus clientes para recalcular la posición óptima del Centro de Distribución.")
        
        # Entradas dinámicas para simular ruteo y localización
        col_c1, col_c2, col_c3 = st.columns(3)
        with col_c1:
            st.markdown("**Nodo 1: Cali**")
            cx = st.number_input("Coordenada X (Cali)", value=100.0)
            cy = st.number_input("Coordenada Y (Cali)", value=200.0)
            cdem = st.number_input("Demanda kg (Cali)", value=5000)
            cfi = st.number_input("Tarifa f_i (Cali)", value=3500)
        with col_c2:
            st.markdown("**Nodo 2: Palmira**")
            px = st.number_input("Coordenada X (Palmira)", value=115.0)
            py = st.number_input("Coordenada Y (Palmira)", value=215.0)
            pdem = st.number_input("Demanda kg (Palmira)", value=4100)
            pfi = st.number_input("Tarifa f_i (Palmira)", value=2800)
        with col_c3:
            st.markdown("**Nodo 3: Buga**")
            bx = st.number_input("Coordenada X (Buga)", value=120.0)
            by = st.number_input("Coordenada Y (Buga)", value=280.0)
            bdem = st.number_input("Demanda kg (Buga)", value=3200)
            bfi = st.number_input("Tarifa f_i (Buga)", value=2100)
            
        # Algoritmo matemático de centro de gravedad
        denom = (cdem * cfi) + (pdem * pfi) + (bdem * bfi)
        num_x = (cx * cdem * cfi) + (px * pdem * pfi) + (bx * bdem * bfi)
        num_y = (cy * cdem * cfi) + (py * pdem * pfi) + (by * bdem * bfi)
        
        target_x = num_x / denom
        target_y = num_y / denom
        
        st.metric(label="Coordenada Óptima X del CEDI", value=f"{target_x:.2f}")
        st.metric(label="Coordenada Óptima Y del CEDI", value=f"{target_y:.2f}")
        
        # Gráfico interactivo de localización
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.scatter([cx, px, bx], [cy, py, by], color="blue", s=100, label="Clientes/Nodos")
        ax.scatter(target_x, target_y, color="red", marker="*", s=250, label="CEDI Óptimo (Centro Gravedad)")
        for txt, x, y in zip(["Cali", "Palmira", "Buga"], [cx, px, bx], [cy, py, by]):
            ax.annotate(txt, (x+1, y+1))
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

# ==========================================
# SECCIÓN 3: RED DE SUMINISTROS Y MODELO MATEMÁTICO
# ==========================================
elif menu == "3. Red de Suministros y Modelo Matemático":
    st.markdown('<p class="subtitle">3. Optimización de la Red de Suministros</p>', unsafe_allow_html=True)
    st.write("Estructura de la red planteada de 3 eslabones: **Proveedores** $\\rightarrow$ **Planta/CEDI** $\\rightarrow$ **Clientes Finales**.")
    
    st.subheader("Formulación Matemática de Transporte (Ruteo de Abastecimiento)")
    st.markdown("""
    * **Función Objetivo:** Minimizar $Z = \\sum \\sum c_{ij} X_{ij}$
    * **Restricción de Oferta:** $\\sum X_{ij} \\leq a_i$
    * **Restricción de Demanda:** $\\sum X_{ij} = b_j$
    """)
    
    # Resolver dinámicamente usando programación lineal (Scipy)
    # Costos del documento
    costs = np.array([
        [12, 10, 15, 18],  # Yotoco
        [14, 12, 10, 8],   # Tuluá
        [13, 11, 12, 16]   # Ginebra
    ])
    
    supply = [700, 500, 400]
    demand = [400, 500, 300, 400]
    
    # Programación lineal para transporte
    c = costs.flatten()
    A_eq = []
    b_eq = []
    
    # Restricciones oferta (filas)
    for i in range(3):
        row = np.zeros((3, 4))
        row[i, :] = 1
        A_eq.append(row.flatten())
        b_eq.append(supply[i])
        
    # Restricciones demanda (columnas)
    for j in range(4):
        col = np.zeros((3, 4))
        col[:, j] = 1
        A_eq.append(col.flatten())
        b_eq.append(demand[j])
        
    res = linprog(c, A_eq_rows=A_eq, b_eq_rows=b_eq, method='highs')
    
    if res.success:
        alloc = res.x.reshape(3, 4)
        df_alloc = pd.DataFrame(alloc, index=["Yotoco", "Tuluá", "Ginebra"], columns=["Cali", "Palmira", "Buga", "Tuluá"])
        st.subheader("Asignación de Carga Óptima Calculada (kg/Materia Prima)")
        st.dataframe(df_alloc)
        st.success(f"Costo Mínimo Total de Transporte Optimizado: ${res.fun:,.2f} USD/Unidades Monetarias")
    else:
        st.error("No se pudo calcular la asignación óptima de rutas.")

# ==========================================
# SECCIÓN 4: SIMULACIÓN EN PISO
# ==========================================
elif menu == "4. Simulación en Piso (FlexSim)":
    st.markdown('<p class="subtitle">4. Simulación del Sistema Productivo en FlexSim</p>', unsafe_allow_html=True)
    st.write("Esta sección sirve de puente interactivo para la defensa de tu simulación en vivo.")
    
    st.info("📢 **Nota para el expositor:** Abre tu software **FlexSim** en paralelo y muestra el modelo en 3D corriendo con los siguientes parámetros analizados en el documento.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Flujo del Proceso Validado")
        st.markdown("""
        1. **Recepción** de Café Verde e Insumos (Bolsas)
        2. **Almacenamiento** Temporal en Silos/Racks
        3. Operación de **Tostión y Molienda** (Cuello de botella estimado)
        4. Línea de **Empaque y Sellado**
        5. **Despacho** Logístico
        """)
    with col2:
        st.subheader("Tipo de Distribución Empleada")
        st.warning("Se determinó una **Distribución por Producto (Línea de producción)** para el flujo principal del café, garantizando trayectorias lineales simples y reduciendo tiempos muertos en el piso de producción.")

# ==========================================
# SECCIÓN 5: DISTRIBUCIÓN INTERNA Y BALANCEO
# ==========================================
elif menu == "5. Distribución Interna y Balanceo":
    st.markdown('<p class="subtitle">5. Diagrama de Hilos, Distribución WD y Balanceo de Línea</p>', unsafe_allow_html=True)
    
    st.subheader("Análisis de Desplazamiento Carga-Distancia ($WD$)")
    st.write("Fórmula del Esfuerzo de Manejo de Materiales: $WD = \\sum (W_i \\times D_i)$")
    
    # Matriz del documento
    wd_df = pd.DataFrame({
        "Tramo Flujo": ["A-C (Café Verde)", "C-D (A Proceso)", "D-E (A Empaque)", "E-F (A Almacén PT)", "F-G (A Despacho)", "B-E (Ingreso Bolsas)"],
        "Distancia (m)": [8, 12, 6, 5, 10, 15],
        "Carga Semanal (kg)": [500, 500, 480, 480, 480, 200]
    })
    wd_df["Esfuerzo WD (kg·m)"] = wd_df["Distancia (m)"] * wd_df["Carga Semanal (kg)"]
    st.dataframe(wd_df)
    st.metric(label="Factor WD Total de la Planta", value=f"{wd_df['Esfuerzo WD (kg·m)'].sum():,} kg·m/semana")
    
    st.write("---")
    st.subheader("⏱️ Indicadores de Balanceo de Línea de Producción")
    
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        st.markdown("**Datos Base de Operación (Supuestos del Proyecto)**")
        st.write("- **Demanda diaria requerida:** 320 paquetes")
        st.write("- **Tiempo disponible (8 horas):** 28,800 segundos")
        st.write("- **Tiempo de Ciclo Máximo ($TC$):** 90 segundos/unidad")
        st.write("- **Estaciones de Trabajo Diseñadas:** 6 estaciones")
    
    with col_b2:
        st.markdown("**Métricas de Eficiencia del Sistema**")
        st.metric(label="Eficiencia Global de Línea ($E$)", value="69.44 %")
        st.metric(label="Retraso del Balanceo ($RB$)", value="30.56 %")
        st.metric(label="Tiempo Ocioso Total ($TO$)", value="165 segundos")
        
    st.success("🎯 **Conclusión Técnica Final:** El balanceo estructural con 6 estaciones asegura el cumplimiento estricto de la tasa de producción de Café CASAENZ. Se sugiere al jurado la oportunidad de optimizar las estaciones combinando tareas automatizadas en el empaque y sellado para elevar la eficiencia arriba del 80%.")
