import duckdb

con = duckdb.connect()

# Create Employees table (ID, Name, ManagerID)
con.execute("CREATE TABLE employees (id INT, name VARCHAR, manager_id INT)")
con.execute("""
    INSERT INTO employees VALUES 
    (1, 'Alice', NULL),   -- CEO
    (2, 'Bob', 1),        -- Reports to Alice
    (3, 'Charlie', 2),    -- Reports to Bob
    (4, 'David', 3)       -- Reports to Charlie
""")

print("🛠️ Generating Management Hierarchy Path (Recursive CTE)...")

# The Query:
# We want to build a "Path" string: Alice -> Bob -> Charlie -> David
query = """
    WITH RECURSIVE org_chart AS (
        -- 1. Anchor: Find the Boss (No manager)
        SELECT 
            id, 
            name, 
            manager_id, 
            name as path_trace,
            1 as level
        FROM employees
        WHERE manager_id IS NULL
        
        UNION ALL
        
        -- 2. Recursive Step: Join employees to their managers in 'org_chart'
        SELECT 
            e.id, 
            e.name, 
            e.manager_id, 
            o.path_trace || ' -> ' || e.name,
            o.level + 1
        FROM employees e
        JOIN org_chart o ON e.manager_id = o.id
    )
    SELECT path_trace, level FROM org_chart
    ORDER BY level
"""

result = con.execute(query).df()
print(result)