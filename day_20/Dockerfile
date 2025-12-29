# 1. Use Python 3.9 as the base system
FROM python:3.9-slim

# 2. Create a folder for our code
WORKDIR /app

# 3. Copy our scripts into that folder
COPY . /app

# 4. Install the libraries we need
RUN pip install pandas duckdb

# 5. The command to run when the container starts
CMD ["python", "Day19_Warehouse.py"]