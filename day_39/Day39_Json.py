import duckdb

con = duckdb.connect()

# Create a table with a raw JSON column (simulating an API response)
con.execute("CREATE TABLE api_logs (id INT, response JSON)")
con.execute("""
    INSERT INTO api_logs VALUES 
    (1, '{"user": {"name": "Alice", "id": 101}, "status": "active"}'),
    (2, '{"user": {"name": "Bob", "id": 102}, "status": "inactive"}')
""")

print("🛠️ Extracting Nested JSON Data...")

# The Query:
# We use the '->>' operator (or json_extract_string) to dig into the structure.
# 'response -> user -> name' means "Go to response, get user, get name".
query = """
    SELECT 
        id,
        response->'$.user.name' as User_Name,
        response->'$.status' as Status
    FROM api_logs
"""

result = con.execute(query).df()
print(result)