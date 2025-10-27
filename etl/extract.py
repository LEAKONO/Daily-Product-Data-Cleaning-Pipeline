# etl/extract.py
import pandas as pd

def extract_data(input_file):
    print(f"Extracting data from {input_file}")
    return pd.read_csv(input_file)
