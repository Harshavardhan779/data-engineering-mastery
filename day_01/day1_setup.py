import pandas as pd

# 1. Create a simple dataset (like INSERT INTO...)
data = {
    'employee_id': [101, 102, 103],
    'name': ['Harsha', 'Alex', 'Sam'],
    'role': ['Data Engineer', 'Data Analyst', 'Manager']
}

# 2. Load into a DataFrame (like creating a TABLE)
df = pd.DataFrame(data)

# 3. Display it (like SELECT * FROM...)
print("--- My First Data Engineering Frame ---")
print(df)