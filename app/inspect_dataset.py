from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = PROJECT_ROOT / "data" / "Online Retail.xlsx"


def inspect_dataset():
    df = pd.read_excel(DATASET_PATH)

    print("\n--- FIRST 5 ROWS ---")
    print(df.head())

    print("\n--- DATASET SHAPE ---")
    print(df.shape)

    print("\n--- COLUMN NAMES ---")
    print(df.columns.tolist())

    print("\n--- DATA TYPES ---")
    print(df.dtypes)

    print("\n--- MISSING VALUES ---")
    print(df.isnull().sum())


if __name__ == "__main__":
    inspect_dataset()