import duckdb

con = duckdb.connect()

# Generate a large dataset (Sequence 1 to 100)
con.execute("CREATE TABLE big_data AS SELECT range AS id FROM range(1, 101)")

print("🛠️ Extracting a 5% Sample...")

# The Query:
# We want roughly 5 random rows from the 100 rows.
# 'USING SAMPLE' is much faster than 'ORDER BY RANDOM()' for huge data.
query = """
    SELECT * FROM big_data 
    USING SAMPLE 5 PERCENT (bernoulli)
"""

result = con.execute(query).df()
print(result)