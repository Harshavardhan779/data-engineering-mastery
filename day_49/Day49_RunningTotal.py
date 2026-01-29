import duckdb

con = duckdb.connect()

# Create Daily Sales Table
con.execute("CREATE TABLE sales (day INT, amount INT)")
con.execute("""
    INSERT INTO sales VALUES 
    (1, 100),
    (2, 50),
    (3, 200),
    (4, 10)
""")

print("🛠️ Calculating Running Total...")

# The Query:
# SUM(...) OVER (ORDER BY day) implies "Sum from start up to current row"
query = """
    SELECT 
        day,
        amount,
        SUM(amount) OVER (ORDER BY day) as Running_Total
    FROM sales
    ORDER BY day
"""

result = con.execute(query).df()
print(result)