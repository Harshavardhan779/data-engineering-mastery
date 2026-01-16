import duckdb

con = duckdb.connect()

# Create a table with missing phone numbers
con.execute("CREATE TABLE users (name VARCHAR, phone VARCHAR)")
con.execute("""
    INSERT INTO users VALUES 
    ('Alice', '555-0100'), 
    ('Bob', NULL), 
    ('Charlie', '555-0199'), 
    ('David', NULL)
""")

print("🛠️ Fixing Missing Data (COALESCE)...")

# The Query:
# If phone is NULL, replace it with 'Not Provided'.
query = """
    SELECT 
        name,
        COALESCE(phone, 'Not Provided') as Clean_Phone
    FROM users
"""

result = con.execute(query).df()
print(result)