import sqlite3
import time
import random
import string

# 1. Setup DB
connection = sqlite3.connect('large_db.db')
cursor = connection.cursor()

# 2. Create a Table WITHOUT an Index initially
cursor.execute("DROP TABLE IF EXISTS user_logs")
cursor.execute("""
CREATE TABLE user_logs (
    log_id INTEGER PRIMARY KEY,
    username TEXT,
    action TEXT,
    timestamp INTEGER
);
""")

# 3. Insert 1 MILLION Rows (This might take 5-10 seconds)
print("⏳ Generating 1 Million rows... (Please wait)")
data = []
for i in range(1000000):
    # Random 5-letter username
    user = ''.join(random.choices(string.ascii_lowercase, k=5))
    data.append((i, user, "LOGIN", i))

cursor.executemany("INSERT INTO user_logs VALUES (?, ?, ?, ?)", data)
connection.commit()
print("✅ Data Loaded.")

# 4. The Race: Find a specific user ("abcde") WITHOUT Index
target_user = "abcde"
print(f"\n🐢 Running Search for '{target_user}' (No Index)...")

start_time = time.time()
cursor.execute("SELECT * FROM user_logs WHERE username = ?", (target_user,))
result = cursor.fetchone()
end_time = time.time()

print(f"⏱️ Time taken: {end_time - start_time:.5f} seconds")

# 5. Create an INDEX
print("\n⚡ Creating Index on 'username' column...")
cursor.execute("CREATE INDEX idx_username ON user_logs(username)")
print("✅ Index Built.")

# 6. The Race: Find same user WITH Index
print(f"\n🚀 Running Search for '{target_user}' (WITH Index)...")

start_time = time.time()
cursor.execute("SELECT * FROM user_logs WHERE username = ?", (target_user,))
result = cursor.fetchone()
end_time = time.time()

print(f"⏱️ Time taken: {end_time - start_time:.5f} seconds")

connection.close()