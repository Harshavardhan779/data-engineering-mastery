import sqlite3
import pandas as pd

# --- STEP 1: Setup Database ---
connection = sqlite3.connect('company_v2.db')
cursor = connection.cursor()

# Enable Foreign Keys support in SQLite
cursor.execute("PRAGMA foreign_keys = ON;")

# --- STEP 2: Create Tables (Schema Design) ---
# Table 1: Departments
cursor.execute("""
CREATE TABLE IF NOT EXISTS departments (
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT
);
""")

# Table 2: Employees (Linked to Dept via Foreign Key)
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    salary INTEGER,
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES departments (dept_id)
);
""")

# --- STEP 3: Insert Mock Data ---
# Clear old data to prevent duplicates when re-running
cursor.execute("DELETE FROM employees;")
cursor.execute("DELETE FROM departments;")

# Insert Departments
depts = [(1, 'Engineering'), (2, 'HR'), (3, 'Sales')]
cursor.executemany("INSERT INTO departments VALUES (?, ?)", depts)

# Insert Employees
emps = [
    (101, 'Harsha', 120000, 1), # Eng
    (102, 'Sam', 60000, 2),     # HR
    (103, 'Alex', 110000, 1),   # Eng
    (104, 'Ria', 75000, 3)      # Sales
]
cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", emps)
connection.commit()

# --- STEP 4: The "Money Query" (JOIN + AGGREGATION) ---
# Question: "Calculate the average salary for each department."
query = """
SELECT 
    d.dept_name,
    COUNT(e.emp_id) as emp_count,
    AVG(e.salary) as avg_salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name
ORDER BY avg_salary DESC;
"""

print("📊 Department Performance Report:")
df_report = pd.read_sql(query, connection)
print(df_report)

connection.close()