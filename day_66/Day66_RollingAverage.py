import pandas as pd

# Create daily sales data with massive spikes (noise)
data = {
    'day': range(1, 8),
    'sales': [10, 50, 20, 100, 30, 40, 90]
}
df = pd.DataFrame(data)

print("📊 Raw Daily Sales (Spiky & Noisy):")
print(df)
print("-" * 40)

# Calculate a 3-day rolling average
# window=3 means look at the current row + previous 2 rows
# min_periods=1 means calculate an average even for day 1 and 2 where we don't have 3 full days yet
df['3_day_moving_avg'] = df['sales'].rolling(window=3, min_periods=1).mean().round(2)

print("📈 Smoothed Sales Data (Trend):")
print(df)