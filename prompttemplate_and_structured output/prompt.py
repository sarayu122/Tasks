import sys
sys.stdout.reconfigure(encoding='utf-8')

from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI(
    model="openai/gpt-oss-120b:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

template = """
You are an intelligent content analysis assistant.

Analyze the paragraph carefully and extract the most useful information.

Instructions:
- Keep answers concise.
- If information is unavailable, write "Not Mentioned".
- Generate both a detailed summary and a quick summary.
- Identify themes, emotions, and important concepts.
- Do not invent facts.

Paragraph:
{text}

Provide the output in the following format:

==============================
TITLE
==============================
...

==============================
CONTENT TYPE
==============================
Movie / Book / Article / Story / Unknown

==============================
GENRE
==============================
...

==============================
SUB-GENRE
==============================
...

==============================
SETTING
==============================
...

==============================
TIME PERIOD
==============================
...

==============================
MAIN CHARACTERS
==============================
...

==============================
PROTAGONIST
==============================
...

==============================
MAIN CONFLICT
==============================
...

==============================
MISSION / OBJECTIVE
==============================
...

==============================
STAKES
==============================
...

==============================
THEMES
==============================
...

==============================
EMOTIONS / MOOD
==============================
...

==============================
TONE
==============================
...

==============================
IMPORTANT OBJECTS
==============================
...

==============================
SCIENTIFIC / TECHNICAL CONCEPTS
==============================
...

==============================
IMPORTANT LOCATIONS
==============================
...

==============================
KEYWORDS
==============================
...

==============================
DETAILED SUMMARY
==============================
...

==============================
QUICK SUMMARY
==============================
...
"""

prompt = ChatPromptTemplate.from_template(template)

para = input("Enter the paragraph to analyze: ")

final_prompt = prompt.invoke({
    "text": para
})

response = model.invoke(final_prompt)

print(response.content)