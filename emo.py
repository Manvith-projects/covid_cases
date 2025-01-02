import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# URL of the CSV file from Our World in Data
url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'

# Load data into a pandas dataframe
try:
    df = pd.read_csv(url)
except Exception as e:
    print(f"Error loading data: {e}")
    exit(1)

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Filter data for the country
country = 'United States'
country_data = df[df['location'] == country]

# Group by weekly data
weekly_cases = country_data.resample('W', on='date').sum().reset_index()

# Plotting
plt.style.use('ggplot')
plt.figure(figsize=(12, 6))
sns.lineplot(x='date', y='new_cases', data=weekly_cases)
plt.title(f'New COVID-19 Cases in {country}')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('new_cases.png')
plt.close()

# Analysis
print("Analysis completed, plot saved as 'new_cases.png'\n")

# Basic statistics
print("Basic Statistics:")
print(weekly_cases['new_cases'].describe())

# Week with maximum cases
max_week = weekly_cases.loc[weekly_cases['new_cases'].idxmax()]
print("\nWeek with the highest number of cases:")
print(f"Date: {max_week['date'].strftime('%Y-%m-%d')}")
print(f"New Cases: {max_week['new_cases']:.0f}")
