from etl.extract import extract_data
from etl.transform import clean_data
from etl.load import load_data

from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from time import perf_counter, sleep

console = Console()

console.print(Panel.fit("[bold blue] ETL PIPELINE — PRODUCT CLEANING[/bold blue]"))

start = perf_counter()

steps = [
    ("Extracting data...", extract_data),
    ("Transforming data...", clean_data),
    ("Loading data...", load_data),
]

df = None
input_path = "data/raw/sales.csv"
output_path = "data/processed/cleaned_products.csv"

for message, step in track(steps, description="Processing"):
    sleep(0.4)  
    if "Extract" in message:
        df = step(input_path)
    elif "Transform" in message:
        df = step(df)
    else:
        step(df, output_path)

stop = perf_counter()
console.print(Panel.fit(f"[bold green]DONE in {stop - start:.2f}s[/bold green]"))
