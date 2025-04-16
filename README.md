# 🛍️ Sales Trend Analysis Using SQL

This project is part of a data analysis task focused on understanding **monthly revenue and order volume trends** from an e-commerce dataset. We used **MySQL** to write a query that aggregates sales by month and year.

---

## 📊 Task Objective

Perform a **Sales Trend Analysis** using SQL:
- Analyze **monthly revenue** (`SUM(sales)`)
- Analyze **monthly order volume** (`COUNT(DISTINCT order_id)`)

---

## 🧰 Tools Used

- SQL (MySQL Workbench)
- Dataset: `jewelry_cleaned.csv`

---

## 📝 SQL Query Overview

sql
SELECT
    YEAR(STR_TO_DATE(order_date, '%Y-%m-%d')) AS year,
    MONTH(STR_TO_DATE(order_date, '%Y-%m-%d')) AS month,
    SUM(amount) AS total_revenue,
    COUNT(DISTINCT order_id) AS total_orders
FROM
    jewelry_cleaned
GROUP BY
    YEAR(STR_TO_DATE(order_date, '%Y-%m-%d')),
    MONTH(STR_TO_DATE(order_date, '%Y-%m-%d'))
ORDER BY
    year, month
LIMIT 12;
