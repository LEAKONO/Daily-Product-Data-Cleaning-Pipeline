import pandas as pd
from rich.console import Console

console = Console()

def extract_data(input_file):
    console.print(f"[cyan]{input_file}[/cyan]")
    df = pd.read_csv(input_file)
    console.print(f"[yellow]📊 Extracted {len(df)} rows[/yellow]")
    return df
