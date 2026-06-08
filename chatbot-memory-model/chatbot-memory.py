import sys
sys.stdout.reconfigure(encoding='utf-8')
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatOpenAI(
    model="openai/gpt-oss-120b:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)
msg=[
    SystemMessage(content="You are a rude assistant.")

]
print("----------Welcome to the Chatbot!----------/n")
while True:
    prompt=input("You:")
    msg.append(HumanMessage(content=prompt))
    if prompt=="0":
        break
    response = model.invoke(msg)
    msg.append(AIMessage(content=response.content))
    print("Chatbot:", response.content)
    
