# 📅 Day 9: Striver Arrays (Easy) & SQL Joins

## 🧠 Data Structures & Algorithms (Striver Step 3.1)

### 1. Rotate Array (LeetCode #189)
* **Goal:** Rotate array to the right by `k` steps.
* **Optimal Algorithm:** **Reversal Algorithm**.
    1. Reverse first `n-k` elements.
    2. Reverse last `k` elements.
    3. Reverse the entire array.
* **Time:** $O(N)$ | **Space:** $O(1)$.

### 2. Missing Number (LeetCode #268)
* **Goal:** Find the missing number in range `[0, n]`.
* **Optimal Algorithm:** **Summation Formula**.
    * `Expected Sum = n * (n + 1) / 2`
    * `Missing = Expected Sum - Actual Sum`
* **Time:** $O(N)$ | **Space:** $O(1)$.

## 🏗️ Data Engineering: Complex SQL
* **Concept:** Performing Joins and Aggregations in Python.
* **Key Query Pattern:**
    ```sql
    SELECT d.dept_name, AVG(e.salary) 
    FROM employees e 
    JOIN departments d ON e.dept_id = d.dept_id 
    GROUP BY d.dept_name;
    ```
* **Why:** This mimics the daily work of a DE: joining raw data tables to create analytical reports.

## 🏛️ Data Engineering: Relational Logic

### 1. The JOIN Operation
* **Purpose:** Combines rows from two or more tables based on a related column.
* **Why split tables?** To reduce redundancy (Normalization). We store `dept_name` in one place and reference it via `dept_id` (Foreign Key).
* **Our Query:** `INNER JOIN` (Only returns rows where there is a match in *both* tables).

### 2. Aggregation (GROUP BY)
* **Purpose:** Condenses many rows into a single summary row.
* **Process:**
    1.  **Split:** Data is divided into groups based on the key (e.g., `dept_name`).
    2.  **Apply:** A function (Count, Sum, Avg) is applied to each group.
    3.  **Combine:** The results are returned as a new table.
* **Key Insight:** You cannot select a raw column (like `employee_name`) if you are grouping by `dept_name`—because which employee name would the DB pick? You can only select the *Group Key* or an *Aggregate Function*.