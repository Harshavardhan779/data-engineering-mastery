import duckdb

con = duckdb.connect()

# Create messy data: inconsistent case, extra spaces
con.execute("CREATE TABLE users (id INT, email VARCHAR)")
con.execute("INSERT INTO users VALUES (1, '  JOhn.Doe@Gmail.com '), (2, 'alice@yahoo.COM')")

print("🛠️ Cleaning Messy Emails...")

# The Query:
# 1. TRIM removes the spaces around John's email.
# 2. LOWER converts everything to lowercase.
# 3. SPLIT_PART extracts the domain (everything after @).
query = """
    SELECT 
        email as Original,
        LOWER(TRIM(email)) as Cleaned_Email,
        SPLIT_PART(email, '@', 2) as Domain_Only
    FROM users
"""

result = con.execute(query).df()
print(result)