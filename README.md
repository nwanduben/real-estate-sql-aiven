##  Project Summary: Real Estate Market Analytics (2001–2022)

### Overview
This project analyzes over 1 million property sales across Connecticut (2001–2022) using PostgreSQL and Python.  
The goal is to uncover pricing trends, regional patterns, and correlations between assessed and actual market values.

### Key Insights
- **Top Luxury Markets:** Greenwich, New Canaan, and Darien lead with average property prices above \$1.6M.  
-  **Market Trends:** Sales volume declined sharply post-2008, indicating the housing bubble impact.  
-  **Value Correlation:** A moderate correlation (0.52) between assessed and sale values reveals price variability across regions.  
-  **Property Types:** Residential and condominium properties dominate sales activity.  
-  **Yearly Dynamics:** 2006–2007 marked a peak in average sale prices before the dip.

### Tools Used
- **PostgreSQL (Aiven)** — SQL-based EDA & aggregation queries  
- **Python (Pandas, Psycopg2)** — automation and data loading  

##  Data Sources
All datasets used in this project are publicly viewable via Google Drive.

| Dataset | Description | Download Link |
|----------|--------------|----------------|
| Real_Estate_Sales_2001-2022_GL.csv | Full Connecticut real estate sales data (2001-2022) | [View on Drive](https://drive.google.com/file/d/1D-pjbsFmRFcPjBzEFhdIB896lGhTYRW3/view) |
| sample_real_estate.csv | Lightweight 1 000-row sample for quick testing | [View on Drive](https://drive.google.com/file/d/1G-k8sBVFbNfT9ibshvrNE4_BO10n84bS/view) |
| yearly_sales.csv | Yearly total sales summary | [View on Drive](https://drive.google.com/file/d/1o8OF3dhJw89d0nJHswpOWC7EPAYaQYOK/view) |
| top_towns.csv | Top 10 towns by average sale price | [View on Drive](https://drive.google.com/file/d/1uNlQ02T8XNQrKnhLLUyW6rFWqZmkJ9Qp/view) |
| avg_sale_trend.csv | Average sale trend by year | [View on Drive](https://drive.google.com/file/d/1QDGBE0roR_Cc9NoXt0_ouDqPEUS_FDu2/view) |
| corr_assessed_sale.csv | Correlation between assessed value and sale price | [View on Drive](https://drive.google.com/file/d/1LNG-niEvqQC_BgsvaZ5uCXb66C6iPr-W/view) |
| median_property_type.csv | Median sale price by property type | [View on Drive](https://drive.google.com/file/d/1oboZ-SKlGj4exCK-FXAniKSPdaRicDkr/view) |
| top_residential_types.csv | Top residential types by average price | [View on Drive](https://drive.google.com/file/d/1Isn0JsmpgRhqBvsmQm-siLIcaeB0KDg2/view) |

## ⚡️ Reproducibility Guide

Follow these steps to recreate the database, run the SQL analysis, and generate the reports.

---

### 1️⃣ Create a PostgreSQL Database (Aiven or Local)

You can use one of the following methods:

- **Aiven for PostgreSQL (cloud-hosted):** [aiven.io/postgresql](https://aiven.io/postgresql)  
- **Local setup (Homebrew or Docker):**
  ```bash
  createdb real_estate_db
2️⃣ Load the Dataset

Run the Python ETL script:


python src/load_aiven.py --csv data/raw/sample_real_estate.csv --table real_estate_sales


This script will:

- Read and clean the CSV

- Remove duplicates

- Create a PostgreSQL table named real_estate_sales

- Insert all rows using efficient psycopg2 bulk inserts

3️⃣ Run the SQL Analysis

Execute all SQL analysis queries:

psql -d real_estate_db -f src/queries.sql

Export query results to CSV files:

\copy (SELECT * FROM yearly_sales) TO 'reports/summary/yearly_sales.csv' WITH CSV HEADER;




