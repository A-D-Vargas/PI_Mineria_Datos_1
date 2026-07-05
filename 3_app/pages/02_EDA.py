import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="EDA", page_icon="📈", layout="wide")
st.title("📈 Análisis Exploratorio de Datos (EDA)")
st.markdown("---")

url_limpio = 'https://raw.githubusercontent.com/A-D-Vargas/PI_Mineria_Datos_1/refs/heads/main/1_data/processed/streaming_users_limpio.csv'

try:
    df = pd.read_csv(url_limpio)
    
    # ----- 1. VISUALIZACIONES UNIVARIADAS (2) -----
    st.markdown("## 📊 1. Análisis Univariado")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Distribución de la Edad de los Usuarios")
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.histplot(df['age'], bins=20, kde=True, color='skyblue', ax=ax)
        ax.set_xlabel("Edad")
        ax.set_ylabel("Frecuencia")
        st.pyplot(fig)
        st.info("**Interpretación:** La población analizada muestra una distribución madura y activa, concentrando el volumen principal de usuarios entre los 25 y 45 años.")

    with col2:
        st.markdown("### Preferencia de Planes de Suscripción")
        fig, ax = plt.subplots(figsize=(6, 4))
        df['subscription_plan'].value_counts().plot(kind='bar', color='salmon', ax=ax)
        ax.set_xlabel("Plan de Suscripción")
        ax.set_ylabel("Cantidad de Usuarios")
        plt.xticks(rotation=0)
        st.pyplot(fig)
        st.info("**Interpretación:** Existe una distribución equitativa de usuarios entre los distintos niveles de membresía, permitiendo análisis comparativos estables por segmento.")

    st.markdown("---")

    # ----- 2. VISUALIZACIONES BIVARIADAS (2) -----
    st.markdown("## 📊 2. Análisis Bivariado")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("### Tiempo de Reproducción según el Plan")
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.boxplot(x='subscription_plan', y='monthly_watch_time_mins', data=df, palette='Set2', ax=ax)
        ax.set_xlabel("Plan")
        ax.set_ylabel("Minutos Mensuales")
        st.pyplot(fig)
        st.info("**Interpretación:** Sorprendentemente, los niveles de uso del servicio se mantienen estables horizontalmente, sugiriendo que la limitación de planes no altera drásticamente el consumo horario.")

    with col4:
        st.markdown("### Tickets de Soporte por Rango Etario")
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.scatterplot(x='age', y='customer_support_tickets', data=df, alpha=0.3, color='purple', ax=ax)
        ax.set_xlabel("Edad")
        ax.set_ylabel("Tickets Generados")
        st.pyplot(fig)
        st.info("**Interpretación:** No se visualizan tendencias ni correlaciones lineales marcadas entre la edad del cliente y la frecuencia de reportes dirigidos a soporte.")

    st.markdown("---")

    # ----- 3. VISUALIZACIÓN MULTIVARIADA (1) -----
    st.markdown("## 📊 3. Análisis Multivariado")
    
    st.markdown("### Correlación Numérica de Variables Clave")
    columnas_num = df.select_dtypes(include=['float64', 'int64']).columns
    
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.heatmap(df[columnas_num].corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, ax=ax)
    st.pyplot(fig)
    st.info("**Interpretación:** La matriz revela coeficientes de correlación débiles entre las métricas demográficas y de uso del servicio, indicando la necesidad de recurrir a reducción estadística como PCA para agrupar comportamientos de manera alternativa.")

except Exception as e:
    st.error(f"Error al graficar el EDA: {e}")