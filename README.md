# AgriData Explorer – District-Level Crop Analytics in India

## Project Overview

**AgriData Explorer** is an end-to-end data analytics project aimed at understanding and visualizing the agricultural performance of Indian districts using data from ICRISAT. The project covers **data cleaning**, **exploratory data analysis**, **predictive modeling**, **SQL querying**, and **interactive dashboards in Power BI**.

---

## Dataset

**Source:** [ICRISAT - District Level Crop Data](https://www.icrisat.org)

###Dataset Includes:
- Crop-wise area cultivated, production, and yield
- Time range: multiple years (historical)
- Granularity: District-level across Indian states
- Crops covered: Rice, Wheat, Maize, Groundnut, Oilseeds, Sugarcane, Cotton, Millets, Sorghum, Soybean, Sunflower, and others

---

## Problem Statement

To build an interactive and intelligent system that helps:
- Identify top-performing districts and states by crop
- Analyze historical trends in production and yield
- Predict future production (e.g., Groundnut in 2020)
- Enable real-time data exploration via dashboards
- Recommend high-performing crops per region

---

## Tech Stack & Tools

| Tool           | Purpose                                      |
|----------------|----------------------------------------------|
| **Python (Pandas, Seaborn, Scikit-learn)** | Data Cleaning, EDA, Prediction |
| **MySQL**      | SQL querying and data modeling               |
| **Power BI**   | Interactive visualization dashboards         |
| **Jupyter Notebook** | Code documentation & analysis         |

---

## Project Workflow

### 1. Data Cleaning & Preparation (Python)
- Replaced all `-1` values with `0` to handle invalid entries
- Standardized column names (snake_case)
- Removed duplicates and missing values
- Saved as `ICRISATcleaned.csv`

### 2. Exploratory Data Analysis (EDA)
Plots created using `Matplotlib`, `Seaborn`, and `Plotly`:
- Top 5 Wheat Producing States (Bar + Pie Chart)
- Sunflower, Sugarcane, Millet, Sorghum Trends
- Crop-wise production trends over 50 years
- Yield comparison between Rice and Wheat
- Groundnut Production by State & District

### 3. SQL Analysis (MySQL)
Used a normalized SQL table (`agri_data`) inside the database `indian_agri`. Example queries:
- Top 5 districts by wheat yield increase over 5 years
- Cotton production growth by state
- Yearly rice production by top 3 states
- Groundnut production prediction for 2020 (via Python)

### 4. Predictive Modeling (Optional)
- Used `LinearRegression` from `sklearn` to predict missing 2020 groundnut production per district
- Saved predictions to `groundnut_prediction_2020.csv`

### 5. Power BI Dashboard
Key features:
- Filled Maps showing regional production
- Slicers for Year, Crop, State
- KPIs for Yield, Area, Production
- Trend Charts (line, area, column)
- Interactive comparisons (Rice vs Wheat, etc.)

---

## Key Questions Answered

1. Year-wise trend of rice production across top 3 states
2. Top 5 districts with maximum wheat yield growth
3. States with highest oilseed production growth
4. Correlation between area cultivated and production (major crops)
5. Cotton production growth in top 5 states
6. Groundnut production predicted for 2020 (via ML)
7. Average maize yield by state
8. Total oilseed area by state
9. Districts with highest rice yield
10. Comparative rice vs wheat production (Top 5 states)

---

## Power BI Visuals

- **Filled Maps** – Region-wise crop production
- **Line Charts** – Yield/production trends
- **Bar Charts** – Top producing districts/states
- **Area Charts** – Crop output over time
- **KPI Tiles** – Total Area, Production, Yield
- **Slicers** – Crop, Year, State/District

---

## Files & Structure

```bash
├── ICRISAT-District-Level-Data.csv         # Original Dataset
├── ICRISATcleaned.csv                      # Cleaned Data (Python)
├── groundnut_prediction_2020.csv           # Prediction Output
├── SQL_Queries.sql                         # SQL query file
├── powerbi_dashboard.pbix                  # Power BI Dashboard
├── eda_plots/                              # Saved charts and visuals
├── README.md                               # This file
└── notebooks/
    └── analysis_notebook.ipynb             # Jupyter analysis
