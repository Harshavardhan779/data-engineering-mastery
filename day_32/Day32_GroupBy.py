import duckdb

con = duckdb.connect()

# Create a sales table
con.execute("CREATE TABLE sales (product VARCHAR, category VARCHAR, amount INT)")
con.execute("""
    INSERT INTO sales VALUES 
    ('iPhone', 'Electronics', 1000), 
    ('Samsung', 'Electronics', 900), 
    ('T-Shirt', 'Clothing', 20), 
    ('Jeans', 'Clothing', 50),
    ('Laptop', 'Electronics', 1200)
""")

print("🛠️ Analyzing Sales by Category...")

# The Query:
# 1. GROUP BY category -> Buckets the data (Electronics vs Clothing)
# 2. COUNT(*) -> How many items in that bucket?
# 3. SUM(amount) -> Total value of that bucket.
query = """
    SELECT 
        category,
        COUNT(*) as Items_Sold,
        SUM(amount) as Total_Revenue
    FROM sales
    GROUP BY category
    ORDER BY Total_Revenue DESC
"""

result = con.execute(query).df()
print(result)