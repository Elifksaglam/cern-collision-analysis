import pandas as pd

# CERN Open Data
url = "https://opendata.cern.ch/record/700/files/MuRun2010B_0.csv"

df = pd.read_csv(url)

print(df.head())
print(df.shape)
print(df.columns)
