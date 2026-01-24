import duckdb

con = duckdb.connect()

# Create Employees table with Manager IDs
con.execute("CREATE TABLE employees (emp_id INT, name VARCHAR, manager_id INT)")
con.execute("""
    INSERT INTO employees VALUES 
    (1, 'Alice', NULL),    -- Alice is the Boss (No manager)
    (2, 'Bob', 1),         -- Bob reports to Alice
    (3, 'Charlie', 1),     -- Charlie reports to Alice
    (4, 'David', 2)        -- David reports to Bob
""")

print("🛠️ Employee Hierarchy (SELF JOIN)...")

# The Query:
# We alias the table as 'emp' (Employee) and 'mgr' (Manager).
query = """
    SELECT 
        emp.name as Employee,
        mgr.name as Manager
    FROM employees as emp
    LEFT JOIN employees as mgr ON emp.manager_id = mgr.emp_id
    ORDER BY emp.emp_id
"""

result = con.execute(query).df()
print(result)