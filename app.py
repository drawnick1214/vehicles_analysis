import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Análisis de Vehículos", page_icon="🚗", layout="wide")

# Título principal
st.title("🚗 Análisis de Anuncios de Venta de Coches")

# Encabezado
st.header("Visualización de Datos de Vehículos")

# Leer los datos del archivo CSV (ruta relativa para deploy)
car_data = pd.read_csv('vehicles_us.csv')

# Mostrar información básica del dataset
st.write(f"El conjunto de datos contiene **{len(car_data):,}** anuncios de vehículos.")

# Crear casillas de verificación para los gráficos
st.subheader("Selecciona los gráficos que deseas visualizar:")

# Checkbox para histograma
build_histogram = st.checkbox('Construir histograma de odómetro')

if build_histogram:
    st.write('**Histograma:** Distribución de kilometraje de los vehículos')
    
    # Crear histograma con plotly express
    fig_hist = px.histogram(
        car_data, 
        x='odometer',
        nbins=50,
        title='Distribución del Odómetro',
        labels={'odometer': 'Kilometraje (millas)', 'count': 'Cantidad de vehículos'}
    )
    fig_hist.update_layout(
        xaxis_title="Kilometraje (millas)",
        yaxis_title="Cantidad de vehículos"
    )
    
    st.plotly_chart(fig_hist, use_container_width=True)

# Checkbox para gráfico de dispersión
build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_scatter:
    st.write('**Gráfico de dispersión:** Relación entre el odómetro y el precio')
    
    # Filtrar datos válidos (sin valores nulos en las columnas relevantes)
    scatter_data = car_data.dropna(subset=['odometer', 'price'])
    
    # Crear gráfico de dispersión con plotly express
    fig_scatter = px.scatter(
        scatter_data,
        x='odometer',
        y='price',
        title='Relación entre Kilometraje y Precio',
        labels={'odometer': 'Kilometraje (millas)', 'price': 'Precio (USD)'},
        opacity=0.5
    )
    fig_scatter.update_layout(
        xaxis_title="Kilometraje (millas)",
        yaxis_title="Precio (USD)"
    )
    
    st.plotly_chart(fig_scatter, use_container_width=True)
