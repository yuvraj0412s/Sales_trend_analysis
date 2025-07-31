# 📊 Sales Trend Analysis Using SQL & Python

![Python](https://img.shields.io/badge/Python-Data%20Cleaning-yellow?style=flat-square)
![SQL](https://img.shields.io/badge/SQL-Aggregation-blue?style=flat-square)
![Pandas](https://img.shields.io/badge/Pandas-Used-brightgreen?style=flat-square)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

> A real-world data project where I cleaned and transformed a sales dataset using Python, and performed time-based trend analysis using SQL — revealing insights on monthly revenue and order volume.

---

## 🧠 Objective

To explore trends in monthly sales and order volume using **SQL-based aggregation**, supported by **Python-powered data cleaning**.

---

## 🚀 What I Did

✅ Cleaned the raw CSV using Python  
✅ Transformed messy data into SQL-friendly format  
✅ Wrote a SQL script to analyze sales and order trends  
✅ Exported final cleaned dataset ready for dashboards or reports

---

## 🛠️ Skillset Demonstrated

| Category           | Skills / Tools                            |
|--------------------|-------------------------------------------|
| 👨‍💻 Programming    | Python, Pandas                            |
| 🗄️ Database Querying | SQL (MySQL, SQLite compatible)           |
| 🧹 Data Cleaning    | Column renaming, date parsing, null handling |
| 📊 Analysis         | Time-based aggregation (revenue, orders) |
| 📁 File Handling    | CSV import/export                         |

---

## 📝 Dataset Overview

- **Input File:** `Sample_sales.csv`
- **Output File:** `cleaned_sales_for_mysql.csv`
- **Important Fields:** `order_id`, `order_date`, `amount`, `product_id`

---

## 🧹 Data Cleaning Steps (Python)

```python
import pandas as pd

# Load dataset
df = pd.read_csv("Sample_sales.csv", encoding="latin1")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Convert order_date to datetime
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

# Select and rename relevant columns
clean_df = df[['ordernumber', 'order_date', 'sales', 'productcode']].copy()
clean_df.columns = ['order_id', 'order_date', 'amount', 'product_id']

# Drop rows with missing values
clean_df.dropna(inplace=True)

# Save the cleaned data for SQL import
clean_df.to_csv("cleaned_sales_for_mysql.csv", index=False)
