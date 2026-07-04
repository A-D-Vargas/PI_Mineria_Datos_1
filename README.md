# Información General
Este proyecto presenta un análisis de datos enfocado en el comportamiento de consumo y soporte técnico de los usuarios de una plataforma de streaming. El desarrollo abarca desde el proceso de extracción, transformación y carga (ETL), hasta la exploración estadística y una interfaz final interactiva.

**Curso**: Mineria de datos 1

App: Panel en Streamlit Cloud (Reemplazar por el enlace real)

# Objetivo del Proyecto
El objetivo principal es analizar el comportamiento de los usuarios, sus preferencias de contenido y los problemas de soporte técnico para descubrir qué factores impulsan el consumo y detectar fallas críticas en el servicio. A través de este análisis, se busca aportar información basada en datos para optimizar la retención de clientes y la personalización del catálogo.

# Dataset
El conjunto de datos original cuenta con información sobre los clientes de la plataforma, incluyendo variables demográficas, tipos de suscripción, minutos de visualización mensuales, géneros preferidos y tickets de soporte técnico generados.

**Dataset Limpio**: "https://raw.githubusercontent.com/A-D-Vargas/PI_Mineria_Datos_1/refs/heads/main/1_data/processed/streaming_users_limpio.csv"

**Volumen Final**: 8,018 registros estandarizados y sin duplicados.

# Estructura del Repositorio

# Preparación y Calidad de Datos
El proceso se documentó detalladamente en el notebook 01_etl.ipynb y sus eventos se guardaron en etl_process.log. Las acciones principales incluyeron la eliminación de registros duplicados y el tratamiento de valores nulos en variables clave. Se estandarizaron los nombres de las columnas a formato snake_case y se corrigieron los tipos de datos de las variables categóricas. También se aplicaron filtros de consistencia para asegurar que los minutos de visualización y las edades se encontraran dentro de rangos lógicos y consistentes para el negocio.

# Resumen del Análisis Exploratorio
Los análisis univariados, bivariados y multivariados desarrollados en los notebooks 02_eda_univariado.ipynb y 03_eda_bivariado_multivariado.ipynb revelaron que el consumo mensual está directamente ligado al nivel de suscripción, siendo el plan Premium el que duplica en minutos al plan Básico. Los usuarios Premium muestran una marcada preferencia por contenidos de Drama y Documentales. Por otro lado, se comprobó estadísticamente que la edad no influye en los géneros elegidos, mostrando un comportamiento transversal. Geográficamente, se detectó que los usuarios Premium en Chile y Perú concentran un nivel críticamente alto de reclamos de soporte técnico.

# Reducción de Dimensionalidad
En el cuaderno 04_pca.ipynb se aplicó un escalamiento de datos utilizando StandardScaler sobre las variables cuantitativas. Al ejecutar el Análisis de Componentes Principales (PCA), se determinó que cada una de las tres componentes explicaba aproximadamente el ~33% de la varianza. Debido a esta nula correlación lineal entre las variables, el PCA no resultó viable para reducir dimensiones sin perder información crítica, por lo que se decidió conservar las tres variables originales para mantener la integridad del modelo.

# Visualización Interactiva
La aplicación desarrollada en Streamlit (app.py) funciona como un portfolio unificado para exponer de manera ordenada la estructura del proyecto. Permite al usuario navegar a través de las diferentes etapas, visualizar la calidad del proceso ETL mediante el registro de logs, revisar los hallazgos de las etapas exploratorias y acceder a las conclusiones finales de forma cómoda e intuitiva.
