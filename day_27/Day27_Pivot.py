import duckdb

con = duckdb.connect()
con.execute("CREATE TABLE sales (year INT, month VARCHAR, revenue INT)")
con.execute("INSERT INTO sales VALUES (2024, 'Jan', 100), (2024, 'Jan', 150), (2024, 'Feb', 200), (2024, 'Feb', 250)")

print("🛠️ Pivoting Rows to Columns...")

# The Query:
# Turn 'month' values into columns.
# Sum the 'revenue' for each cell.
query = """
    PIVOT sales 
    ON month 
    USING SUM(revenue) 
    GROUP BY year
"""

result = con.execute(query).df()
print(result)