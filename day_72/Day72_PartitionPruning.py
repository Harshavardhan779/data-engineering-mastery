import duckdb

print("🔍 Querying the Partitioned Data Lake...")

# The Query:
# 1. We read ALL parquet files in the directory using '**/*.parquet'
# 2. hive_partitioning=1 tells DuckDB to read the folder names as actual columns!
# 3. WHERE month = 2 tells DuckDB to PRUNE (ignore) all the other month folders.
query = """
    SELECT 
        transaction_id, 
        date, 
        amount, 
        year, 
        month
    FROM read_parquet('my_data_lake/**/*.parquet', hive_partitioning=1)
    WHERE year = 2026 AND month = 2
"""

# Execute the query and convert to a Pandas DataFrame for clean printing
try:
    result = duckdb.query(query).df()
    print("\n📊 Results for February 2026 (Pruned Query):")
    print(result)
    print("-" * 40)
    print("Notice how 'year' and 'month' appear as columns, even though they weren't saved INSIDE the Parquet file. They were extracted from the folder path!")
except duckdb.IOException:
    print("\n❌ Error: Could not find 'my_data_lake'. Make sure you are running this in the same folder where you ran Day 71's code!")