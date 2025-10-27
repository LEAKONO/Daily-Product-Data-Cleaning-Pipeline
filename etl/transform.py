# etl/transform.py
import pandas as pd

def clean_data(df):
    print("Transforming data...")

    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

    df = df.dropna(subset=["product_name", "price"])

    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df = df.dropna(subset=["price"])

    df = df.sort_values(by="price", ascending=False)

    return df
