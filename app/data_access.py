import csv

def load_business_data():

    with open("data/business_data.csv",newline="") as file:

        data = csv.DictReader(file)

        return list(data)

def normalise_month(month):

    month = month.strip()
    month = month.lower()

    month_alias = {
        "jan":"January",
        "mar":"March",
        "feb":"February"
    }

    if month in month_alias:
        return month_alias[month]

    return month

def normalise_metric(metric):

    metric = metric.lower()
    metric = metric.strip()

    metri_alias = {
        "revenues":"revenue",
        "expense":"expenses",
        "customer":"customers"
    }

    if metric in metri_alias:
        return metri_alias[metric]

    return metric


def get_month_data(month):

    month = normalise_month(month)

    data = load_business_data()

    for row in data:

        if row["month"].lower() == month.lower():
            return row 

    return None
