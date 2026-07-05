import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dataset Info", page_icon="📊", layout="wide")

st.title("📊 Estructura y Calidad del Dataset")
st.markdown("---")

# Links de origen de datos
url_limpio = 'https://raw.githubusercontent.com/A-D-Vargas/PI_Mineria_Datos_1/refs/heads/main/1_data/processed/streaming_users_limpio.csv'

@st.cache_data
def cargar_datos():
    return pd.read_csv(url_limpio)

try:
    df = cargar_datos()
    
    st.markdown("### 🔍 Vista Previa del Dataset Limpio")
    st.write("Explorá las primeras filas del conjunto de datos ya procesado:")
    st.dataframe(df.head(10), use_container_width=True)
    
    # Resumen breve de calidad
    col1, col2, col3 = st.columns(3)
    col1.metric("Registros Totales Consolidados", f"{len(df)} filas")
    col2.metric("Columnas de Análisis", f"{len(df.columns)} columnas")
    col3.metric("Valores Nulos Remanentes", "0 nulos")
    
    st.markdown("---")
    st.markdown("### 📉 Log de Auditoría y Control de Calidad")
    st.write("El dataset original contaba con 8,160 filas. Así evolucionó la retención de registros tras corregir inconsistencias:")
    
    # Datos de tu tabla de control ajustada a 8,018 registros
    pasos_log = [
        {"Paso": "1. Carga Inicial", "Filas": 8160, "Nulos": 753, "Retención": "100.0%"},
        {"Paso": "2. Estandarización de Texto", "Filas": 8160, "Nulos": 513, "Retención": "100.0%"},
        {"Paso": "3. Filtrado de Outliers", "Filas": 8095, "Nulos": 307, "Retención": "99.20%"},
        {"Paso": "4. Depuración de Fechas", "Filas": 8018, "Nulos": 0, "Retención": "98.26%"},
        {"Paso": "5. Limpieza de Remanentes", "Filas": 8018, "Nulos": 0, "Retención": "98.26%"}
    ]
    st.table(pd.DataFrame(pasos_log))

    st.markdown("### ⚙️ Transformaciones Principales Aplicadas")
    st.markdown(
        "* **Normalización de Texto:** Conversión a minúsculas, remoción de espacios y mapeo de sinónimos para consistencia en categorías (ej. de 'std' o 'estandar' a *Estándar*).\n"
        "* **Control de Outliers:** Remoción de edades atípicas y filtrado del flag de error matemático (`99999`) detectado en los minutos de consumo.\n"
        "* **Parseo de Fechas Extensivo:** Tratamiento de formatos mixtos utilizando parseos flexibles para evitar la pérdida masiva de datos válidos."
    )

except Exception as e:
    st.error(f"No se pudieron cargar los datos de GitHub: {e}")