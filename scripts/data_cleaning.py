import pandas as pd

# بارگذاری دیتابیس
data_path = "../data/owid-covid-data.csv"
df = pd.read_csv(data_path)

# نمایش اطلاعات اولیه
print(df.info())
print(df.head())

# حذف ستون‌هایی که لازم نداریم
columns_to_keep = [
    "iso_code","continent","location","date",
    "total_cases","new_cases",
    "total_deaths","new_deaths",
    "total_tests","new_tests",
    "total_vaccinations","new_vaccinations",
    "people_vaccinated","people_fully_vaccinated",
    "population","gdp_per_capita"
]
df = df[columns_to_keep]

# تبدیل تاریخ به datetime
df['date'] = pd.to_datetime(df['date'])

# پر کردن مقادیر خالی با 0
df.fillna(0, inplace=True)

# ذخیره دیتای پاکسازی شده
df.to_csv("../data/owid_covid_cleaned.csv", index=False)
print("Data cleaning done and saved!")
