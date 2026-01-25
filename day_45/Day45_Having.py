"""
Day 45 - GROUP BY & HAVING

WHERE  -> filters rows BEFORE aggregation
HAVING -> filters aggregated results AFTER aggregation
"""

import sqlite3

# -----------------------------
# Setup in-memory database
# -----------------------------
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# -----------------------------
# Create table
# -----------------------------
cursor.execute("""
CREATE TABLE orders (
    order_id INTEGER,
    customer_id INTEGER,
    order_date TEXT,
    amount REAL
)
""")

# -----------------------------
# Insert sample data
# -----------------------------
orders = [
    (1, 101, "2024-01-05", 120),
    (2, 101, "2024-02-10", 250),
    (3, 102, "2024-03-12", 80),
    (4, 102, "2024-04-01", 50),
    (5, 103, "2024-05-22", 600),
    (6, 101, "2023-12-30", 200),
]

cursor.executemany(
    "INSERT INTO orders VALUES (?, ?, ?, ?)",
    orders
)

conn.commit()

# -----------------------------
# WHERE example (before math)
# -----------------------------
print("Orders from 2024 only:")
query_where = """
SELECT *
FROM orders
WHERE order_date LIKE '2024%'
"""
for row in cursor.execute(query_where):
    print(row)

# -----------------------------
# GROUP BY + HAVING example
# -----------------------------
print("\nCustomers who spent more than $300 in 2024:")

query_having = """
SELECT
    customer_id,
    SUM(amount) AS total_spent
FROM orders
WHERE order_date LIKE '2024%'      -- filter rows first
GROUP BY customer_id
HAVING total_spent > 300           -- filter aggregated results
"""

for row in cursor.execute(query_having):
    print(row)

# -----------------------------
# Cleanup
# -----------------------------
conn.close()
