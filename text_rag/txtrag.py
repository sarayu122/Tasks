import sys
sys.stdout.reconfigure(encoding='utf-8')

from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# RAG Imports
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "chroma_db")

print("BASE_DIR:", BASE_DIR)
print("DB_PATH:", db_path)

model = ChatOpenAI(
    model="openai/gpt-oss-120b:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# --------------------------
# User Text Input
# --------------------------

print("\nPaste your knowledge text.")
print("When finished type END on a new line.\n")

lines = []

while True:
    line = input()
    if line.strip() == "END":
        break
    lines.append(line)

text = "\n".join(lines)

# --------------------------
# Split Text
# --------------------------

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_text(text)

print(f"\nCreated {len(chunks)} chunks")

# --------------------------
# Embeddings
# --------------------------

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# --------------------------
# Vector Store
# --------------------------

vectorstore = Chroma.from_texts(
    texts=chunks,
    embedding=embedding_model,
    persist_directory=db_path
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

print("\nKnowledge Base Ready!")

# --------------------------
# Q&A Loop
# --------------------------

prompt = ChatPromptTemplate.from_template("""
Answer the question only from the provided context.

Context:
{context}

Question:
{question}

Answer:
""")

while True:

    question = input("\nAsk Question (type exit to quit): ")

    if question.lower() == "exit":
        break

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    chain = prompt | model

    response = chain.invoke({
        "context": context,
        "question": question
    })

    print("\nAnswer:")
    print(response.content)