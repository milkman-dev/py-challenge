import pandas as pd

filepath = r'D:\tech-challenge\py-challenge\transactions.csv'
df = pd.read_csv(filepath)

total_balance = df['amount'].sum()
df['date'] = pd.to_datetime(df['date'], format='%m/%d')
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
unique_months = df['month'].unique()

print(f'Total balance is: {total_balance}')

print(unique_months)
