import duckdb

# Create a connection (in-memory)
con = duckdb.connect()

# 1. Create dummy data
con.execute("CREATE TABLE sales (id INTEGER, category VARCHAR, amount INTEGER)")
con.execute("INSERT INTO sales VALUES (1, 'Tech', 100), (2, 'Tech', 50), (3, 'Home', 200)")

# 2. CREATE VIEW: Save the complex logic as 'category_summary'
print("🛠️ Creating View...")
con.execute("""
    CREATE VIEW category_summary AS 
    SELECT category, SUM(amount) as total 
    FROM sales 
    GROUP BY category
""")

# 3. Query the View (Simple!)
print("📊 Querying the View:")
result = con.execute("SELECT * FROM category_summary").df()
print(result)