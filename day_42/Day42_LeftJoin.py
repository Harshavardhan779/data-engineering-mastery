import duckdb

con = duckdb.connect()

# Table 1: Customers
con.execute("CREATE TABLE customers (id INT, name VARCHAR)")
con.execute("INSERT INTO customers VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Charlie')")

# Table 2: Orders (Charlie is missing here)
con.execute("CREATE TABLE orders (order_id INT, cust_id INT, amount INT)")
con.execute("INSERT INTO orders VALUES (101, 1, 500), (102, 2, 300)")

print("🛠️ All Customers Report (LEFT JOIN)...")

# The Query:
# We want a report of ALL customers, even if they spent $0.
# We use COALESCE(amount, 0) to turn NULLs into 0.
query = """
    SELECT 
        customers.name,
        orders.order_id,
        COALESCE(orders.amount, 0) as Amount_Spent
    FROM customers
    LEFT JOIN orders ON customers.id = orders.cust_id
    ORDER BY customers.id
"""

result = con.execute(query).df()
print(result)