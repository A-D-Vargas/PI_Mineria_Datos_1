import streamlit as st

st.set_page_config(page_title="Conclusiones", page_icon="🏁", layout="wide")
st.title("🏁 Conclusiones y Cierre")
st.markdown("---")

st.markdown("### 🎯 Hallazgos Clave")
st.success(
    "* **Estabilidad Estructural:** Se logró consolidar exitosamente una base estructurada de **8,018 registros limpios** con 0% de nulos críticos.\n"
    "* **Consumo Homogéneo:** El análisis exploratorio (EDA) demostró que el plan contratado no restringe la cantidad de minutos de visualización mensuales, planteando un desafío en la monetización de segmentos.\n"
    "* **Segmentación Compleja:** El modelo PCA corrobora que las métricas tradicionales básicas no son suficientes por sí solas para trazar fronteras lineales directas de usuarios."
)

st.markdown("### ⚠️ Limitaciones Identificadas")
st.warning(
    "* **Falta de Variables Temporales:** No poseemos datos secuenciales sobre la evolución mensual histórica para detectar tendencias de abandono (群体流失 / Churn Rate).\n"
    "* **Datos Categóricos Reducidos:** El género favorito de contenido y el país no presentan variaciones de peso estadístico directo sobre las variables de rendimiento numéricas."
)

st.markdown("### 🚀 Próximos Pasos")
st.info(
    "1. **Modelos de Clustering Avanzado:** Aplicar algoritmos no supervisados como *K-Means* o *DBSCAN* sobre las coordenadas obtenidas en el PCA para identificar tribus de consumidores.\n"
    "2. **Ingeniería de Características (Feature Engineering):** Crear ratios de tickets por minutos reproducidos para aislar usuarios con problemas técnicos severos.\n"
    "3. **Inclusión de Variables de Negocio:** Integrar los costos operativos de soporte técnico para calcular el valor de vida del cliente (CLV)."
)