
from app.transaction_data_access import (
    load_transactions,
    classify_transactions,
    get_gross_sales_summary,
)
from app.transaction_data_access import get_monthly_gross_sales



def main():
    original = load_transactions()
    classified = classify_transactions(original)
    summary = get_gross_sales_summary()

    print("Original rows:", len(original))
    print("Classified rows:", len(classified))
    print("\nGross sales summary:")
    for key, value in summary.items():
        print(f"{key}: {value}")

    # Classification must not delete any source rows.
    assert len(original) == len(classified)

    # Every included gross-sales line must have
    # positive quantity, positive price, and no C-prefix.
    included = classified[classified["is_gross_sales_line"]]

    assert (included["Quantity"] > 0).all()
    assert (included["UnitPrice"] > 0).all()
    assert not included["is_cancellation_invoice"].any()

    print("\nBasic transaction-data checks passed!")

    print("\nDecember 2010:")
    print(get_monthly_gross_sales(2010, 12))

    print("\nJanuary 2011:")
    print(get_monthly_gross_sales(2011, 1))
if __name__ == "__main__":
    main()
