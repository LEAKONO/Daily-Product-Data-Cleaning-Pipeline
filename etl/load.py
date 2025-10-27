from rich import print
from rich.panel import Panel

def load_data(df, output_file):
    df.to_csv(output_file, index=False)
    print(Panel.fit(f"[green]Saved: {output_file}\n Rows: {len(df)}[/green]"))
