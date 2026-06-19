# Document RAG

Simple Flask-based document Q&A using Pinecone, Hugging Face embeddings, and OpenRouter.

## What it does

1. Upload a PDF, TXT, or DOCX file.
2. Chunk the document and embed the chunks with `sentence-transformers/all-MiniLM-L6-v2`.
3. Store the chunks in a Pinecone index using a namespace for that upload.
4. Redirect to a chat page where questions are answered from only that document.

## Setup

1. Create a virtual environment and install dependencies from `requirements.txt`.
2. Copy `.env.example` to `.env` and fill in your keys.
3. Make sure your Pinecone index exists or let the app create it automatically.

## Run

From the `document_RAG` folder:

```bash
python app.py
```

Open the app in your browser, upload a document, then ask questions on the chat page.

## Notes

- The app stores the uploaded document chunks in Pinecone under a document-specific namespace.
- If the answer is not in the document context, the assistant will say so instead of guessing.