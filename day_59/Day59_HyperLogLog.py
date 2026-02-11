import duckdb

con = duckdb.connect()

# Create a large dataset with duplicates
# Range 1..1000, repeated 5 times (Total 5000 rows, but only 1000 unique)
con.execute("CREATE TABLE clicks AS SELECT (range % 1000) + 1 as user_id FROM range(5000)")

print("🛠️ Counting Unique Users (Approx vs Exact)...")

# The Query:
# 1. Exact Count (Slow, memory heavy)
# 2. Approx Count (Fast, memory light, uses HLL)
query = """
    SELECT 
        COUNT(DISTINCT user_id) as exact_count,
        approx_count_distinct(user_id) as hll_estimate
    FROM clicks
"""

result = con.execute(query).df()
print(result)