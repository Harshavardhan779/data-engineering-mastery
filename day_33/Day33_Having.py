import duckdb

con = duckdb.connect()

# Same table as yesterday
con.execute("CREATE TABLE sales (product VARCHAR, category VARCHAR, amount INT)")
con.execute("""
    INSERT INTO sales VALUES 
    ('iPhone', 'Electronics', 1000), 
    ('Samsung', 'Electronics', 900), 
    ('T-Shirt', 'Clothing', 20), 
    ('Jeans', 'Clothing', 50),
    ('Laptop', 'Electronics', 1200)
""")

print("🛠️ High Value Categories (Revenue > 1000)...")

# The Query:
# We only want to see categories where the SUM(amount) is HUGE.
# We cannot use WHERE for this. We must use HAVING.
query = """
    SELECT 
        category,
        SUM(amount) as Total_Revenue
    FROM sales
    GROUP BY category
    HAVING SUM(amount) > 1000
"""

result = con.execute(query).df()
print(result)