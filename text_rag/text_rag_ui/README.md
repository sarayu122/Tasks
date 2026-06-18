# Text RAG UI

This folder contains the browser-based user interface for the Text RAG project. It includes a small Flask server that serves the frontend and proxies requests to OpenRouter, plus the HTML and JavaScript that drive the chat experience.

## What this folder includes

- [textragui.py](textragui.py): Flask app that serves the UI and handles `/api/ask`
- [index.html](index.html): main page layout and styling
- [script.js](script.js): frontend logic for chat history, text input, and Q&A
- `.env`: optional local environment file for your API key

## How it works

1. The browser loads `index.html` and `script.js`.
2. The page lets you paste knowledge text, split it into chunks, and start a chat.
3. The frontend sends prompts to the Flask backend in `textragui.py`.
4. The backend forwards those prompts to OpenRouter and returns the answer.

## Prerequisites

- Python 3.10 or newer
- An `OPENROUTER_API_KEY` value in your environment or `.env` file
- Internet access for the OpenRouter API call

## Setup

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in this folder if you do not already have one:

```env
OPENROUTER_API_KEY=your_api_key_here
```

## Run the UI

Start the Flask app from this folder:

```bash
python textragui.py
```

Then open the local address shown in the terminal, usually:

```text
http://127.0.0.1:5000
```

## Using the UI

1. Enter a title for the knowledge base if you want one.
2. Paste or type your source text into the textbox.
3. Click **Analyze & Start Asking**.
4. Ask questions in the chat input.
5. Use **Clear Text** to reset the source text.
6. Use the sidebar history to reopen previous chats or delete them.

## Frontend behavior

- Text is split into chunks before questions are answered.
- Chat history is saved in the browser with `localStorage`.
- The sidebar shows previously created chats.
- The current chat can be cleared from the top bar.

## Backend behavior

- `textragui.py` serves `index.html` and `script.js`.
- The `/api/ask` route forwards prompts to OpenRouter.
- The response is returned as JSON to the frontend.

## Notes

- This README is only for `text_rag_ui`.
- The command-line RAG script in the parent `text_rag` folder is documented separately.