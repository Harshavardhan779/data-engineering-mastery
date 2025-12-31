import duckdb

con = duckdb.connect()
con.execute("CREATE TABLE orders (id INT, customer VARCHAR, amount INT)")
con.execute("INSERT INTO orders VALUES (1, 'Alice', 100), (2, 'Bob', 200), (3, 'Alice', 50)")

print("🛠️ Running Query with CTE...")

# The Query:
# 1. First, calculate total spending per customer (The CTE)
# 2. Then, filter for 'VIPs' who spent > 100
query = """
    WITH customer_totals AS (
        SELECT customer, SUM(amount) as total_spent
        FROM orders
        GROUP BY customer
    )
    SELECT * FROM customer_totals 
    WHERE total_spent > 100
"""

result = con.execute(query).df()
print(result)