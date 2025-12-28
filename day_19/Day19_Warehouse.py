import duckdb
import pandas as pd
import time
import os  # <--- This was missing!

# 0. Setup: Create a dummy large CSV if it doesn't exist
# csv_file = "sales_data.csv"
# if not os.path.exists(csv_file):
    # ... rest of the code remains the same

# 0. Setup: Create a dummy large CSV if it doesn't exist
csv_file = "sales_data.csv"
if not os.path.exists(csv_file):
    print("⚙️ Generating dummy data...")
    # Create a simple dataframe with 100,000 rows
    df = pd.DataFrame({
        'id': range(100000),
        'category': ['Electronics', 'Clothing', 'Home'] * 33333 + ['Home'],
        'amount': [100, 50, 200, 20] * 25000
    })
    df.to_csv(csv_file, index=False)
    print("✅ Dummy data created.")

# 1. The Power of DuckDB
# We don't "load" the data. We query the FILE directly.
print("\n🦆 Running Analytical Query with DuckDB...")

start_time = time.time()

# SQL Query: Group By Category and Sum Amount
# Notice we select from the filename string!
query = """
    SELECT 
        category, 
        SUM(amount) as total_revenue, 
        COUNT(*) as transaction_count,
        AVG(amount) as avg_ticket
    FROM 'sales_data.csv' 
    GROUP BY category 
    ORDER BY total_revenue DESC
"""

result = duckdb.query(query).to_df()
end_time = time.time()

print(f"⏱️ Time Taken: {end_time - start_time:.4f} seconds")
print("\n📊 Warehouse Report:")
print(result)

# 2. Export result to Parquet (The Gold Standard format for Big Data)
# Parquet is compressed and much faster than CSV.
duckdb.query("COPY (SELECT * FROM 'sales_data.csv') TO 'sales_data.parquet' (FORMAT PARQUET)")
print("\n💾 Data converted to Parquet format (Optimized Storage).")