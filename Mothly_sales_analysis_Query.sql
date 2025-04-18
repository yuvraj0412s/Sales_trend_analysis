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
