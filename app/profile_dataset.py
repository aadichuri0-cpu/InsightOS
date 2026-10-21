
from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = PROJECT_ROOT / "data" / "Online Retail.xlsx"


def profile_dataset():
    df = pd.read_excel(DATASET_PATH)

    # 1. Inspect quantities and prices
    print("\n--- QUANTITY CHECK ---")
    print("Zero quantities:", (df["Quantity"] == 0).sum())
    print("Negative quantities:", (df["Quantity"] < 0).sum())

    print("\n--- UNIT PRICE CHECK ---")
    print("Zero prices:", (df["UnitPrice"] == 0).sum())
    print("Negative prices:", (df["UnitPrice"] < 0).sum())

    # 2. Identify cancellation-like invoice numbers
    invoice_text = df["InvoiceNo"].astype(str).str.strip()
    cancellation_rows = invoice_text.str.startswith("C", na=False)

    print("\n--- CANCELLATION CHECK ---")
    print("Rows with C-prefixed invoice numbers:", cancellation_rows.sum())
    print("Unique cancellation invoices:",
          df.loc[cancellation_rows, "InvoiceNo"].nunique())

    # 3. Inspect date range
    print("\n--- DATE RANGE ---")
    print("Earliest transaction:", df["InvoiceDate"].min())
    print("Latest transaction:", df["InvoiceDate"].max())

    # 4. Inspect missing values
    print("\n--- MISSING VALUES ---")
    print(df.isnull().sum())

    # 5. Calculate row-level line value
    df["LineValue"] = df["Quantity"] * df["UnitPrice"]

    print("\n--- LINE VALUE CHECK ---")
    print("Total line value:", round(df["LineValue"].sum(), 2))
    print("Negative line values:", (df["LineValue"] < 0).sum())


if __name__ == "__main__":
    profile_dataset()
