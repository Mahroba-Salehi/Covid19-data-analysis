import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = os.path.join("data", "processed", "cleaned_data.csv")

# Load cleaned data
df = pd.read_csv(file_path)
df["date"] = pd.to_datetime(df["date"])

# Filter data for Iran
country = "Iran"
country_df = df[df["location"] == country]

# Plot new cases and deaths
plt.figure(figsize=(12, 5))
plt.plot(country_df["date"], country_df["new_cases"], label="New Cases")
plt.plot(country_df["date"], country_df["new_deaths"], label="New Deaths")
plt.xlabel("Date")
plt.ylabel("Count")
plt.title(f"COVID-19 Daily Trends in {country}")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
