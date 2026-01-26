import duckdb

con = duckdb.connect()

# Create Scores table
con.execute("CREATE TABLE scores (student VARCHAR, score INT)")
con.execute("""
    INSERT INTO scores VALUES 
    ('Alice', 95), 
    ('Bob', 95), 
    ('Charlie', 90), 
    ('David', 85)
""")

print("🛠️ Calculating Ranks (Window Functions)...")

# The Query:
# We assign a rank based on score descending.
# Notice: No GROUP BY is needed.
query = """
    SELECT 
        student,
        score,
        RANK() OVER (ORDER BY score DESC) as Rank_Num,
        DENSE_RANK() OVER (ORDER BY score DESC) as Dense_Rank_Num
    FROM scores
    ORDER BY score DESC
"""

result = con.execute(query).df()
print(result)