import pandas as pd
import os

file_path = os.path.join("data", "processed", "cleaned_data.csv")

# Load cleaned data
df = pd.read_csv(file_path)

# Define income groups by GDP per capita
income_threshold = df['gdp_per_capita'].median()
df['income_level'] = df['gdp_per_capita'].apply(lambda x: "High Income" if x > income_threshold else "Low Income")

# Calculate average death per million for each group
summary = df.groupby("income_level")['new_deaths'].mean()

print("Average new deaths per day by income level:")
print(summary)
