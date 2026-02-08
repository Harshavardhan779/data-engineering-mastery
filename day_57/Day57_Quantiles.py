import duckdb

con = duckdb.connect()

# Generate a sequence 1 to 1000, but scramble them slightly to simulate real data
con.execute("CREATE TABLE metrics AS SELECT (range * 2) as latency FROM range(1, 1001)")

print("🛠️ Calculating Median Latency...")

# The Query:
# quantile_cont(0.5) = Median (50th percentile)
# quantile_cont(0.95) = P95 (95% of requests are faster than this)
query = """
    SELECT 
        MIN(latency) as min_val,
        quantile_cont(latency, 0.5) as median_val,
        quantile_cont(latency, 0.95) as p95_val,
        MAX(latency) as max_val
    FROM metrics
"""

result = con.execute(query).df()
print(result)