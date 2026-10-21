from pathlib import Path
import pandas as pd

dataset_path = Path("data") / "Online Retail.xlsx"

df = pd.read_excel(dataset_path)

negative_quantity = df[df["Quantity"] < 0]

print(len(negative_quantity))

print(negative_quantity["InvoiceNo"].astype(str).str.startswith("C").sum())