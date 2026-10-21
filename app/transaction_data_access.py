
#This is used for working with files and folder paths
from pathlib import Path
#This imports pandas to read excel file
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = PROJECT_ROOT / "data" / "Online Retail.xlsx"


def load_transactions() -> pd.DataFrame:
    """Load the original transaction-level retail dataset."""
    if not DATASET_PATH.exists():
        raise FileNotFoundError(
            f"Transaction dataset not found: {DATASET_PATH}"
        )

    df = pd.read_excel(DATASET_PATH)

    required_columns = {
        "InvoiceNo",
        "StockCode",
        "Description",
        "Quantity",
        "InvoiceDate",
        "UnitPrice",
        "CustomerID",
        "Country",
    }

    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Dataset is missing required columns: "
            f"{sorted(missing_columns)}"
        )

    return df


def classify_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """Add analytical classifications without deleting source rows."""
    result = df.copy()

    invoice_numbers = (
        result["InvoiceNo"].astype(str).str.strip()
    )

    result["is_cancellation_invoice"] = (
        invoice_numbers.str.startswith("C", na=False)
    )

    result["is_accounting_adjustment"] = (
        result["UnitPrice"] < 0
    )

    result["is_return_or_negative_quantity"] = (
        result["Quantity"] < 0
    )

    result["line_value"] = (
        result["Quantity"] * result["UnitPrice"]
    )

    result["is_gross_sales_line"] = (
        (result["Quantity"] > 0)
        & (result["UnitPrice"] > 0)
        & (~result["is_cancellation_invoice"])
    )

    result["gross_sales_value"] = (
        result["line_value"].where(
            result["is_gross_sales_line"], 0
        )
    )

    return result


def get_gross_sales_summary() -> dict:
    """Return the initial gross-sales metric and its row counts."""
    df = classify_transactions(load_transactions())

    return {
        "metric": "gross_product_sales",
        "currency": "GBP",
        "gross_sales": round(
            float(df["gross_sales_value"].sum()), 2
        ),
        "total_rows": int(len(df)),
        "gross_sales_rows": int(
            df["is_gross_sales_line"].sum()
        ),
        "cancellation_invoice_rows": int(
            df["is_cancellation_invoice"].sum()
        ),
        "negative_quantity_rows": int(
            df["is_return_or_negative_quantity"].sum()
        ),
        "accounting_adjustment_rows": int(
            df["is_accounting_adjustment"].sum()
        ),
    }


def get_monthly_gross_sales(year: int, month: int) -> dict:
    """Calculate gross product sales for a specific month."""
    if not 1 <= month <= 12:
        raise ValueError("month must be between 1 and 12")

    df = classify_transactions(load_transactions())

    selected = df[
        (df["InvoiceDate"].dt.year == year)
        & (df["InvoiceDate"].dt.month == month)
    ]

    return {
        "year": year,
        "month": month,
        "currency": "GBP",
        "gross_sales": round(
            float(selected["gross_sales_value"].sum()), 2
        ),
        "transaction_rows": int(len(selected)),
    }
