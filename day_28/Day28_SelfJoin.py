import duckdb

con = duckdb.connect()

# 1. Setup: Create a single table with a hierarchy
# Joe (id 1) reports to Sam (id 3).
# Henry (id 2) reports to Max (id 4).
# Sam and Max are bosses (Manager ID is NULL).
con.execute("CREATE TABLE employees (id INT, name VARCHAR, salary INT, manager_id INT)")
con.execute("""
    INSERT INTO employees VALUES 
    (1, 'Joe', 70000, 3), 
    (2, 'Henry', 80000, 4), 
    (3, 'Sam', 60000, NULL), 
    (4, 'Max', 90000, NULL)
""")

print("🛠️ Analyzing Hierarchy: Who earns more than their boss?")

# 2. The Logic: Join the table to ITSELF
# We treat one copy as 'Worker' (e) and one copy as 'Boss' (m)
query = """
    SELECT 
        e.name AS Worker,
        e.salary AS Worker_Salary,
        m.name AS Manager,
        m.salary AS Manager_Salary
    FROM employees e
    JOIN employees m 
      ON e.manager_id = m.id
    WHERE e.salary > m.salary
"""

result = con.execute(query).df()
print(result)