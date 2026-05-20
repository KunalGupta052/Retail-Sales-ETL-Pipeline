# Retail Sales ETL Pipeline using PySpark

A data engineering project I built to understand how ETL pipelines actually work — not just theory, but end-to-end: reading messy data, cleaning it, running analysis, and saving structured output.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](YOUR_COLAB_LINK_HERE)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![PySpark](https://img.shields.io/badge/PySpark-3.5.1-orange?logo=apachespark)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## Why I built this

I kept seeing "ETL Pipeline" in data engineering job descriptions and wanted to actually build one instead of just reading about it. So I picked a retail sales dataset, wrote the pipeline from scratch using PySpark, and tried to keep it as close to a real workflow as possible.

---

## What it does

- Reads raw retail sales CSV data
- Drops duplicate records and null values
- Calculates revenue per order
- Finds top-selling products and monthly revenue trends
- Saves cleaned data and reports to output folder

---

## Project Structure

```
retail-sales-etl-pipeline/
├── data/
│   └── sales_data.csv        # input data
├── output/                   # generated after running
│   ├── cleaned_sales.csv
│   ├── top_products.csv
│   └── monthly_sales.csv
├── etl_pipeline.py
├── requirements.txt
└── README.md
```

---

## Sample Data

| order_id | product | category | quantity | price | order_date |
|----------|---------|----------|----------|-------|------------|
| 1001 | Laptop | Electronics | 1 | 55000 | 2024-01-05 |
| 1002 | T-Shirt | Clothing | 3 | 499 | 2024-01-10 |
| 1003 | Rice Bag | Grocery | 5 | 250 | 2024-01-15 |

---

## How to run

```bash
git clone https://github.com/KunalGupta052/Retail-Sales-ETL-Pipeline.git
cd Retail-Sales-ETL-Pipeline
pip install -r requirements.txt
python etl_pipeline.py
```

Or just open Colab and run it there — no setup needed:

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1j1iQVggu_F6uDQQpWKOUEx2DGIVr64gP?usp=sharing)

---

## Output files

| File | What's in it |
|------|-------------|
| `cleaned_sales.csv` | Cleaned data with revenue column |
| `top_products.csv` | Products sorted by total revenue |
| `monthly_sales.csv` | Month-wise revenue |

---

## Tech used

Python, PySpark, Pandas, SQL (via Spark), GitHub

---

## What I learned

Honestly the trickiest part wasn't the code — it was understanding *why* each step matters. Like why you drop duplicates before calculating revenue, not after. Small things like that made the project actually useful to build.

---

**Kunal Gupta**
[GitHub](https://github.com/KunalGupta052) · [LinkedIn](https://linkedin.com/in/kunalgupta052) · kunalgupta5627@gmail.com
