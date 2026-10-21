from app.orchestration import route_request


def test_revenue_routes_to_agent():
    state = {
        "question": "What is our revenue?",
        "task": "revenue",
        "answer": ""
    }

    assert route_request(state) == "agent"


def test_profit_routes_to_agent():
    state = {
        "question": "Calculate our profit",
        "task": "profit",
        "answer": ""
    }

    assert route_request(state) == "agent"


def test_unknown_routes_to_reject():
    state = {
        "question": "Tell me a joke",
        "task": "unknown",
        "answer": ""
    }

    assert route_request(state) == "reject"


def test_unexpected_task_routes_to_reject():
    state = {
        "question": "Analyse everything",
        "task": "unexpected_task",
        "answer": ""
    }

    assert route_request(state) == "reject"

def test_missing_task_routes_to_reject():
    state = {
        "question": "What is our revenue?",
        "answer": ""
    }

    assert route_request(state) == "reject"


def test_none_task_routes_to_reject():
    state = {
        "question": "What is our revenue?",
        "task": None,
        "answer": ""
    }

    assert route_request(state) == "reject"