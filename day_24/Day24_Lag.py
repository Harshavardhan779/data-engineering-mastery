import duckdb

con = duckdb.connect()
con.execute("CREATE TABLE sales (day INT, revenue INT)")
con.execute("INSERT INTO sales VALUES (1, 100), (2, 120), (3, 110), (4, 150)")

print("🛠️ Calculating Daily Growth (LAG Function)...")

# The Query:
# LAG(revenue) gets the revenue from the PREVIOUS row.
query = """
    SELECT 
        day, 
        revenue,
        LAG(revenue) OVER (ORDER BY day) as prev_revenue,
        revenue - LAG(revenue) OVER (ORDER BY day) as growth
    FROM sales
"""

result = con.execute(query).df()
print(result)