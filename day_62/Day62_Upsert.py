import duckdb

con = duckdb.connect()

# 1. Target Table (Current State)
con.execute("CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR, email VARCHAR)")
con.execute("INSERT INTO users VALUES (1, 'Alice', 'alice@old.com'), (2, 'Bob', 'bob@old.com')")

print("BEFORE UPDATE:")
print(con.execute("SELECT * FROM users ORDER BY id").df())

# 2. Source Data (Incoming Changes)
# - Alice changed her email (UPDATE)
# - Charlie is a new user (INSERT)
con.execute("CREATE TABLE incoming_data (id INT, name VARCHAR, email VARCHAR)")
con.execute("INSERT INTO incoming_data VALUES (1, 'Alice', 'alice@new.com'), (3, 'Charlie', 'charlie@new.com')")

print("\n🛠️ Running MERGE (Upsert)...")

# The Query:
# Try to insert. If ID conflict (1), update the email. If no conflict (3), insert normally.
query = """
    INSERT INTO users 
    SELECT * FROM incoming_data
    ON CONFLICT (id) DO UPDATE 
    SET email = EXCLUDED.email
"""

con.execute(query)

print("AFTER UPDATE:")
print(con.execute("SELECT * FROM users ORDER BY id").df())