import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="CASAENZ",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>",
                unsafe_allow_html=True)

logo = Image.open("assets/logo.png")

col1, col2 = st.columns([1,4])

with col1:
    st.image(logo, width=180)

with col2:
    st.title("☕ Café Artesanal CASAENZ")
    st.subheader("Proyecto Integrador - Distribución de Planta")

st.markdown("---")

st.markdown("""
### Bienvenido

Aplicación interactiva desarrollada para presentar:

- Factores de localización
- Métodos de localización
- Red de suministro
- Simulación FlexSim
- Distribución de planta
- Balanceo de línea
""")
