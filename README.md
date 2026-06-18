# ✦ Tasks Workspace — AI, ML & NLP Projects Collection

This workspace is a collection of small, focused projects for learning and
prototyping in AI, machine learning, and NLP. Each project lives in its own
folder and includes a README describing purpose, how to run it, and key
implementation notes.

---

## Projects (short summaries)

- `chatbot-memory-model/` — Memory-enabled Streamlit chatbot (Savage AI).
- `chatbot-model/` — Streamlit chatbot demo with a custom personality (RudeBot).
- `embedding-generation-model/` — Embeddings example using LangChain + OpenRouter.
- `Evaluation-metrics/` — NumPy implementations of binary classification metrics.
- `house_predict/` — Housing price experiments (AmesHousing dataset).
- `Iris_Classification/` — Iris dataset classification with Logistic Regression,
	Decision Tree, and Random Forest examples.
- `movie_review/` — IMDB sentiment classification scripts.
- `multi-layer-nndl/` — 2-layer neural network (PyTorch) example.
- `prompttemplate_and_structured output/` — Streamlit apps for content analysis
	and structured information extraction.
- `single-layer-nndl/` — Single-layer (NumPy) feedforward neural net example.
- `text_rag/` — Retrieval-Augmented Generation (RAG) pipeline with ChromaDB and
	a small UI in `text_rag/text_rag_ui/`.

Open a project's own `README.md` for full details and project-specific commands.

---

## Quick global setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows PowerShell
.\.venv\Scripts\activate
```

2. Install only what you need per project, for example:

```bash
pip install -r text_rag/requirements.txt
```

3. If a project requires an API key (OpenRouter), set it with an env var or
	 a local `.env` file (do not commit secrets):

```bash
export OPENROUTER_API_KEY=your_api_key_here  # macOS / Linux
setx OPENROUTER_API_KEY "your_api_key_here"  # Windows (persist)
```

---

## How to run selected projects

- Text RAG (CLI):

```bash
python text_rag/txtrag.py
```

- Text RAG UI (Flask):

```bash
python text_rag/text_rag_ui/textragui.py
# open http://127.0.0.1:5000
```

- Iris classification examples:

```bash
python Iris_Classification/iris_sklearn.py
python Iris_Classification/iris_loaddata.py
```

- NYC Taxi cleaning & viz (see project README for thresholds):

```bash
python "NYC taxi dataset cleaning/clean_data.py"
python "NYC taxi dataset cleaning/visualization.py"
```

---

## Recommendations & next steps

- Check each project's `requirements.txt` before installing dependencies.
- Keep API keys out of source control; use `.env` or environment variables.
- I can:
	- regenerate missing per-project `README.md` files,
	- create `requirements.txt` for projects that lack them,
	- add a consolidated `run_all.sh`/`run_all.ps1` to demonstrate quick runs.

If you want, tell me which of the options above to do next and I'll implement it.