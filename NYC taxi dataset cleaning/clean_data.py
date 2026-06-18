import os
import pandas as pd
from sklearn.model_selection import train_test_split

# -----LOAD DATA-----

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, "taxi.csv")
cols = [
    'fare_amount',
    'trip_distance',
    'tpep_pickup_datetime',
    'tpep_dropoff_datetime',
    'pickup_latitude',
    'pickup_longitude',
    'dropoff_latitude',
    'dropoff_longitude',
    'total_amount'
]
df = pd.read_csv(file_path, usecols=cols, low_memory=False) #low_memory=False to avoid converting dataset to form chuncks to reduce memory
# work on sample for speed
df = df.sample(500000, random_state=42)

# -----BASIC CLEANING-----
#drop nan values in these columns
df = df.dropna(subset=[
    'fare_amount',
    'trip_distance',
    'tpep_pickup_datetime',
    'tpep_dropoff_datetime'
])

# Convert datetimes from string format
df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'], errors='coerce') # coerce will convert invalid values to NaT
df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'], errors='coerce')

# Drop rows where datetime conversion is failed
df = df.dropna(subset=['tpep_pickup_datetime', 'tpep_dropoff_datetime'])

# -----REMOVE INVALID VALUES-----

df = df[
    (df['fare_amount'] > 0) &
    (df['trip_distance'] > 0) &
    (df['total_amount'] > 0)
]

# -----OUTLIER REMOVAL (99th percentile)

df = df[df['trip_distance'] < df['trip_distance'].quantile(0.99)]
df = df[df['fare_amount'] < df['fare_amount'].quantile(0.99)]
df = df[df['total_amount'] < df['total_amount'].quantile(0.99)]

# -----VALID GPS FILTERING-----

df = df[
    (df['pickup_latitude'].between(-90, 90)) &
    (df['pickup_longitude'].between(-180, 180)) &
    (df['dropoff_latitude'].between(-90, 90)) &
    (df['dropoff_longitude'].between(-180, 180))
]

# -----FEATURE ENGINEERING STEPS-----

df['trip_duration'] = (
    df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime'] # if we subtract these we get timedelta object not a fixed number
).dt.total_seconds() / 60

# Remove invalid durations
df = df[(df['trip_duration'] > 1) & (df['trip_duration'] < 300)] # 5 hours is too long and 1 minute is too short for a taxi ride

df['hour'] = df['tpep_pickup_datetime'].dt.hour
df['weekday'] = df['tpep_pickup_datetime'].dt.day_name()
df['day'] = df['tpep_pickup_datetime'].dt.day

# Time slot feature
def time_slot(hour):
    if 7 <= hour <= 10:
        return "Morning Peak"
    elif 17 <= hour <= 21:
        return "Evening Peak"
    else:
        return "Normal"

df['time_slot'] = df['hour'].apply(time_slot) # this is caled binning, we convert hours to time slots

# -----7. SPEED FEATURE-----

df['speed_kmph'] = df['trip_distance'] / (df['trip_duration'] / 60) # it converts minutes to hours

# Remove unrealistic speeds
df = df[df['speed_kmph'] < 100] # keeping 100 as threshold because in some cases taxi can go very fast on highways, but we want to remove outliers that are due to data errors

# -----8. REMOVE DUPLICATES-----
df = df.drop_duplicates()
df = df.reset_index(drop=True)

# -----9. SPLIT DATA-----

# train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
# Taxi dataset is Time sensitive
df = df.sort_values('tpep_pickup_datetime') # sorting by pickup times helps to create split between past rides vs future rides
split_index = int(len(df) * 0.8) # we take 80 % of sorted data for training and remaining to testing
train_df = df.iloc[:split_index] 
test_df = df.iloc[split_index:]

# -----10. SAVE DATA-----
output_dir = os.path.join(BASE_DIR, "processed_data")
os.makedirs(output_dir, exist_ok=True)

train_df.to_csv(os.path.join(output_dir, "train.csv"), index=False)
test_df.to_csv(os.path.join(output_dir, "test.csv"), index=False)
df.to_csv(os.path.join(output_dir, "cleaned_data.csv"), index=False)

print("Files saved successfully") # save data to use this cleaned data again

# find peak taxi demand hours
# print(df['hour'].value_counts().sort_index().plot(kind='bar'))
# # find which days of week have more taxi rides
# print(df['weekday'].value_counts().plot(kind='bar'))
# # find which time slot has more taxi rides
# print(df['time_slot'].value_counts().plot(kind='bar'))
# # find distribution of trip durations
# print(df['trip_duration'].hist(bins=50))
# # find relationship between trip distance and fare amount
# print(df.plot.scatter(x='trip_distance', y='fare_amount'))