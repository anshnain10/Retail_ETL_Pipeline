# 🚀 Retail ETL Pipeline Project  
### *PySpark | Hadoop HDFS | PostgreSQL | Docker | SQL Analytics*

This project demonstrates a complete end-to-end **ETL pipeline** built using **PySpark**, **Hadoop (HDFS)**, and **PostgreSQL**, all running in a **Dockerized environment**. It cleans raw retail data, stores it in a distributed file system (HDFS), and loads it into a PostgreSQL database for deriving actionable **business insights**.

> 🧠 Ideal for showcasing your **data engineering skills** and **analytical thinking** in interviews!

---

## 📚 Table of Contents
- [🧱 Architecture Overview](#-architecture-overview)
- [🛠 Tools & Technologies](#-tools--technologies)
- [📁 Project Structure](#-project-structure)
- [🔄 ETL Workflow](#-etl-workflow)
- [📊 Business Insights (SQL)](#-business-insights-sql)
- [📈 Future Enhancements](#-future-enhancements)
- [✅ Conclusion](#-conclusion)

---

## 🧱 Architecture Overview

```plaintext
Raw CSV File (local)
   │
   ├── ✅ Cleaned using PySpark (Data_cleaning.py)
   │
   ├── ⬆️ Manually uploaded to HDFS (`hdfs dfs -put`)
   │
   ├── 📂 Merged output files into one cleaned CSV
   │
   └── 🛢️ Loaded into PostgreSQL via Pandas & SQLAlchemy (conn.py)
```

---

## 🛠 Tools & Technologies

| Tool             | Purpose                            |
|------------------|-------------------------------------|
| PySpark          | Data cleaning & transformation      |
| Hadoop HDFS      | Distributed file storage            |
| PostgreSQL       | Data warehousing & analytics        |
| Pandas + SQLAlchemy | PostgreSQL integration in Python |
| Docker & Compose | Environment setup & isolation       |
| Git              | Version control                     |

---

## 📁 Project Structure

```
etl-pipeline/
├── data/
│   └── output/
│       └── cleaned_data.csv         # Final merged clean file
├── spark_scripts/
│   ├── Data_cleaning.py             # PySpark data cleaner
│   ├── conn.py                      # Upload to PostgreSQL
│   └── .env                         # DB credentials (not in Git)
├── docker/
│   └── docker-compose.yml           # Hadoop + PostgreSQL services
└── README.md                        # You're reading it :)
```

---

## 🔄 ETL Workflow

### 🔹 Step 1: Clean Data with PySpark

- Read raw CSV.
- Remove nulls, duplicates.
- Compute `TotalPrice = Quantity * UnitPrice`.
- Output saved as multiple `part-*.csv` files.

---

### 🔹 Step 2: Merge Output into Single CSV

```bash
head -n 1 part-00000-*.csv > cleaned_data.csv
tail -n +2 -q part-0000*.csv >> cleaned_data.csv
```

---

### 🔹 Step 3: Start Dockerized Environment

```bash
cd docker/
docker-compose up -d --build
```

---

### 🔹 Step 4: Upload to HDFS (Manual)

```bash
docker exec -it namenode bash
hdfs dfs -mkdir /retail
hdfs dfs -put /data/output/cleaned_data.csv /retail/
```

---

### 🔹 Step 5: Load into PostgreSQL

Update `.env`:

```env
POSTGRES_USER=retail_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=retail_db
```

Then run:

```bash
python3 spark_scripts/conn.py
```

---

## 📊 Business Insights (SQL)

✅ **Top 5 Countries by Total Sales**
```sql
SELECT "Country", ROUND(SUM("TotalPrice")::numeric, 2) AS total_sales
FROM retail_data_cleaned
GROUP BY "Country"
ORDER BY total_sales DESC
LIMIT 5;
```

✅ **Monthly Revenue Trend**
```sql
SELECT DATE_TRUNC('month', "InvoiceDate"::timestamp) AS month,
       ROUND(SUM("TotalPrice")::numeric, 2) AS monthly_revenue
FROM retail_data_cleaned
GROUP BY month
ORDER BY month;
```

✅ **Top 10 Most Sold Products**
```sql
SELECT "Description", SUM("Quantity") AS total_quantity_sold
FROM retail_data_cleaned
GROUP BY "Description"
ORDER BY total_quantity_sold DESC
LIMIT 10;
```

✅ **Top 5 Customers (Lifetime Value)**
```sql
SELECT "CustomerID", ROUND(SUM("TotalPrice")::numeric, 2) AS lifetime_value
FROM retail_data_cleaned
WHERE "CustomerID" IS NOT NULL
GROUP BY "CustomerID"
ORDER BY lifetime_value DESC
LIMIT 5;
```

✅ **Average Order Value by Country**
```sql
SELECT "Country",
       ROUND(SUM("TotalPrice")::numeric / COUNT(DISTINCT "InvoiceNo")::numeric, 2) AS avg_order_value
FROM retail_data_cleaned
GROUP BY "Country"
ORDER BY avg_order_value DESC;
```

---

## 📈 Future Enhancements

- Automate Spark → HDFS → PostgreSQL using Spark jobs
- Add Apache Airflow for orchestration
- Visualize insights using Power BI, Tableau, or Dash
- Add unit tests for ETL validation
- Add CI/CD pipelines

---

## ✅ Conclusion

This project simulates a real-world **ETL + Analytics** use case using a modern data engineering stack. It demonstrates:

✅ Hands-on experience with distributed processing  
✅ Clear understanding of data movement from raw to insights  
✅ Docker-based reproducibility  
✅ Strong SQL analytics skills



---

