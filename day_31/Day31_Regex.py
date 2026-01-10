import duckdb

con = duckdb.connect()

# Create table with mixed text
con.execute("CREATE TABLE logs (message VARCHAR)")
con.execute("""
    INSERT INTO logs VALUES 
    ('User login: alice@gmail.com'), 
    ('Error: 404 Not Found'), 
    ('User login: bob@yahoo.co.in'), 
    ('System Reboot')
""")

print("🛠️ Extracting Pattern Matches (Regex)...")

# The Query:
# regexp_matches(col, 'pattern') checks if the pattern exists.
# Pattern: [a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+ (Basic Email Pattern)
query = """
    SELECT 
        message,
        regexp_matches(message, '[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+') as Is_Email
    FROM logs
"""

result = con.execute(query).df()
print(result)