import pandas as pd
from pymongo import MongoClient

URL = "https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/store_sales.csv"

def extract():
    return pd.read_csv(URL)

def transform(df):
    return df.copy()

def load(df):
    client = MongoClient("mongodb://localhost:27017/")
    collection = client["store_sales_db"]["store_sales"]

    collection.insert_many(df.to_dict("records"))

    print(f"Loaded {len(df)} documents into MongoDB")
    client.close()

def run_etl():
    print("ETL Started")

    try:
        data = extract()
        print(f"Extracted: {len(data)} rows")

        data = transform(data)
        print("Transformed successfully")

        load(data)
        print("ETL Completed Successfully")

    except Exception as e:
        print(f"ETL Failed: {e}")

if __name__ == "__main__":
    run_etl()