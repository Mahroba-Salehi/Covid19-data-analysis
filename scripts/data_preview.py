import pandas as pd

file_path = "Data/raw/owid-covid-data.csv"

df = pd.read_csv(file_path)

print("simple data:")
print(df.head(10))

print("\nDataset info:")
print(df.info())
