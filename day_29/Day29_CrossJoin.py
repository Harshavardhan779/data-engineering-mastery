import duckdb

con = duckdb.connect()

# Create two small tables
con.execute("CREATE TABLE sizes (size VARCHAR)")
con.execute("INSERT INTO sizes VALUES ('S'), ('M'), ('L')")

con.execute("CREATE TABLE colors (color VARCHAR)")
con.execute("INSERT INTO colors VALUES ('Red'), ('Blue')")

print("🛠️ Generating All Possible Products (Cross Join)...")

# The Query:
# No "ON" condition. Just comma-separated tables.!
query = """
    SELECT 
        s.size, 
        c.color 
    FROM sizes s, colors c
"""

result = con.execute(query).df()
print(result)