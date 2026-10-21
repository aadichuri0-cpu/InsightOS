from agents import Runner
from app.agent import agent

from agents import Runner
from typing import TypedDict

class WorkflowState(TypedDict):

    task : str
    question: str
    answer: str
    


def classify_request(question: str) -> str:

    question = question.lower()

    if "revenue" in question:
        return "revenue"

    elif "expenses" in question:
        return "expenses"

    elif "customers" in question:
        return "customers"

    elif "growth" in question:
        return "growth"

    elif "id" in question:
        return "user_id"

    elif "profit" in question:
        return "profit"

    else:
        return "unknown"

def classify_node(state: WorkflowState) -> WorkflowState:
    task = classify_request(state['question'])
    state['task'] = task
    return state


def route_request(state: WorkflowState) -> str:

    task = state.get('task')

    supported_tasks = {
        "revenue",
        "expenses",
        "customers",
        "growth",
        "profit",
        "user_id"
    }

    if task in supported_tasks:
        return "agent"

    return "reject"


async def agent_node(state: WorkflowState) -> WorkflowState:
    result = await Runner.run(agent,state['question'])
    state['answer'] = result.final_output
    return state


def reject_node(state: WorkflowState) -> WorkflowState:
    state['answer'] = ("I can currently help with business analytics"
                        "questions supported by InsightOS")
    return state

async def run_workflow(question: str) -> str:
    state: WorkflowState = {
        "question": question,
        "answer": "",
        "task": ""
    }

    state = classify_node(state)

    next_node = route_request(state)

    print("Selected route:", next_node)

    if next_node == "reject":
        state = reject_node(state)
    elif next_node == "agent":
        state = await agent_node(state)

    print("Final workflow state:", state)
    return state['answer']



