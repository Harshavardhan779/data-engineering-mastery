import pandas as pd
import numpy as np
import os

print("🛠️ Generating 1,000,000 rows of dummy data...")

# Create a large DataFrame
data = {
    'id': np.arange(1000000),
    'category': np.random.choice(['A', 'B', 'C', 'D'], size=1000000),
    'value': np.random.randn(1000000)
}
df = pd.DataFrame(data)

# 1. Save as CSV
csv_filename = "data_day70.csv"
df.to_csv(csv_filename, index=False)
csv_size_mb = os.path.getsize(csv_filename) / (1024 * 1024)

# 2. Save as Parquet
parquet_filename = "data_day70.parquet"
df.to_parquet(parquet_filename, engine='pyarrow', index=False)
parquet_size_mb = os.path.getsize(parquet_filename) / (1024 * 1024)

print("\n📊 Storage Comparison:")
print(f"CSV Size:     {csv_size_mb:.2f} MB")
print(f"Parquet Size: {parquet_size_mb:.2f} MB")
print(f"Space Saved:  {((csv_size_mb - parquet_size_mb) / csv_size_mb) * 100:.2f}%")

# Clean up files so we don't clog your hard drive
os.remove(csv_filename)
os.remove(parquet_filename)