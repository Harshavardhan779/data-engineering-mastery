import duckdb

con = duckdb.connect()

# Create Stock Prices table
con.execute("CREATE TABLE stocks (day INT, price INT)")
con.execute("""
    INSERT INTO stocks VALUES 
    (1, 100),
    (2, 110),
    (3, 105),  -- Dip
    (4, 115),
    (5, 120)
""")

print("🛠️ Calculating 3-Day Moving Average...")

# The Query:
# Calculate the average of the current row + the 2 previous rows.
query = """
    SELECT 
        day,
        price,
        AVG(price) OVER (
            ORDER BY day 
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ) as Moving_Avg_3Day
    FROM stocks
    ORDER BY day
"""

result = con.execute(query).df()
print(result)