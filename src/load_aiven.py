#!/usr/bin/env python3
import os
import argparse
import psycopg2
import pandas as pd
from dotenv import load_dotenv
from psycopg2.extras import execute_values
import numpy as np

# Load .env variables
load_dotenv()

def connect_db():
    """Establish connection to Aiven PostgreSQL."""
    return psycopg2.connect(
        host=os.getenv("PG_HOST"),
        port=os.getenv("PG_PORT"),
        dbname=os.getenv("PG_DB"),
        user=os.getenv("PG_USER"),
        password=os.getenv("PG_PASSWORD"),
        sslmode=os.getenv("PG_SSLMODE")
    )

def main():
    ap = argparse.ArgumentParser(description="Load Real Estate dataset into Aiven PostgreSQL")
    ap.add_argument("--csv", required=True, help="Path to the CSV dataset")
    ap.add_argument("--table", required=True, help="Target PostgreSQL table name")
    args = ap.parse_args()

    # 🧩 Read CSV safely
    df = pd.read_csv(args.csv, low_memory=False)
    print("✅ Loaded CSV:", df.shape)

    # 🧹 Remove duplicates by Serial Number
    if "Serial Number" in df.columns:
        df = df.drop_duplicates(subset=["Serial Number"])
        print("✅ After removing duplicates:", df.shape)

    # 🪄 Clean column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("[^0-9a-zA-Z_]", "", regex=True)
    )

    # 🗓️ Convert date column to datetime
    if "date_recorded" in df.columns:
        df["date_recorded"] = pd.to_datetime(df["date_recorded"], errors="coerce")

    # 💡 Convert numeric columns
    for col in ["assessed_value", "sale_amount", "sales_ratio"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # 🔁 Convert datetime64 to object, replace NaT and NaN with None
    df = df.astype(object)
    df = df.replace({np.nan: None, pd.NaT: None, "NaT": None})

    # 🚀 Connect to database
    conn = connect_db()
    cur = conn.cursor()

    # Drop and recreate table
    cur.execute(f"DROP TABLE IF EXISTS {args.table};")
    create_sql = f"""
    CREATE TABLE {args.table} (
        serial_number BIGINT PRIMARY KEY,
        list_year INT,
        date_recorded DATE,
        town VARCHAR(100),
        address VARCHAR(255),
        assessed_value NUMERIC(14,2),
        sale_amount NUMERIC(14,2),
        sales_ratio NUMERIC(10,4),
        property_type VARCHAR(100),
        residential_type VARCHAR(100),
        non_use_code VARCHAR(50),
        assessor_remarks TEXT,
        opm_remarks TEXT,
        location VARCHAR(100)
    );
    """
    cur.execute(create_sql)
    conn.commit()
    print("✅ Table created in PostgreSQL")

    # 🚚 Bulk insert
    cols = list(df.columns)
    records = [tuple(x) for x in df.to_numpy()]
    query = f"INSERT INTO {args.table} ({', '.join(cols)}) VALUES %s"
    execute_values(cur, query, records, page_size=5000)  # safer batch inserts
    conn.commit()

    cur.close()
    conn.close()
    print(f"✅ Successfully inserted {len(df)} rows into table `{args.table}`")

if __name__ == "__main__":
    main()
