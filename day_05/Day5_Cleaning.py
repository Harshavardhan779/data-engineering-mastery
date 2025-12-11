import pandas as pd
import numpy as np # Standard library for numerical operations

# --- STEP 1: Create Dirty Data ---
print("🗑️ Generating Messy Data...")
data = {
    'customer_id': [101, 102, 103, 104, 102, 105], # Duplicate 102
    'name': ['Harsha', 'Alex', np.nan, 'Priya', 'Alex', 'Sam'], # Missing Name
    'age': [25, 30, 22, np.nan, 30, 28], # Missing Age
    'city': ['Hyd', 'Bangalore', 'Hyd', 'Chennai', 'Bangalore', None], # Missing City
    'purchase_amount': [1000, 2500, None, 500, 2500, 1200] # Missing & Duplicate Amount
}
df = pd.DataFrame(data)

print("\n--- 🛑 DIRTY DATA SNAPSHOT ---")
print(df)
print("\n--- 🔍 MISSING VALUES COUNT ---")
print(df.isnull().sum()) # Like SQL: SELECT COUNT(*) WHERE col IS NULL

# --- STEP 2: The Cleaning Process ---

# 1. Remove Duplicates (Rows that are exactly the same)
# SQL: SELECT DISTINCT *
df_clean = df.drop_duplicates()
print(f"\n✅ Removed Duplicates. Rows reduced from {len(df)} to {len(df_clean)}")

# 2. Handle Missing Numeric Data (Fill with Mean/Average)
# SQL: NVL(age, AVG(age))
mean_age = df_clean['age'].mean()
df_clean['age'] = df_clean['age'].fillna(mean_age)
print(f"✅ Filled missing Age with mean: {mean_age:.1f}")

# 3. Handle Missing Categorical Data (Fill with 'Unknown')
# SQL: NVL(name, 'Unknown')
df_clean['name'] = df_clean['name'].fillna("Unknown")
df_clean['city'] = df_clean['city'].fillna("Unknown")
print("✅ Filled missing Name/City with 'Unknown'")

# 4. Drop rows where critical data is missing (e.g., purchase_amount)
# SQL: DELETE FROM table WHERE purchase_amount IS NULL
df_final = df_clean.dropna(subset=['purchase_amount'])
print("✅ Dropped rows with no purchase amount")

# --- STEP 3: Save Clean Data ---
print("\n--- ✨ CLEAN DATA SNAPSHOT ---")
print(df_final)
df_final.to_csv('cleaned_customers.csv', index=False)