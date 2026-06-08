# LangChain OpenRouter Embeddings Example

## Overview
This project demonstrates how to use LangChain's `OpenAIEmbeddings` with OpenRouter to generate text embeddings using the `text-embedding-3-large` model.

## Setup Requirements
- Python 3.8+
- `langchain-openai`
- `python-dotenv`

## Installation

```bash
pip install langchain-openai python-dotenv
```

## Environment Variables

Create a `.env` file in your project root and add:

```
OPENROUTER_API_KEY=your_api_key_here
```

## Code Explanation

This script:
1. Loads environment variables using `dotenv`
2. Initializes OpenAIEmbeddings with OpenRouter endpoint
3. Generates embeddings for a sample sentence
4. Prints the embedding vector

### Python Code

```python
from dotenv import load_dotenv
import os
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

vector = embeddings.embed_query("You are going to learn GenAI")
print(vector)
```

## Run the Project

```bash
python your_script.py
```

## Output
A high-dimensional embedding vector representing the input text.
