import duckdb

con = duckdb.connect()

# Create Customers table with spending
con.execute("CREATE TABLE customers (name VARCHAR, spend INT)")
con.execute("""
    INSERT INTO customers VALUES 
    ('Alice', 1000), ('Bob', 900), ('Charlie', 800), ('David', 700),
    ('Eve', 600),    ('Frank', 500), ('Grace', 400), ('Hank', 300)
""")
# 8 Customers.

print("🛠️ Segmenting Customers into Quartiles (4 Buckets)...")

# The Query:
# Divide customers into 4 buckets based on spend (High to Low).
# Bucket 1 = High Spenders. Bucket 4 = Low Spenders.
query = """
    SELECT 
        name,
        spend,
        NTILE(4) OVER (ORDER BY spend DESC) as Quartile
    FROM customers
    ORDER BY Quartile, spend DESC
"""

result = con.execute(query).df()
print(result)