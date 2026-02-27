from pydantic import BaseModel, ValidationError
from typing import Optional

# 1. Define the Data Contract
class Transaction(BaseModel):
    transaction_id: int
    amount: float
    currency: str
    is_active: bool
    notes: Optional[str] = None # Optional field

print("🛡️ Enforcing Data Contracts...")

# 2. Test with GOOD data
good_payload = {
    "transaction_id": 101,
    "amount": 250.50,
    "currency": "USD",
    "is_active": True
}

try:
    valid_record = Transaction(**good_payload)
    print("\n✅ Good Payload Accepted!")
    print(valid_record.model_dump())
except ValidationError as e:
    print(e)

# 3. Test with BAD data
bad_payload = {
    "transaction_id": "T-102",      # ERROR: String instead of Int
    "amount": "two hundred",        # ERROR: String instead of Float
    "currency": "USD",
    "is_active": "yes"              # ERROR: String instead of Boolean
}

try:
    print("\n❌ Testing Bad Payload...")
    invalid_record = Transaction(**bad_payload)
except ValidationError as e:
    print("🚨 CONTRACT VIOLATION DETECTED!")
    print(e)