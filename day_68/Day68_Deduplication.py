import pandas as pd

# Create messy data with duplicates
data = {
    'transaction_id': [101, 102, 101, 103, 102],
    'user': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'],
    'status': ['Pending', 'Completed', 'Completed', 'Completed', 'Completed'],
    'timestamp': ['10:00', '10:05', '10:15', '10:20', '10:25'] # Notice the later timestamps
}
df = pd.DataFrame(data)

print("🗑️ Raw, Dirty Data:")
print(df)
print("-" * 40)

# 1. Identify Duplicates (based on transaction_id)
# keep=False means it flags ALL instances of the duplicate so we can see them
duplicates = df[df.duplicated(subset=['transaction_id'], keep=False)]
print("\n🔍 Found Duplicates:")
print(duplicates.sort_values('transaction_id'))
print("-" * 40)

# 2. Clean the Data
# We keep the 'last' entry because it has the most updated status/timestamp
clean_df = df.drop_duplicates(subset=['transaction_id'], keep='last')

print("\n✨ Cleaned Data (Most Recent Kept):")
print(clean_df.sort_values('transaction_id').reset_index(drop=True))