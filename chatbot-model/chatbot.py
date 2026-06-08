import sys
sys.stdout.reconfigure(encoding='utf-8')
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(
    model="openai/gpt-oss-120b:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

response = model.invoke("give me a comedy joke in telugu ")

print(response.content)
