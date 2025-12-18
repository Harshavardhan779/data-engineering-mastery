# 📅 Day 11: SQL Indexing & Kadane's Algorithm

## 🏛️ Data Engineering: Indexing (B-Tree)
* **Problem:** Searching a database is $O(N)$ (slow) by default.
* **Solution:** Create an **Index**. This builds a B-Tree structure (like a sorted phonebook) pointing to the actual data.
* **Performance:** Reduces search from $O(N)$ to $O(\log N)$.
    * *Example:* Searching 1 million rows goes from **0.5 seconds** to **0.0001 seconds**.
* **Trade-off:** Indexes make `SELECT` fast, but `INSERT/UPDATE` slower (because the B-Tree must be updated too).

## 🧠 DSA: Kadane's Algorithm
* **Problem:** Find the contiguous subarray with the largest sum.
* **Core Logic:** "Don't carry negative baggage."
    * Iterate and add to `currentSum`.
    * Update `maxSum` if `currentSum` is high.
    * **CRITICAL STEP:** If `currentSum` drops below 0, reset it to 0. A negative prefix never helps you achieve a maximum sum.