import duckdb

con = duckdb.connect()

# Create Yearly Revenue Table
con.execute("CREATE TABLE revenue (year INT, amount INT)")
con.execute("""
    INSERT INTO revenue VALUES 
    (2021, 100),
    (2022, 120),
    (2023, 110),
    (2024, 150)
""")

print("🛠️ Calculating Year-Over-Year Growth (LAG)...")

# The Query:
# We use LAG to bring the previous year's amount onto the current row.
query = """
    SELECT 
        year,
        amount as Current_Rev,
        LAG(amount, 1) OVER (ORDER BY year) as Prev_Year_Rev,
        amount - LAG(amount, 1) OVER (ORDER BY year) as Growth
    FROM revenue
    ORDER BY year
"""

result = con.execute(query).df()
print(result)