from agents import Agent
from app.tools import get_revenue,get_customer_count,get_expenses,compare_growth,get_external_user,calculate_profit


agent = Agent(
    name="InsightOS",
    instructions="You are a business assistant",
    model="gemini-3.5-flash-lite",
    tools=[
        get_revenue,
        get_expenses,
        get_customer_count,
        compare_growth,
        get_external_user,
        calculate_profit
    ]
)

