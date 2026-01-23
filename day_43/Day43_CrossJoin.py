import duckdb

con = duckdb.connect()

# Table 1: Sizes
con.execute("CREATE TABLE sizes (size VARCHAR)")
con.execute("INSERT INTO sizes VALUES ('S'), ('M'), ('L')")

# Table 2: Colors
con.execute("CREATE TABLE colors (color VARCHAR)")
con.execute("INSERT INTO colors VALUES ('Red'), ('Blue')")

print("🛠️ Generating Inventory Variants (CROSS JOIN)...")

# The Query:
# No "ON" condition. Just join them.
query = """
    SELECT 
        size,
        color
    FROM sizes
    CROSS JOIN colors
"""

result = con.execute(query).df()
print(result)