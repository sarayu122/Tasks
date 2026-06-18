axi Demand Optimization Project (NYC Dataset)


📌 Problem Statement
Analyze NYC taxi trip data to identify demand patterns across time and locations, and help optimize:
🚖 Driver availability
⏰ Peak hour planning
💰 Revenue optimization
📍 Demand hotspots


📊 Project Workflow
This project is divided into 3 main stages:
1. Raw Data (NYC Taxi CSV)
        ↓
2. Data Cleaning + Feature Engineering (clean_data.py)
        ↓
3. Visualization + Insights (visualization.py)
        ↓
4. Processed Dataset (processed_data/)
🧹 1. Data Cleaning & Feature Engineering
📄 File: clean_data.py


✔ Steps performed:
📌 Data Loading
Loaded only required columns for efficiency
Used sampling (500,000 rows) for faster processing
📌 Data Cleaning
Removed missing values
Converted datetime columns
Filtered invalid records:
fare_amount > 0
trip_distance > 0
total_amount > 0
📌 Outlier Removal
Removed extreme values using 99th percentile filtering
📌 GPS Validation
Ensured valid latitude and longitude ranges
📌 Feature Engineering


Created new features:
⏱ trip_duration (in minutes)
🕒 hour of trip
📅 weekday
📆 day
🧭 time_slot (Morning Peak / Evening Peak / Normal)
🚗 speed_kmph
📌 Data Filtering
Removed unrealistic trip durations (>300 min or <1 min)
Removed unrealistic speeds (>100 km/h)


📌 Final Processing
Removed duplicates
Sorted data by pickup time
Performed time-based train-test split (80/20)


💾 Output Files
Generated inside processed_data/:
processed_data/
│
├── cleaned_data.csv   → Final cleaned dataset
├── train.csv          → Training dataset
├── test.csv           → Testing dataset


📊 2. Visualization & Insights

📄 File: visualization.py
📈 Visualizations Created
1️⃣ Taxi Demand by Hour
Shows hourly ride distribution
Identifies peak demand hours
📊 Graph Type: Line Chart

2️⃣ Taxi Demand by Time Slot
Morning Peak vs Evening Peak vs Normal
📊 Graph Type: Bar Chart

3️⃣ Taxi Demand by Weekday
Identifies busiest days of the week
📊 Graph Type: Bar Chart

4️⃣ Trip Distance Distribution
Shows how most trips are short distance
📊 Graph Type: Histogram

5️⃣ Fare Distribution by Time Slot
Shows fare variation across different time periods
Helps understand revenue patterns
📊 Graph Type: Box Plot

🧠 Key Insights
✔ Peak demand occurs during:
Morning (7–10 AM)
Evening (5–9 PM)
✔ Weekdays show higher demand than weekends
✔ Most trips are short distance (0–5 km)
✔ Evening trips often have higher fare variation
✔ Taxi demand is highly time-dependent


🤖 Technologies Used
Python 🐍
Pandas 📊
Matplotlib 📈
Scikit-learn 🤖
Jupyter / VS Code 💻


🚀 How to Run
1️⃣ Install dependencies
pip install pandas matplotlib scikit-learn
2️⃣ Run data cleaning
python clean_data.py
3️⃣ Run visualizations
python visualization.py


📁 Project Structure
Taxi-Demand-Optimization/
│
├── taxi.csv
├── clean_data.py
├── visualization.py
│
├── processed_data/
│   ├── cleaned_data.csv
│   ├── train.csv
│   ├── test.csv
│
└── README.md


💡 Future Improvements
📍 Geo heatmap of pickup locations
🤖 ML model to predict taxi demand per hour
📊 Streamlit dashboard for live analytics
🚖 Surge pricing prediction system


🏆 Project Goal Achieved
This project successfully transforms raw NYC taxi data into:
✔ Clean dataset
✔ Feature-rich dataset
✔ Business insights
✔ Visual analytics
✔ ML-ready data split