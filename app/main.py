
from config import *
from agents import Runner
import asyncio
from orchestration import run_workflow

async def main():

    question = input("Ask InsightOS. a question:")

    result = await run_workflow(question)

    print(result)


if __name__ == "__main__":

    asyncio.run(main())