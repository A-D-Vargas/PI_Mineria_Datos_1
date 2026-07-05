import streamlit as st
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="PCA Analysis", layout="wide")
st.title("Análisis de Componentes Principales (PCA)")
st.markdown("---")

url_limpio = 'https://raw.githubusercontent.com/A-D-Vargas/PI_Mineria_Datos_1/refs/heads/main/1_data/processed/streaming_users_limpio.csv'

try:
    df = pd.read_csv(url_limpio)
    
    # Selección de variables numéricas
    features = ['age', 'monthly_watch_time_mins', 'customer_support_tickets']
    st.markdown("### Configuración Estadística")
    st.write(f"**Variables utilizadas para el modelo:** {', '.join(features)}")
    st.write("**Escalamiento aplicado:** `StandardScaler` (Z-score normalization, mandatorio para equiparar magnitudes de minutos y tickets).")
    
    # Procesamiento
    X = df[features].dropna()
    X_scaled = StandardScaler().fit_transform(X)
    
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    
    var_explicada = pca.explained_variance_ratio_
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Varianza Explicada Acumulada")
        fig, ax = plt.subplots(figsize=(6, 4))
        componentes = ['PC1', 'PC2']
        ax.bar(componentes, var_explicada, color='teal', alpha=0.7, label='Individual')
        ax.plot(componentes, var_explicada.cumsum(), marker='o', color='darkorange', label='Acumulado')
        ax.set_ylabel("Porcentaje de Varianza")
        ax.legend()
        st.pyplot(fig)
        st.write(f"**PC1 explica:** {var_explicada[0]*100:.2f}% | **PC2 explica:** {var_explicada[1]*100:.2f}%")
        
    with col2:
        st.markdown("### Proyección de Usuarios en el Espacio PCA")
        df_pca = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.scatterplot(x='PC1', y='PC2', data=df_pca.sample(1000, random_state=42), alpha=0.5, color='darkblue', ax=ax)
        st.pyplot(fig)
        
    st.markdown("### Interpretación del PCA")
    st.info(
        "Las primeras dos componentes principales capturan una fracción representativa de la inercia total de los datos. "
        "La dispersión uniforme indica que las variaciones en el tiempo de consumo mensual y la fricción por reclamos "
        "en soporte no siguen patrones lineales agrupados obvios, lo que sugiere perfiles de comportamiento muy heterogéneos "
        "entre los suscriptores."
    )

except Exception as e:
    st.error(f"Error procesando el análisis PCA: {e}")