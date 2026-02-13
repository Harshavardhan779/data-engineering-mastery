import duckdb

con = duckdb.connect()

# Create two tables representing user lists
con.execute("CREATE TABLE users_jan (id INT, name VARCHAR)")
con.execute("CREATE TABLE users_feb (id INT, name VARCHAR)")

con.execute("INSERT INTO users_jan VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Charlie')")
con.execute("INSERT INTO users_feb VALUES (1, 'Alice'), (3, 'Charlie'), (4, 'David')")

print("Jan Users: Alice, Bob, Charlie")
print("Feb Users: Alice, Charlie, David")
print("\n🛠️ Finding Retained Users (INTERSECT)...")

# Query 1: Who is in BOTH lists?
query_intersect = """
    SELECT * FROM users_jan
    INTERSECT
    SELECT * FROM users_feb
"""
print(con.execute(query_intersect).df())

print("\n🛠️ Finding Churned Users (EXCEPT)...")

# Query 2: Who was in Jan but NOT in Feb?
query_except = """
    SELECT * FROM users_jan
    EXCEPT
    SELECT * FROM users_feb
"""
print(con.execute(query_except).df())