import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.linear_model import LinearRegression

data = pd.read_csv("E:/GUVI/Project 2/ICRISAT-District Level Data - ICRISAT-District Level Data.csv")

data.columns = data.columns.str.strip().str.replace(" ", "_").str.lower()

data = data.replace(-1, 0)

predictions = []

for district, group in data.groupby('dist_name'):
    if group['year'].nunique() >= 5:
        X = group['year'].values.reshape(-1, 1)
        y = group['groundnut_production_(1000_tons)'].values
        model = LinearRegression().fit(X, y)
        pred_2020 = model.predict([[2020]])[0]
        predictions.append((district, pred_2020))

pred_df = pd.DataFrame(predictions, columns=['dist_name', 'predicted_groundnut_production_2020'])

data = pd.merge(data, pred_df, on='dist_name', how='left')

output_path = "E:/GUVI/Project 2/ICRISATcleaned.csv"
data.to_csv(output_path, index=False)

print("✅ Predicted column added to full dataset.")
print("📁 File saved at:", output_path)
