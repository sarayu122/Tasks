Simple RAG System using LangChain + ChromaDB


📌 Overview

This project is a Retrieval-Augmented Generation (RAG) system built using LangChain, OpenAI-compatible LLMs (via OpenRouter), HuggingFace embeddings, and Chroma vector database.
It allows you to:
Paste your own knowledge text
Automatically split it into chunks
Store embeddings in a local vector database (ChromaDB)
Ask questions based only on the provided knowledge
Get AI-generated answers grounded in retrieved context


⚙️ Tech Stack
Python 🐍
LangChain 🦜🔗
OpenRouter API (OpenAI-compatible LLM)
HuggingFace Embeddings (sentence-transformers/all-MiniLM-L6-v2)
ChromaDB (Vector Database)
dotenv (Environment variable management)


📂 Project Structure
project/
│
├── main.py               # Your main RAG application script
├── chroma_db/            # Auto-generated vector database (created after first run)
├── .env                  # Stores API keys
└── README.md


🔑 Setup Instructions

1. Clone or Download Project
git clone <your-repo-url>
cd <project-folder>

2. Install Dependencies
pip install langchain langchain-openai langchain-community langchain-chroma
pip install chromadb sentence-transformers python-dotenv

3. Setup Environment Variables
Create a .env file:
OPENROUTER_API_KEY=your_api_key_here
Get your API key from:
https://openrouter.ai/

🚀 How to Run
Run the script:
python main.py

🧾 How It Works

1. Input Knowledge
You paste your text into the terminal.
Example input used:

Artificial Intelligence refers to the broad field of computer science focused on building intelligent systems capable of performing tasks that typically require human intelligence...
Machine Learning is a subset of AI that learns from data...
Overfitting occurs when a model learns noise instead of patterns...

Type END to finish input.

2. Text Chunking
The text is split into smaller chunks using:
Chunk size: 500 characters
Overlap: 50 characters
This improves retrieval accuracy.

3. Embedding + Storage
Each chunk is converted into vector embeddings using:
sentence-transformers/all-MiniLM-L6-v2
Stored in ChromaDB locally (chroma_db/ folder).

4. Question Answering (RAG Pipeline)
When you ask a question:
Relevant chunks are retrieved using similarity search
Context is passed into the LLM
Model generates answer ONLY from provided context

💬 Example Usage
Input:
What is Machine Learning?
Output:
Machine Learning is a subset of Artificial Intelligence that enables systems to learn from data and improve predictions without being explicitly programmed.

🧠 Key Features
🔍 Context-aware question answering
📦 Local vector database (ChromaDB)
🤖 LLM-powered responses
📚 Custom knowledge ingestion
⚡ Fast semantic retrieval
⚠️ Limitations

📈 Future Improvements
Add document/PDF upload support
Web UI (Streamlit / React frontend)
Multi-document knowledge base
Streaming responses
Better reranking of retrieved chunks

🏁 Conclusion
This project demonstrates a simple but powerful RAG pipeline, combining embeddings, vector search, and LLM reasoning to build a private knowledge-based chatbot.