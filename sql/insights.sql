Insight 1: Top 5 Countries by Total Sales

SELECT "Country", ROUND(SUM("TotalPrice")::numeric, 2) AS total_sales
FROM retail_data_cleaned
GROUP BY "Country"
ORDER BY total_sales DESC
LIMIT 5;

Insight 2: Monthly Revenue Trend

SELECT DATE_TRUNC('month', "InvoiceDate"::timestamp) AS month,
       ROUND(SUM("TotalPrice")::numeric, 2) AS monthly_revenue
FROM retail_data_cleaned
GROUP BY month
ORDER BY month;

Insight 3: Top 10 Most Sold Products

SELECT "Description", SUM("Quantity") AS total_quantity_sold
FROM retail_data_cleaned
GROUP BY "Description"
ORDER BY total_quantity_sold DESC
LIMIT 10;

Insight 4: Customer Lifetime Value (Top 5 Customers)

SELECT "CustomerID", ROUND(SUM("TotalPrice")::numeric, 2) AS lifetime_value
FROM retail_data_cleaned
WHERE "CustomerID" IS NOT NULL
GROUP BY "CustomerID"
ORDER BY lifetime_value DESC
LIMIT 5;

Insight 5: Average Order Value by Country

SELECT "Country",
       ROUND(SUM("TotalPrice")::numeric / COUNT(DISTINCT "InvoiceNo")::numeric, 2) AS avg_order_value
FROM retail_data_cleaned
GROUP BY "Country"
ORDER BY avg_order_value DESC;
