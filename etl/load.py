# etl/load.py

def load_data(df, output_file):
    print(f"Loading data to {output_file}")
    df.to_csv(output_file, index=False)
    print("Load complete!")
