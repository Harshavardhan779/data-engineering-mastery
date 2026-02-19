import pandas as pd

# Create a DataFrame of scores with a tie for 1st place
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'score': [100, 100, 90, 85]
}
df = pd.DataFrame(data)

print("🏆 The Leaderboard Base Data:")
print(df)
print("-" * 40)

# Apply the three different types of ranking
# ascending=False means highest score gets rank 1
df['row_number'] = df['score'].rank(method='first', ascending=False).astype(int)
df['rank'] = df['score'].rank(method='min', ascending=False).astype(int)
df['dense_rank'] = df['score'].rank(method='dense', ascending=False).astype(int)

# Sort by score just to make it clean
df = df.sort_values(by='score', ascending=False)

print("📊 Ranking Results:")
print(df)