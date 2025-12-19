import json
import os

# File acting as our "NoSQL Database"
DB_FILE = "user_store.json"

# 1. The Data: Nested, Flexible Structure (Impossible in 1 SQL row)
# Notice "skills" is a list, and "address" is a nested object.
users_data = [
    {
        "id": 101,
        "name": "Harsha",
        "role": "Data Engineer",
        "skills": ["Python", "SQL", "Java"],
        "address": {
            "city": "Hyderabad",
            "zip": "500081"
        },
        "active": True
    },
    {
        "id": 102,
        "name": "Alice",
        "role": "Data Scientist",
        "skills": ["R", "Python", "Tableau"],
        # Alice doesn't have an address. In SQL this would be NULL. In NoSQL, it just doesn't exist.
        "active": False
    }
]

# 2. WRITE: Dump data to JSON (Simulation of MongoDB Insert)
print("💾 Saving data to NoSQL Store...")
with open(DB_FILE, 'w') as f:
    json.dump(users_data, f, indent=4)
print("✅ Data Saved.")

# 3. READ & QUERY: Find all users who know 'Python'
print("\n🔍 Querying: Find users with 'Python' skill...")

with open(DB_FILE, 'r') as f:
    data = json.load(f)

python_devs = []
for user in data:
    # NoSQL Query Logic: Check inside the list
    if "Python" in user.get("skills", []):
        python_devs.append(user["name"])

print(f"🐍 Python Developers: {python_devs}")

# 4. UPDATE: Add a new field 'experience' to Harsha only
print("\n🔄 Updating: Adding field to Harsha...")
for user in data:
    if user["id"] == 101:
        user["experience_years"] = 3  # Flexible Schema! Alice won't have this.

# Print final structure of Harsha to show flexibility
print(json.dumps(data[0], indent=2))