# 🚗 Car Sales Listings Analysis

Interactive web application to explore and visualize data from used vehicle sales listings in the United States.

## Description

This application allows users to analyze a vehicle dataset through interactive visualizations. It includes:

- **Mileage histogram:** Shows the odometer distribution of listed vehicles.
- **Scatter plot:** Visualizes the relationship between mileage and vehicle price.

## Technologies Used

- **Python 3**
- **Streamlit** - Framework for building data web applications
- **Pandas** - Data manipulation and analysis
- **Plotly Express** - Interactive visualizations

## How to Run the Application Locally

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd 3T_proyecto_s7
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

5. Open your browser at `http://localhost:8501`

## Project Structure

```
3T_proyecto_s7/
├── app.py              # Main Streamlit application
├── vehicles_us.csv
├── notebooks/
│   └── EDA.ipynb       # Exploratory data analysis
├── requirements.txt    # Project dependencies
└── README.md           # This file
```

## Application URL

🔗 [https://threet-proyecto-s7.onrender.com](#)
