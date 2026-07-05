import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Proyecto Minería de Datos 1", page_icon="🎬", layout="centered")

st.title(" Análisis de Usuarios de Streaming")
st.subheader("Proyecto Integrador - Minería de Datos I")

st.markdown("---")

# Información del proyecto
col1, col2 = st.columns(2)
with col1:
    st.markdown("### Integrantes:")
    st.write(''' 
    **  Galeano Mariela**   
    **  Sosa Ramiro**   
    **  Vargas Alex Daniel**  ''')  
with col2:
    st.markdown("### Detalles:")
    st.write("- **Comisión:** [Bandera]")
    st.write("- **Fecha:** 4 de Julio 2026")

st.markdown("---")

# Contexto Breve
st.markdown("""
### 📊 Contexto del Proyecto
Este proyecto tiene como objetivo analizar el comportamiento, consumo y características de los usuarios de una plataforma de streaming audiovisual. 
Realizamos un proceso completo que abarca desde la limpieza de datos y el Análisis Exploratorio (EDA), hasta la reducción de dimensionalidad mediante **PCA (Análisis de Componentes Principales)**. 

El fin último es identificar patrones clave que permitan entender mejor la retención de usuarios y optimizar las estrategias de la plataforma.
""")

st.markdown("---")

# Enlace al repositorio de GitHub
st.markdown("### Código Fuente")
st.info("Puedes revisar el desarrollo técnico completo, los notebooks de respaldo y el pipeline de datos en nuestro repositorio:")
st.link_button("Ir al Repositorio de GitHub", "https://github.com/A-D-Vargas/PI_Mineria_Datos_1.git")