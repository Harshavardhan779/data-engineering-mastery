import sqlite3
import pandas as pd
print("🔌 Connecting to SQLite Database...")
connection=sqlite3.connect('company.db')
cursor=connection.cursor()
create_table_query = """
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
);
"""
cursor.execute(create_table_query)
print("✅ Table 'employees' created.")
employees_data = [
    (101, 'Harsha', 'Data Eng', 85000),
    (102, 'Alex', 'Data Sci', 95000),
    (103, 'Sam', 'DevOps', 75000)
]
cursor.executemany('INSERT OR IGNORE into employees VALUES(?,?,?,?)',employees_data)
connection.commit()
print(f"✅ Inserted {len(employees_data)} rows.")

print("\n📊 Reading from Database into Pandas:")
df=pd.read_sql("SELECT * from employees where salary> 80000",connection)
print(df)
connection.close()
print("\n🔌 Connection closed.")