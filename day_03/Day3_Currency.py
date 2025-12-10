import requests
import pandas as pd
from datetime import datetime

api_url="https://open.er-api.com/v6/latest/USD"
print("📡 Connecting to API...")
# verify=False tells Python to trust the connection even if the certificate looks weird
response = requests.get(api_url, verify=False)
if response.status_code==200:
    print("Connection establihed Successfully")
    data=response.json()
    rates_dict=data['rates']
    df=pd.DataFrame(list(rates_dict.items()),columns=['currency','rates'])
    df['load_timestamp']=datetime.now()
    print('Preview of data')
    print(df.head())
    df.to_csv('real_time_rates.csv',index=False)
    print("data saved to the real_time_csv_file")
else:
    print(f"Got error in connection{response.status_code}")    
    

    