import duckdb

con = duckdb.connect()
# Create dummy employee data
con.execute("CREATE TABLE employees (name VARCHAR, dept VARCHAR, salary INT)")
con.execute("INSERT INTO employees VALUES ('Alice', 'HR', 5000), ('Bob', 'HR', 4000), ('Charlie', 'IT', 6000), ('Dave', 'IT', 7000)")

print("🛠️ Ranking Employees by Salary (Window Function)...")

# The Query:
# RANK() OVER (PARTITION BY dept ORDER BY salary DESC)
# "For each department, rank them by salary highest to lowest"
query = """
    SELECT 
        name, 
        dept, 
        salary,
        RANK() OVER (PARTITION BY dept ORDER BY salary DESC) as rank_in_dept
    FROM employees
"""

result = con.execute(query).df()
print(result)