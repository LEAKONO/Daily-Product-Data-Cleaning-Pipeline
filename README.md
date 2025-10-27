# A simple ETL pipeline project for cleaning eCommerce product data.
A simple Data Engineering mini-project that extracts messy eCommerce product data, cleans and transforms it, and loads the processed dataset back for analytics use.

This pipeline features a visually engaging terminal UI using the Rich library perfect for demos, screenshots, and LinkedIn posts.

## Overview
| Step	|Description
|-------|-----------
|Extract	|Loads raw CSV product data from the /data/raw directory
| Transform	| Cleans missing values, trims whitespace, fixes price formatting, sorts by highest value
| Load	|Outputs a cleaned CSV to /data/processed
## Project Structure
```plaintext
data/
 ├─ raw/
 │   └─ file.csv
 └─ processed/
     └─ cleaned.csv

etl/
 ├─ extract.py
 ├─ transform.py
 └─ load.py
pipeline.py
requirements.txt
```

## Features

 - Real ETL workflow
 - Animated terminal logs + progress bar
- Data cleaning + validation


##  Tech Stack
| Category	| Tools
|-----------|-------
| Language	Python 3|
|Data Processing |	Pandas
| Logging / CLI  |	Rich
|Storage Format	| CSV
## Setup & Run Pipeline
### Create & activate a virtual environment

### On Linux / macOS
```
python3 -m venv venv
source venv/bin/activate
```
### On Windows (PowerShell)
```
python -m venv venv
venv\Scripts\activate
```
## Run pipeline
```bash
python3 pipeline.py
```
## Future Enhancements

- Logging to /logs

- Retry + error handling

- CLI arguments (--input, --output)

- Airflow / Prefect orchestration

- Docker deployment

- Data validation rules

---
Emmanuel Leakono

leakonoemmanuel3@gmail.com

Data Engineering learner