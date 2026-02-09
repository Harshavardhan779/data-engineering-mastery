import duckdb

con = duckdb.connect()

# Create Users table with a single 'permissions' integer column
con.execute("CREATE TABLE users (name VARCHAR, permissions INT)")
con.execute("""
    INSERT INTO users VALUES 
    ('Alice', 7),  -- 4+2+1 (Read, Write, Delete)
    ('Bob', 3),    -- 2+1   (Read, Write)
    ('Charlie', 4) -- 4     (Delete only)
""")

print("🛠️ Finding users who can WRITE (Flag 2)...")

# The Query:
# We want to check if the '2' bit is set.
# Logic: (permissions & 2) > 0
# 7 & 2 = (111 & 010) = 010 (Result is 2, which is > 0)
# 4 & 2 = (100 & 010) = 000 (Result is 0)

query = """
    SELECT 
        name,
        permissions,
        bin(permissions) as binary_value,
        CASE WHEN (permissions & 2) > 0 THEN 'YES' ELSE 'NO' END as can_write
    FROM users
"""

result = con.execute(query).df()
print(result)