import pandas as pd
import sqlite3
import os

# --- STEP 0: Create Mock "Messy" Data (The Source) ---
# Notice: Missing values (None), Currency symbols ('$'), and Duplicates.
messy_data = {
    'order_id': [1, 2, 3, 4, 2, 5],  # ID 2 is duplicated
    'customer': ['Harsha', 'Alice', 'Bob', None, 'Alice', 'Charlie'], # None value
    'amount': ['$1000', '$250', '$50', '$1200', '$250', '$500'], # String with '$'
    'status': ['Delivered', 'Pending', 'Cancelled', 'Delivered', 'Pending', 'Delivered']
}
df_raw = pd.DataFrame(messy_data)
df_raw.to_csv('raw_orders.csv', index=False)
print("❌ Raw CSV Created (Contains duplicates & nulls).")

# --- STEP 1: EXTRACT (Read from Source) ---
print("\n📥 Extracting data...")
df = pd.read_csv('raw_orders.csv')
print(f"   Rows extracted: {len(df)}")

# --- STEP 2: TRANSFORM (Clean the Data) ---
print("\n⚙️ Transforming data...")

# A. Remove Duplicates
df.drop_duplicates(subset=['order_id'], inplace=True)

# B. Handle Missing Values (Drop rows where customer is missing)
df.dropna(subset=['customer'], inplace=True)

# C. Clean Currency (Convert '$1000' -> 1000.0)
# We strip '$' and convert to float
df['amount'] = df['amount'].astype(str).str.replace('$', '').astype(float)

# D. Filter (Only keep High Value orders > 100)
df_clean = df[df['amount'] > 100]

print("✅ Data Cleaned.")
print(df_clean)

# --- STEP 3: LOAD (Write to Destination) ---
print("\n📤 Loading into Database...")
conn = sqlite3.connect('clean_warehouse.db')
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS high_value_orders (
    order_id INTEGER PRIMARY KEY,
    customer TEXT,
    amount REAL,
    status TEXT
)
""")

# Load dataframe to SQL
df_clean.to_sql('high_value_orders', conn, if_exists='replace', index=False)
print("✅ ETL Job Finished Successfully.")

# Verify
print("\n📊 Final Data in DB:")
print(pd.read_sql("SELECT * FROM high_value_orders", conn))
conn.close()