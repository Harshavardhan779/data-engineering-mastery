import duckdb

con = duckdb.connect()

# Create Employees table with Departments
con.execute("CREATE TABLE employees (name VARCHAR, dept VARCHAR, salary INT)")
con.execute("""
    INSERT INTO employees VALUES 
    ('Alice', 'Engineering', 120000),
    ('Bob', 'Engineering', 100000),
    ('Charlie', 'Sales', 95000),
    ('David', 'Sales', 150000)
""")

print("🛠️ Ranking Employees PER Department...")

# The Query:
# Rank salaries high-to-low, but RESTART the ranking for each department.
query = """
    SELECT 
        dept,
        name,
        salary,
        RANK() OVER (PARTITION BY dept ORDER BY salary DESC) as Dept_Rank
    FROM employees
    ORDER BY dept, Dept_Rank
"""

result = con.execute(query).df()
print(result)