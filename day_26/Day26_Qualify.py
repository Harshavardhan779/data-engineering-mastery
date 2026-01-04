import duckdb

con = duckdb.connect()
con.execute("CREATE TABLE products (category VARCHAR, item VARCHAR, sales INT)")
con.execute("INSERT INTO products VALUES ('Phone', 'iPhone', 1000), ('Phone', 'Pixel', 800), ('Laptop', 'Mac', 2000), ('Laptop', 'Dell', 1500)")

print("🛠️ Finding Top Product per Category (QUALIFY)...")

# The Query:
# Find the #1 selling product in each category instantly.
# No CTEs needed!
query = """
    SELECT 
        category, 
        item, 
        sales,
        RANK() OVER (PARTITION BY category ORDER BY sales DESC) as rank
    FROM products
    QUALIFY rank = 1
"""

result = con.execute(query).df()
print(result)