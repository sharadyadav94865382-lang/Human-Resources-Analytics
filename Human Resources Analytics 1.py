import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Seed for consistency
np.random.seed(42)
num_rows = 300

departments = ['IT Engineering', 'Sales', 'Marketing', 'Human Resources', 'Finance']
ratings = ['Unsatisfactory', 'Needs Improvement', 'Meets Expectations', 'Exceeds Expectations']

data = {
    'Employee_ID': [f"EMP{str(i).zfill(3)}" for i in range(1, num_rows + 1)],
    'Name': [f"Employee {i}" for i in range(1, num_rows + 1)],
    'Department': np.random.choice(departments, num_rows, p=[0.35, 0.25, 0.15, 0.10, 0.15]),
    'Hire_Date': [datetime(2023, 1, 1) + timedelta(days=int(np.random.randint(0, 1100))) for _ in range(num_rows)],
    'Status': np.random.choice(['Active', 'Terminated'], num_rows, p=[0.80, 0.20]),
    'Satisfaction_Score': np.random.randint(1, 6, num_rows),
    'Performance_Rating': np.random.choice(ratings, num_rows, p=[0.10, 0.15, 0.55, 0.20]),
    'Monthly_Salary': np.random.randint(35000, 150000, num_rows)
}

df = pd.DataFrame(data)

# Ensuring Termination Date is only for Terminated employees
df['Termination_Date'] = df.apply(
    lambda r: r['Hire_Date'] + timedelta(days=int(np.random.randint(90, 365))) 
    if r['Status'] == 'Terminated' else None, 
    axis=1
)

df.to_csv('HR_Analytics_Data.csv', index=False)
print("--> 'HR_Analytics_Data.csv' successfully created!")