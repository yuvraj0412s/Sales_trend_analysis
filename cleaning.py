import pandas as pd

df = pd.read_csv('Superstore_sales_dataset.csv')

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce', dayfirst=False)
df['ship_date'] = pd.to_datetime(df['ship_date'], errors='coerce', dayfirst=False)

df['postal_code'].fillna(method='ffill', inplace=True)  # forward fill

df.drop_duplicates(inplace=True)

df.reset_index(drop=True, inplace=True)

df.to_csv('superstore_sales_cleaned.csv', index=False)

print("✅ Data cleaned and saved as 'superstore_sales_cleaned.csv'")
