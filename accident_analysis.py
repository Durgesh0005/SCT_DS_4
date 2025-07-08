# accident_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import kagglehub
from folium.plugins import HeatMap

# 1. Load the data
df = pd.read_csv("US_Accidents_Dec20.csv")

# 2. Quick EDA
print("Shape:", df.shape)
print(df.columns)
print(df[['Severity', 'Start_Time', 'Weather_Condition', 'Road_Condition', 'City']].describe())
print(df['Severity'].value_counts())

# 3. Convert time
df['Start_Time'] = pd.to_datetime(df['Start_Time'])
df['Hour'] = df['Start_Time'].dt.hour
df['Day'] = df['Start_Time'].dt.day_name()

# 4. Plot accidents by time
plt.figure(figsize=(10,6))
sns.countplot(data=df, x='Hour', palette='mako')
plt.title("Accidents by Hour of Day")
plt.savefig("output/plots/accidents_by_hour.png")
plt.close()

# 5. Weather condition impact
top_weather = df['Weather_Condition'].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_weather.values, y=top_weather.index, palette="rocket")
plt.title("Top Weather Conditions during Accidents")
plt.xlabel("Number of Accidents")
plt.savefig("output/plots/weather_conditions.png")
plt.close()

# 6. Heatmap of accident hotspots (lat/lon)
df_hotspot = df[['Start_Lat', 'Start_Lng']].dropna().sample(10000)  # sample for performance
map_ = folium.Map(location=[39.5, -98.35], zoom_start=5)
HeatMap(data=df_hotspot.values.tolist(), radius=8).add_to(map_)
map_.save("output/hotspots_map.html")

print("Analysis complete. Check the output folder for results.")

