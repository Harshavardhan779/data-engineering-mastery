import pandas as pd
import requests
import json

API_URL = "https://jsonplaceholder.typicode.com/users"

def fetch_url():
    print(f'--Connecting to the the url{API_URL}....')
    response = requests.get(API_URL, verify=False)
    if response.status_code==200:
      print("✅ Connection Successful! Data received.") 
      return response.json()
    else:
        print(f"❌ Failed. Status Code: {response.status_code}")
        return []
user_json=fetch_url()
if user_json:
    print(f"Extracted the {len(user_json)}")
    
    clean_data = []
    for user in user_json:
        clean_data.append({
            "id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "city": user["address"]["city"],
            "company": user["company"]["name"]
        })    
        
df = pd.DataFrame(clean_data)
print("\n📊 First 5 Rows of Live Data:")
print(df.head())
    
 
df.to_csv("api_users.csv", index=False)
print("\n💾 Saved to 'api_users.csv'")        