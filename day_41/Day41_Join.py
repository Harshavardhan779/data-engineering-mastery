import duckdb

con = duckdb.connect()

# Table 1: Customers
con.execute("CREATE TABLE customers (id INT, name VARCHAR)")
con.execute("INSERT INTO customers VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Charlie')")

# Table 2: Orders (Bob and Alice bought stuff, Charlie did not)
con.execute("CREATE TABLE orders (order_id INT, cust_id INT, amount INT)")
con.execute("INSERT INTO orders VALUES (101, 1, 500), (102, 2, 300), (103, 1, 200)")

print("🛠️ Merging Customers & Orders (INNER JOIN)...")

# The Query:
# We only want to see customers who actually placed an order.
query = """
    SELECT 
        customers.name,
        orders.order_id,
        orders.amount
    FROM customers
    JOIN orders ON customers.id = orders.cust_id
"""

result = con.execute(query).df()
print(result)