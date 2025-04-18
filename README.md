# 📆 Monthly Sales Analysis (Task 6) - SQL

This project focuses on generating a **monthly sales summary** using **MySQL**. The goal is to calculate **total revenue** and **total orders** for each month between **January 2003 and December 2004**.

## 🛠️ Task Overview

Using the `orders` table, we analyze:
- Monthly total revenue
- Number of distinct orders per month

## 🔍 SQL Query Used

```sql
SELECT 
    DATE_FORMAT(order_date, '%Y-%m') AS month_year,
    SUM(amount) AS total_revenue,
    COUNT(DISTINCT order_id) AS total_orders
FROM 
    orders
WHERE
    order_date BETWEEN '2003-01-01' AND '2004-12-31'
GROUP BY 
    DATE_FORMAT(order_date, '%Y-%m')
ORDER BY 
    DATE_FORMAT(order_date, '%Y-%m');
