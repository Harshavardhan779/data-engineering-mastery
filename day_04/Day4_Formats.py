import pandas as pd
import os
# file_path = r'C:\Users\ININTR00455\Data_Engineering_Mastery\day_03\real_time_rates.csv'
df=pd.read_csv('real_time_rates.csv')
df.to_json('real_time_rates.json',orient='records',indent=4)
df.to_parquet('real_time_rates.parquet',index=False)
csv_size=os.path.getsize('real_time_rates.csv')
json_size=os.path.getsize('real_time_rates.json')
parquet_size=os.path.getsize('real_time_rates.parquet')
print("\n--- 📊 STORAGE BATTLE ---")
print(f"CSV Size:     {csv_size} bytes (Human readable, but bulky)")
print(f"JSON Size:    {json_size} bytes (Heavy due to repeated keys)")
print(f"Parquet Size: {parquet_size} bytes (Compressed & Efficient!)")
if parquet_size<csv_size:
    print("\n🏆 Parquet Wins! This is why we use it for Big Data.")