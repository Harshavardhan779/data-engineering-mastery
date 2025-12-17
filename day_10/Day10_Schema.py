import sqlite3
import pandas as pd
connection=sqlite3.connect('retail_warehouse.db')
cursor=connection.cursor()
cursor.execute("""
               CREATE TABLE IF NOT EXISTS dim_products (
    product_key INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT
);""")
cursor.execute("""
               CREATE TABLE IF NOT EXISTS dim_customers(
                   customer_key INTEGER PRIMARY KEY,
                   customer_name TEXT,
                    region TEXT
               );""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS fact_sales (
    sale_id INTEGER PRIMARY KEY,
    product_key INTEGER,
    customer_key INTEGER,
    quantity INTEGER,
    amount REAL,
    FOREIGN KEY(product_key) REFERENCES dim_products(product_key),
    FOREIGN KEY(customer_key) REFERENCES dim_customers(customer_key)
);
""")

cursor.execute("INSERT OR IGNORE INTO dim_products VALUES(1,'Gaming LapTop','Electronics'),(2,'Office Chair','Furniture')")
cursor.execute("INSERT OR IGNORE INTO dim_customers VALUES(101,'Harsha','APAC'),(102,'John','NA')")
sales_data = [
    (1, 1, 101, 1, 2500.0), # Harsha, Laptop, $2500
    (2, 2, 102, 2, 300.0)   # John, Chairs, $300
]
cursor.executemany("INSERT OR IGNORE INTO fact_sales VALUES (?, ?, ?, ?, ?)", sales_data)
connection.commit()
query = """
SELECT 
    c.region,
    p.category,
    SUM(f.amount) as total_revenue
FROM fact_sales f
JOIN dim_customers c ON f.customer_key = c.customer_id
JOIN dim_products p ON f.product_key = p.product_key
GROUP BY c.region, p.category;
"""

print("📊 Revenue Report (Star Schema):")
print(pd.read_sql(query, connection))

connection.close()