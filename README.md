COVID-19 Data Analysis and Visualization in Python
📌 Project Overview
This project performs data analysis and visualization on COVID-19 case data using Python.
It demonstrates the ability to fetch real-world datasets, process them with Pandas, and visualize trends using Matplotlib.

The project focuses on India’s COVID-19 statistics — confirmed cases, recoveries, and deaths — and calculates active cases for each date.

📂 Features
Load COVID-19 dataset from a public GitHub repository.

Filter data for a specific country (India in this example).

Calculate active cases using the formula:

ini
Copy
Edit
Active = Confirmed - Recovered - Deaths
Visualize trends in confirmed, recovered, and death counts.

Save processed data to a CSV file.

🛠 Technologies Used
Python 3

Pandas – Data loading and preprocessing.

Matplotlib – Data visualization.

▶️ How to Run
Install Python 3.x on your system.

Install required libraries:

bash
Copy
Edit
pip install pandas matplotlib
Download the covid_analysis.py file.

Run the script:

bash
Copy
Edit
python covid_analysis.py
📊 Output
Terminal Output: First 5 rows of processed India COVID-19 data.

Graph: Line plot showing trends in confirmed, recovered, and death counts.

CSV File: india_covid_analysis.csv containing processed data.

📈 Skills Demonstrated
Data collection from public sources.

Data preprocessing and cleaning.

Working with time-series data.

Data visualization for insights.

📌 Author
Developed as a demonstration of Python skills in data analysis and visualization.

