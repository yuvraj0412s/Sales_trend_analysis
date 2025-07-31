import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv('Superstore_sales_dataset.csv')

# Step 2: Clean column names (remove spaces, lowercase)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 3: Convert 'order_date' and 'ship_date' to datetime
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce', dayfirst=False)
df['ship_date'] = pd.to_datetime(df['ship_date'], errors='coerce', dayfirst=False)

# Step 4: Handle missing values in 'postal_code'
df['postal_code'].fillna(method='ffill', inplace=True)  # forward fill

# Step 5: Drop duplicates
df.drop_duplicates(inplace=True)

# Step 6: Reset index
df.reset_index(drop=True, inplace=True)

# Step 7: Save the cleaned dataset
df.to_csv('superstore_sales_cleaned.csv', index=False)

print("✅ Data cleaned and saved as 'superstore_sales_cleaned.csv'")
