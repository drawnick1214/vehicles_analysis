# 🚗 Análisis de Anuncios de Venta de Coches

Aplicación web interactiva para explorar y visualizar datos de anuncios de venta de vehículos usados en Estados Unidos.

## Descripción

Esta aplicación permite a los usuarios analizar un conjunto de datos de vehículos mediante visualizaciones interactivas. Incluye:

- **Histograma de kilometraje:** Muestra la distribución del odómetro de los vehículos anunciados.
- **Gráfico de dispersión:** Visualiza la relación entre el kilometraje y el precio de los vehículos.

## Tecnologías utilizadas

- **Python 3**
- **Streamlit** - Framework para crear aplicaciones web de datos
- **Pandas** - Manipulación y análisis de datos
- **Plotly Express** - Visualizaciones interactivas

## Cómo ejecutar la aplicación localmente

1. Clona el repositorio:
   ```bash
   git clone <url-del-repositorio>
   cd 3T_proyecto_s7
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En macOS/Linux
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta la aplicación:
   ```bash
   streamlit run app.py
   ```

5. Abre tu navegador en `http://localhost:8501`

## Estructura del proyecto

```
3T_proyecto_s7/
├── app.py              # Aplicación principal de Streamlit
├── vehicles_us.csv
├── notebooks/
│   └── EDA.ipynb       # Análisis exploratorio de datos
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Este archivo
```

## URL de la aplicación

🔗 [Enlace a la aplicación desplegada](#) *(pendiente de despliegue)*
