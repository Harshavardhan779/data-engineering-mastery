import duckdb

con = duckdb.connect()
con.execute("CREATE TABLE sales (day INT, revenue INT)")
con.execute("INSERT INTO sales VALUES (1, 10), (2, 20), (3, 30), (4, 10)")

print("🛠️ Calculating Cumulative Revenue...")

# The Query:
# SUM(revenue) OVER (ORDER BY day)
# Day 1: 10
# Day 2: 10 + 20 = 30
# Day 3: 10 + 20 + 30 = 60
query = """
    SELECT 
        day, 
        revenue,
        SUM(revenue) OVER (ORDER BY day) as running_total
    FROM sales
"""

result = con.execute(query).df()
print(result)