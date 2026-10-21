from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
from agents import set_default_openai_api, set_default_openai_client


load_dotenv()

client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

set_default_openai_client(client)
set_default_openai_api("chat_completions")