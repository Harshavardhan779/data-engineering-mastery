import duckdb

con = duckdb.connect()

# Create Monthly Revenue table
con.execute("CREATE TABLE revenue (month VARCHAR, amount INT)")
con.execute("""
    INSERT INTO revenue VALUES 
    ('Jan', 1000),
    ('Feb', 1200),
    ('Mar', 1500),
    ('Apr', 1300)
""")

print("🛠️ Calculating Month-over-Month Growth...")

# The Query:
# LAG(amount) gets the previous month's amount.
# Growth = Current - Previous
query = """
    SELECT 
        month,
        amount as current_revenue,
        LAG(amount, 1) OVER (ORDER BY month) as prev_revenue,
        amount - LAG(amount, 1) OVER (ORDER BY month) as growth_amount
    FROM revenue
"""

result = con.execute(query).df()
print(result)