import duckdb

con = duckdb.connect()

con.execute("CREATE TABLE stocks (day INT, price INT)")
con.execute("INSERT INTO stocks VALUES (1, 100), (2, 110), (3, 120), (4, 130), (5, 90)")

print("🛠️ Calculating 3-Day Moving Average...")

# The Query:
# AVG(price) OVER (... ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)
# This looks at Today + Yesterday + Day Before Yesterday.
query = """
    SELECT 
        day, 
        price,
        AVG(price) OVER (
            ORDER BY day 
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ) as Moving_Avg
    FROM stocks
"""

result = con.execute(query).df()
print(result)