import pandas as pd
from rich.console import Console

console = Console()

def clean_data(df):
    before = len(df)
    console.print("[magenta] Cleaning data…[/magenta]")

    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)
    df.dropna(subset=["product_name", "price"], inplace=True)

    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df.dropna(subset=["price"], inplace=True)

    df.sort_values(by="price", ascending=False, inplace=True)

    after = len(df)
    removed = before - after

    console.print(f"✨ Cleaned: {after} rows | ❌ Removed: {removed}")

    return df
