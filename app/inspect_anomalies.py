
from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = PROJECT_ROOT / "data" / "Online Retail.xlsx"


def inspect_anomalies():
    df = pd.read_excel(DATASET_PATH)

    print("\n--- NEGATIVE QUANTITIES ---")
    print(
        df.loc[df["Quantity"] < 0]
        .head(10)
        .to_string(index=False)
    )

    print("\n--- CANCELLATION INVOICES ---")
    invoice_text = df["InvoiceNo"].astype(str).str.strip()
    cancellations = invoice_text.str.startswith("C", na=False)

    print(
        df.loc[cancellations]
        .head(10)
        .to_string(index=False)
    )

    print("\n--- NEGATIVE UNIT PRICES ---")
    print(
        df.loc[df["UnitPrice"] < 0]
        .to_string(index=False)
    )


if __name__ == "__main__":
    inspect_anomalies()
