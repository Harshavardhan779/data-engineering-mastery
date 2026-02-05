import duckdb

con = duckdb.connect()

# Create a "Wide" table (like an Excel sheet)
con.execute("CREATE TABLE wide_sales (product VARCHAR, Jan INT, Feb INT, Mar INT)")
con.execute("INSERT INTO wide_sales VALUES ('Widget', 100, 200, 300)")

print("INPUT (Wide):")
print(con.execute("SELECT * FROM wide_sales").df())

print("\n🛠️ UNPIVOTING (Columns -> Rows)...")

# The Query:
# Turn Jan, Feb, Mar columns into rows.
query = """
    UNPIVOT wide_sales
    ON Jan, Feb, Mar
    INTO
        NAME month    -- The column name for the headers
        VALUE amount  -- The column name for the values
"""

result = con.execute(query).df()
print(result)