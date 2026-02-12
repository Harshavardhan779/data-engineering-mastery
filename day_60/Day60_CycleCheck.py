import duckdb

con = duckdb.connect()

# Create Bad Data (Circular Reference)
con.execute("CREATE TABLE employees (id INT, name VARCHAR, manager_id INT)")
con.execute("""
    INSERT INTO employees VALUES 
    (1, 'Alice', 2),   -- Alice reports to Bob
    (2, 'Bob', 1),     -- Bob reports to Alice (CYCLE!)
    (3, 'Charlie', 3)  -- Charlie reports to himself (CYCLE!)
""")

print("🛠️ Detecting Cycles in Hierarchy...")

# The Query:
# We use an array 'path' to track visited IDs.
# list_contains(path, id) checks if we've seen this person before.
query = """
    WITH RECURSIVE hierarchy AS (
        -- Anchor: Start with everyone
        SELECT 
            id, 
            name, 
            manager_id, 
            [id] as path, -- Start the path with current ID
            FALSE as is_cycle
        FROM employees
        
        UNION ALL
        
        -- Recursive: Join to manager
        SELECT 
            e.id, 
            e.name, 
            e.manager_id, 
            list_append(h.path, e.id),
            list_contains(h.path, e.id) -- Check if current ID is already in history
        FROM employees e
        JOIN hierarchy h ON e.manager_id = h.id
        WHERE NOT h.is_cycle -- Stop if we already found a cycle
    )
    SELECT * FROM hierarchy
    WHERE is_cycle = TRUE
"""

# Note: In standard SQL (Postgres), strictly detecting cycles without crashing
# usually involves an ARRAY column. DuckDB supports lists natively.
try:
    result = con.execute(query).df()
    print(result)
except Exception as e:
    print(e)