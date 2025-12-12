import pandas as pd
import numpy as np

# --- STEP 1: Create Dummy Data (The "Source") ---
data = {
    'EmployeeID': [101, 102, 103, 104, 105, 106],
    'Name': ['Harsha', 'Sam', 'Priya', 'Alex', 'Ria', 'John'],
    'Department': ['IT', 'Sales', 'IT', 'HR', 'Sales', 'IT'],
    'Salary': [80000, 60000, 95000, 50000, 70000, 45000],
    'Rating': [4.8, 3.5, 4.2, 4.0, 4.9, 2.5] # Scale of 1 to 5
}

df=pd.DataFrame(data)
print("Input Data")
print(df)
#2
# --- STEP 2: Define The Business Logic ---
# Logic: 
# 1. If IT and Rating > 4.5 -> 10% Bonus
# 2. If Sales and Rating > 4.0 -> 15% Bonus (Sales gets higher commission)
# 3. Everyone else -> 5% Standard Bonus
def cal_bonus(row):
    dept=row['Department']
    rate=row['Rating']
    salary=row['Salary']
    if dept=="IT" and rate>4.5:
        return salary*0.1
    elif dept=='sales' and rate>4.0:
        return salary*0.15
    else:
        return salary*0.5
print("\n⚙️ Calculating Bonuses...")    
df['Bonus']=df.apply(cal_bonus,axis=1)
df['Total_comp']=df['Bonus'] +df['Salary']  
df_spend=df.groupby('Department')['Total_comp'].sum()
print("\n--- 💰 PAYROLL REPORT ---")
print(df)

print("\n--- 📊 DEPARTMENT SPEND ---")
print(df_spend)

# Save the final report
df.to_csv('payroll_report.csv', index=False)
print("\n✅ Report generated: payroll_report.csv")  