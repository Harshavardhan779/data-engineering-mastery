# 📅 Day 10: Star Schema & The Dutch National Flag

## 🏛️ Data Engineering: Star Schema
* **What is it?** The standard modeling technique for Data Warehouses (OLAP).
* **Fact Table:** The central table containing metrics (Revenue, Quantity) and Foreign Keys. It grows very fast (Millions of rows).
* **Dimension Table:** The lookup tables containing descriptive attributes (Product Name, Region). Small and slow-changing.
* **Why use it?** It optimizes query performance by reducing the complexity of Joins compared to a fully normalized (3NF) database.

## 🧠 DSA: Striver Mediums

### 1. Sort Colors (Dutch National Flag)
* **Problem:** Sort array of 0, 1, 2 in $O(N)$ time and $O(1)$ space.
* **Logic:** "Three Pointers"
    * `[0 ... low-1]`: Region of 0s
    * `[low ... high]`: Region of 1s (and unknown)
    * `[high+1 ... end]`: Region of 2s
* **Key Move:** If we find a `0`, swap it to `low` and expand the 0-zone. If we find a `2`, swap it to `high` and expand the 2-zone.

### 2. Two Sum
* **Logic:** Use a Hash Map to store "values we have seen so far".
* **Formula:** `Complement = Target - Current`. If Complement is in the Map, we found the pair.
* **Complexity:** Time $O(N)$, Space $O(N)$.