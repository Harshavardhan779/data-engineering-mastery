import duckdb

con = duckdb.connect()

# List A: The Candidates
con.execute("CREATE TABLE candidates (name VARCHAR)")
con.execute("INSERT INTO candidates VALUES ('Alice'), ('Bob'), ('Charlie')")

# List B: The Hires
con.execute("CREATE TABLE hires (name VARCHAR)")
con.execute("INSERT INTO hires VALUES ('Bob'), ('Charlie'), ('David')")

print("--- INTERSECT (Who was a candidate AND got hired?) ---")
print(con.execute("SELECT name FROM candidates INTERSECT SELECT name FROM hires").df())

print("\n--- EXCEPT (Who was a candidate but was NOT hired?) ---")
print(con.execute("SELECT name FROM candidates EXCEPT SELECT name FROM hires").df())