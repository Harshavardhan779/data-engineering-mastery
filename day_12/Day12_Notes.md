# 📅 Day 12: NoSQL & Next Permutation

## 📦 Data Engineering: NoSQL (JSON)
* **Concept:** "Not Only SQL". Used when data structure is not known in advance or changes often.
* **Format:** JSON (JavaScript Object Notation). Key-Value pairs.
* **Benefit:** * **Flexibility:** You can add a new field (`experience_years`) to one record without updating the whole database schema.
    * **Nesting:** You can store arrays (`skills`) directly in the record. No need for complex JOINs.

## 🧠 DSA: Next Permutation Algorithm
* **Problem:** Find the next lexicographically greater arrangement of numbers.
* **Logic (The 3 Steps):**
    1.  **Find the Pivot:** Look from the back for the first dip (`nums[i] < nums[i+1]`). This is where the change must happen.
    2.  **Find Successor:** Look from the back for the smallest number *larger* than the pivot. Swap them.
    3.  **Minimize Suffix:** Reverse the array to the right of the pivot. This converts the suffix from Descending (Max) to Ascending (Min), giving the smallest possible "next" value.
* **Complexity:** Time: $O(N)$ (One pass), Space: $O(1)$.