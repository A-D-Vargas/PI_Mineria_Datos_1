import streamlit as st

# Configuración
st.set_page_config(page_title="Streaming Analytics - Home", page_icon="🎬", layout="wide")

st.title("Análisis de Usuarios de Streaming")
st.subheader("Proyecto Integrador - Ciencia de Datos I")

st.markdown("---")

# Columnas de información
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### Contexto")
    st.write(
        "En el competitivo mercado del streaming actual, retener a los usuarios y optimizar "
        "los planes de suscripción es crucial. Esta plataforma interactiva presenta el proceso completo "
        "de auditoría, análisis exploratorio de datos (EDA) y reducción de dimensionalidad (PCA) realizado sobre "
        "nuestro dataset de comportamiento de suscriptores."
    )
    st.write(
        "A través de esta app, se comunican de forma visual y accesible las métricas clave de consumo, "
        "la calidad de los datos recopilados y los hallazgos principales que guiarán las decisiones estratégicas de retención."
    )

with col2:
    st.markdown("### Integrantes")
    st.markdown("- **Galeano Mariela**")
    st.markdown("- **Sosa Ramiro**")
    st.markdown("- **Vargas Alex**")
    
    st.markdown("### Detalles")
    st.markdown("- **Comisión:** Bandera")
    st.markdown("- **Fecha:** 4 de Julio 2026")
    
    # Enlace al repositorio de GitHub
    st.markdown("### Código Fuente")
    st.markdown("[Repositorio - GitHub](https://github.com/A-D-Vargas/PI_Mineria_Datos_1)")