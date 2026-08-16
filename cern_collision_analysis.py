import pandas as pd

# CERN Open Data
url = "https://opendata.cern.ch/record/700/files/MuRun2010B_0.csv"

df = pd.read_csv(url)

print(df.head())
print(df.shape)
print(df.columns)

# Dataset information
print("\n--- Dataset Information ---")
print(df.info())

# Missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Statistical summary
print("\n--- Statistical Summary ---")
print(df.describe())

# Particle type distributions
print("\n--- Particle Type 1 ---")
print(df["Type1"].value_counts())

print("\n--- Particle Type 2 ---")
print(df["Type2"].value_counts())
