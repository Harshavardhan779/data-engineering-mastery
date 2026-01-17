import duckdb

con = duckdb.connect()

# Create two tables with one overlapping row ('B')
con.execute("CREATE TABLE list_A (item VARCHAR)")
con.execute("INSERT INTO list_A VALUES ('A'), ('B')")

con.execute("CREATE TABLE list_B (item VARCHAR)")
con.execute("INSERT INTO list_B VALUES ('B'), ('C')")

print("--- UNION ALL (Keeps Duplicates) ---")
print(con.execute("SELECT * FROM list_A UNION ALL SELECT * FROM list_B").df())

print("\n--- UNION (Removes Duplicates) ---")
print(con.execute("SELECT * FROM list_A UNION SELECT * FROM list_B").df())