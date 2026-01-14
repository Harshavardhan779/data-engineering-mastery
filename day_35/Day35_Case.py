import duckdb

con = duckdb.connect()

con.execute("CREATE TABLE sales (product VARCHAR, amount INT)")
con.execute("""
    INSERT INTO sales VALUES 
    ('iPhone', 1000), 
    ('T-Shirt', 20), 
    ('Laptop', 1200), 
    ('Socks', 5)
""")

print("🛠️ Categorizing Sales (CASE WHEN)...")

# The Query:
# Create a new column 'Category' based on the 'amount'
query = """
    SELECT 
        product,
        amount,
        CASE 
            WHEN amount > 500 THEN 'High Value'
            WHEN amount > 50 THEN 'Medium Value'
            ELSE 'Cheap'
        END as Price_Category
    FROM sales
"""

result = con.execute(query).df()
print(result)