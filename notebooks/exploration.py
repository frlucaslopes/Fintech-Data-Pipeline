import pandas as pd

df = pd.read_csv("data/processed/daily_metrics.csv")

print(df.head())
print(df.info())
print(df.describe())