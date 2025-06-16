import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

data = pd.read_csv("E:/GUVI/Project 2/ICRISAT-District Level Data - ICRISAT-District Level Data.csv")

# print(data.head())
# print(data.info())
# pd.set_option('display.max_rows', None)
# print(data.isnull().sum())

data.columns = data.columns.str.strip().str.replace(" ", "_").str.lower()

data = data.replace(-1, 0)

