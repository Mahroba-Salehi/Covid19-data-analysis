import pandas as pd
import os

file_path = os.path.join("data", "processed", "cleaned_data.csv")

# Load dataset
df = pd.read_csv(file_path)

# Calculate correlation matrix
corr_matrix = df[["new_cases", "new_deaths", "new_tests", "people_vaccinated"]].corr()

print("Correlation matrix:")
print(corr_matrix)
