from agents import function_tool
from app.data_access import get_month_data,normalise_metric,normalise_month
from app.api_calling import find_user
from app.schemas import UserRequest
from pydantic import ValidationError

@function_tool
def get_revenue(month):
    """This tool returns the revenue for a particular month"""

    row = get_month_data(month)

    if row is None:

        return f"The revenue for the month of {month.title()} is not available"

    return f"The revenue for the month of {month.title()} is {row['revenue']}"

@function_tool
def get_expenses(month):
    """This tool returns the expenses for a particular month"""

    row = get_month_data(month)

    if row is None:

        return f"The expenses for the month of {month.title()} is not available"

    return f"The expenses for the month of {month.title()} is {row['expenses']}"

@function_tool
def get_customer_count(month):
    """This tool returns the customer count for a particular month"""

    row = get_month_data(month)

    if row is None:

        return f"The customer count for the month of {month.title()} is not available"

    return f"The customer count for the month of {month.title()} is {row['customers']}"

@function_tool
def compare_growth(month1,month2,metric):
    """This tool returns the growth between any two months """

    month1 = normalise_month(month1)
    month2 = normalise_month(month2)
    metric = normalise_metric(metric)

    allowed_metrics = {"revenue", "expenses", "customers"}

    if metric not in allowed_metrics:
        return f"Invalid metric: {metric}"

    first_month = get_month_data(month1)
    second_month = get_month_data(month2)

    if first_month is None or second_month is None:
        return f"The {metric.title()} is not available betweent these months"
    
    if first_month[metric] == "" or second_month[metric] == "":
        return f"The {metric} data is missing for one or both months."
    
    first_value = float(first_month[metric])
    second_value = float(second_month[metric])

    if first_value == 0:
        return "Cannot calculate percentage growth from a starting value of zero."

    difference = second_value - first_value

    percentage_growth = (difference/first_value)*100

    return (
    f"The percentage growth in {metric} from "
    f"{month1.title()} to {month2.title()} is "
    f"{percentage_growth:.2f}%."
)

@function_tool
def get_external_user(user_id):

    try:
        
        UserRequest(user_id=user_id)

    except ValidationError:

        return {
            "success":False,
            "data":None,
            "error":"The user ID is invalid",
            "error_type":"validation_error"
        }


    result = find_user(user_id)

    if result.success == False:
        return {
            "error":result.error,
            "error_type":result.error_type
        }

    return {
        "data":result.data
    }

@function_tool
def calculate_profit(month: str):
    """Calculate the profit for a particular month."""

    row = get_month_data(month)

    if row is None:
        return f"Business data for {month.title()} is not available."

    revenue = float(row["revenue"])
    expenses = float(row["expenses"])

    profit = revenue - expenses

    return f"The profit for {month.title()} is {profit:.2f}."














