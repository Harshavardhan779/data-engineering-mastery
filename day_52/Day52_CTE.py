import duckdb

con = duckdb.connect()

# Create Sales table
con.execute("CREATE TABLE sales (region VARCHAR, amount INT)")
con.execute("""
    INSERT INTO sales VALUES 
    ('North', 100), ('North', 200),
    ('South', 50),  ('South', 50),
    ('West', 300),  ('West', 100),
    ('East', 50)
""")

print("🛠️ Finding Top Region using CTE...")

# The Query:
# Step 1: regional_totals (Calculate sum per region)
# Step 2: Select from that temporary result
query = """
    WITH regional_totals AS (
        SELECT 
            region,
            SUM(amount) as total_sales
        FROM sales
        GROUP BY region
    ),
    ranked_regions AS (
        SELECT
            region,
            total_sales,
            RANK() OVER (ORDER BY total_sales DESC) as rnk
        FROM regional_totals
    )
    SELECT * FROM ranked_regions
    WHERE rnk = 1
"""

result = con.execute(query).df()
print(result)