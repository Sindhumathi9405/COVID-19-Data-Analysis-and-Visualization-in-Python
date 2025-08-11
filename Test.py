# covid_analysis.py
# COVID-19 Data Analysis Project

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load dataset
url = "https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv"
data = pd.read_csv(url)

# Step 2: Filter for a specific country (India in this example)
country = "India"
india_data = data[data["Country"] == country]

# Step 3: Create a new column for active cases
india_data["Active"] = india_data["Confirmed"] - india_data["Recovered"] - india_data["Deaths"]

# Step 4: Display first few rows
print("First 5 records for", country)
print(india_data.head())

# Step 5: Plot confirmed cases over time
plt.figure(figsize=(10,6))
plt.plot(india_data["Date"], india_data["Confirmed"], label="Confirmed Cases", color="blue")
plt.plot(india_data["Date"], india_data["Recovered"], label="Recovered Cases", color="green")
plt.plot(india_data["Date"], india_data["Deaths"], label="Deaths", color="red")
plt.xticks(rotation=45)
plt.xlabel("Date")
plt.ylabel("Number of Cases")
plt.title(f"COVID-19 Trend in {country}")
plt.legend()
plt.tight_layout()
plt.show()

# Step 6: Save processed data to a CSV file
india_data.to_csv("india_covid_analysis.csv", index=False)
print("Processed data saved to india_covid_analysis.csv")
