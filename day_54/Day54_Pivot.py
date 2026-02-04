import duckdb

con = duckdb.connect()

# Create Sales table
con.execute("CREATE TABLE monthly_sales (month VARCHAR, amount INT)")
con.execute("""
    INSERT INTO monthly_sales VALUES 
    ('Jan', 100), ('Jan', 200),
    ('Feb', 50),  ('Feb', 150),
    ('Mar', 300)
""")

print("🛠️ Pivoting Data (Rows -> Columns)...")

# The Query:
# We want 'Jan', 'Feb', 'Mar' to become COLUMNS.
# Syntax: PIVOT table ON column USING aggregation
query = """
    PIVOT monthly_sales 
    ON month 
    USING SUM(amount)
"""

result = con.execute(query).df()
print(result)