import pandas as pd

# Creating a dummy dataset
data = {
    'employee_id': [101, 102, 103, 104, 105],
    'name': ['Harsha', 'Alex', 'Sam', 'Priya', 'John'],
    'department': ['IT', 'HR', 'IT', 'Finance', 'HR'],
    'salary': [80000, 50000, 85000, 60000, 55000]
}
df = pd.DataFrame(data)
df.to_csv('employees.csv', index=False)
print("CSV Created!")

it_data=pd.read_csv('employees.csv')
it_data=it_data[it_data['department']=='IT']
print(it_data['name'])
