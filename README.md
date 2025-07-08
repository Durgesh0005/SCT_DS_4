# 🚧 Road Accident Data Analysis – EDA & Visualization+

import kagglehub

# Download latest version
path = kagglehub.dataset_download("sobhanmoosavi/us-accidents")

print("Path to dataset files:", path)


## 🧠 Data Science Task 4 – SkillCraft Technology

This project is part of my Data Science training under **SkillCraft Technology**. The goal of this task was to explore and analyze **accident datasets** to extract key insights about accident frequency, severity, causes, and patterns based on time and location.

---

## 🎯 Objective

- Analyze trends in road/traffic accidents
- Identify peak accident times and locations
- Understand the role of weather, light, and road conditions
- Visualize data to support decision-making for traffic safety

---

## 📂 Dataset Information

- **Dataset Name**: `accidents.csv`
- **Columns Included**:
  - `Accident_Severity`
  - `Date`, `Time`
  - `Day_of_Week`
  - `Light_Conditions`, `Weather_Conditions`
  - `Road_Surface_Conditions`
  - `Speed_limit`
  - `Location_Easting_OSGR`, `Location_Northing_OSGR`

- **Source**: UK Department for Transport / Kaggle public datasets

---

## 🛠️ Tools & Libraries Used

- **Python**
- **Pandas** – data preprocessing
- **NumPy** – numeric operations
- **Matplotlib**, **Seaborn**, **Plotly** – visualizations


---

## 📊 EDA Performed

- Data inspection and cleaning
- Handling missing values and date-time conversion
- Accident frequency by:
  - Day of the week
  - Time of day (hourly trends)
  - Weather and road conditions
- Visualization using:
  - Countplots and heatmaps
  - Line and bar graphs
