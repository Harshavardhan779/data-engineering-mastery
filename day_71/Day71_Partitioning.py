import pandas as pd
import numpy as np
import os

print("🛠️ Generating dummy transaction data...")

# Create dummy data spanning several months
dates = pd.date_range(start="2026-01-01", periods=6, freq='ME')
data = pd.DataFrame({
    'transaction_id': range(100, 106),
    'amount': np.random.uniform(10, 100, 6).round(2),
    'date': dates
})

# Extract year and month columns specifically for partitioning
data['year'] = data['date'].dt.year
data['month'] = data['date'].dt.month

print("\n📊 Raw Data (Notice the different months):")
print(data[['transaction_id', 'date', 'year', 'month']])
print("-" * 40)

# Save as Partitioned Parquet
output_dir = "my_data_lake"
data.to_parquet(output_dir, partition_cols=['year', 'month'], engine='pyarrow')

print("\n🗂️ Created Hive-Partitioned Data Lake Directory Structure:")
# This code just prints the folder structure so you can see what Pandas did
for root_dir, dirs, files in os.walk(output_dir):
    level = root_dir.replace(output_dir, '').count(os.sep)
    indent = ' ' * 4 * level
    folder_name = os.path.basename(root_dir)
    if folder_name:
        print(f"{indent}📁 {folder_name}/")
    for f in files:
        if f.endswith('.parquet'):
            print(f"{indent}    📄 {f[:15]}...parquet")