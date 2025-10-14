#!/usr/bin/env python3
import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def connect_db():
    return psycopg2.connect(
        host=os.getenv("PG_HOST"),
        port=os.getenv("PG_PORT"),
        dbname=os.getenv("PG_DB"),
        user=os.getenv("PG_USER"),
        password=os.getenv("PG_PASSWORD"),
        sslmode=os.getenv("PG_SSLMODE")
    )

def run_query(conn, query):
    return pd.read_sql_query(query, conn)

def main():
    conn = connect_db()
    print("✅ Connected to Aiven PostgreSQL")

    os.makedirs("reports/summary", exist_ok=True)

    queries = {
        "yearly_sales": """
            SELECT list_year, COUNT(*) AS num_sales
            FROM real_estate_sales
            GROUP BY list_year
            ORDER BY list_year;
        """,
        "top_towns": """
            SELECT town, ROUND(AVG(sale_amount), 2) AS avg_price
            FROM real_estate_sales
            WHERE sale_amount > 0
            GROUP BY town
            ORDER BY avg_price DESC
            LIMIT 15;
        """,
        "avg_sale_trend": """
            SELECT list_year, ROUND(AVG(sale_amount), 2) AS avg_sale
            FROM real_estate_sales
            WHERE sale_amount > 0
            GROUP BY list_year
            ORDER BY list_year;
        """,
        "corr_assessed_sale": """
            SELECT ROUND(CAST(CORR(assessed_value, sale_amount) AS numeric), 3) AS corr_ratio
            FROM real_estate_sales
            WHERE assessed_value > 0 AND sale_amount > 0;
        """,
        "median_property_type": """
    SELECT property_type,
           ROUND(
               CAST(
                   PERCENTILE_CONT(0.5) 
                   WITHIN GROUP (ORDER BY sale_amount) 
                   AS numeric
               ), 2
           ) AS median_sale
    FROM real_estate_sales
    WHERE sale_amount > 0
    GROUP BY property_type
    ORDER BY median_sale DESC;
""",

        "top_residential_types": """
            SELECT residential_type, COUNT(*) AS total_sales
            FROM real_estate_sales
            GROUP BY residential_type
            ORDER BY total_sales DESC
            LIMIT 10;
        """
    }

    for name, query in queries.items():
        print(f"\n🔹 Running query: {name}")
        df = run_query(conn, query)
        df.to_csv(f"reports/summary/{name}.csv", index=False)
        print(df.head(10))

    conn.close()
    print("\n✅ EDA complete. Results saved in 'reports/summary/'")

if __name__ == "__main__":
    main()
