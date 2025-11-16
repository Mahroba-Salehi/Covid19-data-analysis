import pandas as pd
import os

file_path = os.path.join("data", "raw", "owid-covid-data.csv")

# Load the data
df = pd.read_csv(file_path)

print("Sample data:")
print(df.head())

print("\nColumns:")
print(df.columns)

print("\nDataset info:")
print(df.info())
