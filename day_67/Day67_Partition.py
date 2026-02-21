import pandas as pd

# Create Employee Data
data = {
    'emp_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'department': ['Engineering', 'Engineering', 'Sales', 'Sales', 'Sales'],
    'salary': [120000, 90000, 60000, 80000, 70000]
}
df = pd.DataFrame(data)

print("🏢 Original Employee Data:")
print(df)
print("-" * 40)

# Calculate the Department Average and broadcast it to every row
df['dept_avg_salary'] = df.groupby('department')['salary'].transform('mean')

# Calculate the difference so we can see who is above/below average
df['difference_from_avg'] = df['salary'] - df['dept_avg_salary']

print("📊 Data with Partitioned Window Averages:")
print(df)