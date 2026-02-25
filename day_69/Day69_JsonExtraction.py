import pandas as pd
from pandas import json_normalize

# Simulating a nested JSON payload received from a REST API
api_payload = [
    {
        "transaction_id": "T-100",
        "amount": 250.50,
        "customer": {
            "id": 1,
            "name": "Alice",
            "metadata": {
                "loyalty_tier": "Gold",
                "active": True
            }
        }
    },
    {
        "transaction_id": "T-101",
        "amount": 15.00,
        "customer": {
            "id": 2,
            "name": "Bob",
            "metadata": {
                "loyalty_tier": "Standard",
                "active": False
            }
        }
    }
]

print("📦 Raw Nested JSON:")
print(api_payload[0]) # Showing just the first record to see the nesting
print("-" * 40)

# Flatten the nested JSON structure
# sep='_' tells Pandas to use an underscore when joining nested keys (e.g., customer_metadata_loyalty_tier)
flat_df = json_normalize(api_payload, sep='_')

print("✨ Flattened Relational Table:")
print(flat_df)