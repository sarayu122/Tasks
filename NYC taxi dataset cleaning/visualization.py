import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("processed_data/cleaned_data.csv")

# Taxi Demand by Hour
hour_counts = data['hour'].value_counts().sort_index()
plt.figure(figsize=(10,5))
plt.plot(hour_counts.index, hour_counts.values, marker='o')
plt.title("Taxi Demand Trend by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Trips")
plt.xticks(range(0,24))
plt.grid(True)
plt.show()

# Taxi Demand by Time Slot
slot_counts = data['time_slot'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(slot_counts.index, slot_counts.values)
plt.title("Taxi Demand by Time Slot")
plt.xlabel("Time Slot")
plt.ylabel("Number of Trips")
plt.show()

# Taxi Demand by Weekday
weekday_counts = data['weekday'].value_counts()
order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
weekday_counts = weekday_counts.reindex(order)
plt.figure(figsize=(8,5))
plt.bar(weekday_counts.index, weekday_counts.values)
plt.title("Taxi Demand by Weekday")
plt.xlabel("Day")
plt.ylabel("Number of Trips")
plt.xticks(rotation=45)
plt.show()

# Top Trip Distances
plt.figure(figsize=(10,5))
plt.hist(data['trip_distance'], bins=50)
plt.title("Trip Distance Distribution")
plt.xlabel("Distance (km)")
plt.ylabel("Number of Trips")
plt.grid(True)
plt.show()

# Average Fare by Time Slot
data = [
    data[data['time_slot'] == 'Morning Peak']['fare_amount'],
    data[data['time_slot'] == 'Evening Peak']['fare_amount'],
    data[data['time_slot'] == 'Normal']['fare_amount']
]
plt.figure(figsize=(8,5))
plt.boxplot(data, labels=['Morning', 'Evening', 'Normal'])
plt.title("Fare Distribution by Time Slot")
plt.ylabel("Fare Amount")
plt.show()

