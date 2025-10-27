# pipeline.py
from etl.extract import extract_data
from etl.transform import clean_data
from etl.load import load_data

input_path = "data/raw/sales.csv"
output_path = "data/processed/cleaned_products.csv"

df = extract_data(input_path)
df = clean_data(df)
load_data(df, output_path)
