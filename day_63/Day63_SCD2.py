import duckdb

con = duckdb.connect()

# 1. Current Dimension Table (Alice is active)
con.execute("""
    CREATE TABLE users_history (
        id INT, 
        name VARCHAR, 
        email VARCHAR, 
        start_date DATE, 
        end_date DATE, 
        is_active BOOLEAN
    )
""")

# Initial State: Alice starts on Jan 1st
con.execute("""
    INSERT INTO users_history VALUES 
    (1, 'Alice', 'alice@old.com', '2023-01-01', NULL, TRUE)
""")

print("BEFORE UPDATE (Alice is active):")
print(con.execute("SELECT * FROM users_history").df())

# 2. Incoming Change (Alice changes email on Feb 1st)
con.execute("CREATE TABLE incoming (id INT, email VARCHAR, date DATE)")
con.execute("INSERT INTO incoming VALUES (1, 'alice@new.com', '2023-02-01')")

print("\n🛠️ Running SCD Type 2 Update...")

# Step A: Close the old record (Set end_date and is_active = False)
con.execute("""
    UPDATE users_history
    SET end_date = incoming.date, is_active = FALSE
    FROM incoming
    WHERE users_history.id = incoming.id 
    AND users_history.is_active = TRUE
""")

# Step B: Insert the new record (Set start_date, end_date = NULL, is_active = True)
con.execute("""
    INSERT INTO users_history
    SELECT 
        incoming.id, 
        'Alice', 
        incoming.email, 
        incoming.date, 
        NULL, 
        TRUE
    FROM incoming
""")

print("AFTER UPDATE (History Preserved):")
print(con.execute("SELECT * FROM users_history ORDER BY start_date").df())