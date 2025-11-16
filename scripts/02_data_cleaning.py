import pandas as pd
import os

input_path = os.path.join("data", "raw", "owid-covid-data.csv")
output_path = os.path.join("data", "processed", "cleaned_data.csv")

df = pd.read_csv(input_path)

# Select relevant columns
columns_needed = [
    "iso_code", "continent", "location", "date",
    "new_cases", "new_deaths", "new_tests",
    "people_vaccinated", "people_fully_vaccinated",
    "population", "gdp_per_capita"
]
df = df[columns_needed]

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Drop non-country data (like World or regions)
df = df[df["iso_code"].str.len() == 3]

# Fill missing numeric values with 0
numeric_cols = ["new_cases", "new_deaths", "new_tests", "people_vaccinated", "people_fully_vaccinated"]
df[numeric_cols] = df[numeric_cols].fillna(0)

# Drop rows missing continent & population
df = df.dropna(subset=["continent", "population"])

# Save cleaned data
df.to_csv(output_path, index=False)
print("Cleaned data saved to:", output_path)
