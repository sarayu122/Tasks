# ✦ Tasks Workspace — AI, ML & NLP Projects Collection

This workspace contains a set of small projects, experiments, and utilities for
learning and prototyping in AI, machine learning, and natural language
processing. Each project is kept in its own folder and may include a
`requirements.txt` or README where appropriate.

---

## Current Top-Level Folders

The repository root contains the following project folders (listed with a
short description when available):

- `chatbot-memory-model/` — memory-enabled chatbot experiments
- `chatbot-model/` — basic chatbot experiments and UI
- `embedding-generation-model/` — utilities for generating text embeddings
- `Evaluation-metrics/` — evaluation utilities and experiments
- `house_predict/` — housing price prediction experiments (AmesHousing.csv)
- `Iris_Classification/` — Iris dataset classification examples
- `movie_review/` — sentiment analysis on movie reviews (IMDB dataset)
- `multi-layer-nndl/` — multi-layer neural network example
- `prompttemplate_and_structured output/` — prompt template and structured-output examples
- `single-layer-nndl/` — single-layer neural network example
- `text_rag/` — RAG-related scripts and a small UI app

If a folder contains a README, prefer opening that README for per-project
instructions.

---

## Quick Setup (global)

These are general suggestions — each project may have its own requirements.

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.\\.venv\\Scripts\\activate  # Windows PowerShell
```

2. Install only the packages you need for a project. Example:

```bash
pip install -r text_rag/requirements.txt
```

3. Set environment variables (if required by a project):

```bash
export OPENROUTER_API_KEY=your_api_key_here  # macOS / Linux
setx OPENROUTER_API_KEY "your_api_key_here"  # Windows (persist)
```

---

## How to run each project

Open the folder for the project you want to run and look for `README.md`,
`requirements.txt`, or example run commands. A few examples from this workspace:

- CLI RAG script:

```bash
python text_rag/txtrag.py
```

- Start the small UI for Text RAG (Flask server):

```bash
python text_rag/text_rag_ui/textragui.py
# then open http://127.0.0.1:5000 in your browser
```

- Run the Iris classification example:

```bash
python Iris_Classification/iris_sklearn.py
```

---

## Notes and recommendations

- Many projects include their own dependency lists: check each project's
	`requirements.txt` before installing.
- Keep sensitive keys out of source control — use a local `.env` file or your
	system environment variables.
- If you want a consolidated setup for one project, open its folder and follow
	the project-specific README.

---

If you'd like, I can:

- Add or refresh missing per-project `README.md` files.
- Create a short index file with direct run commands for each project.
- Generate `requirements.txt` files for projects that lack them.

Tell me which option you'd like next.