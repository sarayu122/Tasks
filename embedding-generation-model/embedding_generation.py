
from dotenv import load_dotenv
import os
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)
vector=embeddings.embed_query("You are going to learn GenAI")
print(vector)