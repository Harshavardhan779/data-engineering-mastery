import duckdb

con = duckdb.connect()

con.execute("CREATE TABLE orders (order_id INT, items JSON)")
con.execute("""
    INSERT INTO orders VALUES 
    (101, '["Milk", "Bread", "Eggs"]'),
    (102, '["Laptop", "Mouse"]')
""")

print("🛠️ Exploding JSON Arrays into Rows...")

# FIXED QUERY:
# We use '::VARCHAR[]' to tell DuckDB: 
# "Convert this JSON blob into a List of Strings, THEN Unnest it."
query = """
    SELECT 
        order_id,
        UNNEST(items::VARCHAR[]) as Single_Item
    FROM orders
"""

result = con.execute(query).df()
print(result)