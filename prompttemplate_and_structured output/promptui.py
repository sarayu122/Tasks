import sys
sys.stdout.reconfigure(encoding='utf-8')

from dotenv import load_dotenv
import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

st.set_page_config(
    page_title="Content Analyzer",
    page_icon="✦",
    layout="wide",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Outfit:wght@300;400;500&display=swap');

:root {
    --bg:        #f8f5f0;
    --surface:   #ffffff;
    --surface2:  #faf8f5;
    --ink:       #1c1917;
    --ink2:      #57534e;
    --ink3:      #a8a29e;
    --rose:      #c4a4a4;
    --rose-deep: #9e7070;
    --sage:      #9ab5a4;
    --sage-deep: #6b8f7c;
    --sand:      #d4c5a9;
    --sand-deep: #a8956e;
    --line:      rgba(28, 25, 23, 0.08);
}

*, *::before, *::after { box-sizing: border-box; }

html, body, [data-testid="stAppViewContainer"] {
    background: var(--bg) !important;
    font-family: 'Outfit', sans-serif;
    color: var(--ink);
}
[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"] {
    background: transparent !important;
    display: none !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--sand); border-radius: 2px; }

/* ── Hero ── */
.hero {
    text-align: center;
    padding: 4rem 1rem 2.5rem;
    position: relative;
}
.hero-eyebrow {
    font-family: 'Outfit', sans-serif;
    font-size: 0.65rem;
    font-weight: 500;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: var(--rose-deep);
    margin-bottom: 1rem;
}
.hero h1 {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(2.8rem, 6vw, 4.4rem);
    font-weight: 300;
    font-style: italic;
    color: var(--ink);
    margin: 0 0 0.6rem;
    line-height: 1.05;
    letter-spacing: -0.5px;
}
.hero h1 span {
    font-style: normal;
    font-weight: 600;
    color: var(--rose-deep);
}
.hero-sub {
    font-size: 0.85rem;
    font-weight: 300;
    color: var(--ink3);
    letter-spacing: 0.3px;
}
.hero-divider {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.75rem;
    margin: 2rem auto 0;
    max-width: 220px;
}
.hero-divider-line {
    flex: 1;
    height: 1px;
    background: var(--line);
}
.hero-divider-dot {
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: var(--rose);
}

/* ── Input area ── */
.input-wrapper {
    max-width: 680px;
    margin: 0 auto;
    padding: 0 1rem;
}
.input-label {
    font-size: 0.7rem;
    font-weight: 500;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: var(--ink3);
    margin-bottom: 0.5rem;
}
[data-testid="stTextArea"] textarea {
    font-family: 'Outfit', sans-serif !important;
    font-size: 0.9rem !important;
    font-weight: 300 !important;
    line-height: 1.75 !important;
    border-radius: 4px !important;
    border: 1px solid var(--line) !important;
    border-bottom: 2px solid var(--sand) !important;
    background: var(--surface) !important;
    color: var(--ink) !important;
    padding: 1.1rem 1.25rem !important;
    transition: border-color 0.25s, box-shadow 0.25s !important;
    box-shadow: 0 2px 20px rgba(28,25,23,0.04) !important;
    resize: none !important;
}
[data-testid="stTextArea"] textarea:focus {
    border-bottom-color: var(--rose-deep) !important;
    box-shadow: 0 4px 24px rgba(158,112,112,0.12) !important;
    outline: none !important;
}
[data-testid="stTextArea"] textarea::placeholder {
    color: var(--ink3) !important;
    font-style: italic;
}

/* ── Analyze button ── */
[data-testid="stButton"] button {
    background: var(--ink) !important;
    color: #f8f5f0 !important;
    border: none !important;
    border-radius: 2px !important;
    padding: 0.65rem 2.8rem !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 0.72rem !important;
    font-weight: 500 !important;
    letter-spacing: 3px !important;
    text-transform: uppercase !important;
    transition: background 0.2s, transform 0.15s !important;
    box-shadow: none !important;
    cursor: pointer !important;
}
[data-testid="stButton"] button:hover {
    background: var(--rose-deep) !important;
    transform: translateY(-1px) !important;
}
[data-testid="stButton"] button:active {
    transform: translateY(0) !important;
}

/* ── Results section header ── */
.results-header {
    text-align: center;
    padding: 3.5rem 1rem 0.5rem;
}
.results-header p {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.05rem;
    font-style: italic;
    font-weight: 300;
    color: var(--ink3);
    margin: 0;
}

/* ── Cards grid ── */
.cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 1px;
    background: var(--line);
    border: 1px solid var(--line);
    max-width: 1100px;
    margin: 2rem auto;
    border-radius: 6px;
    overflow: hidden;
}

.card {
    background: var(--surface);
    padding: 1.4rem 1.5rem;
    transition: background 0.2s;
    animation: fadeIn 0.5s ease both;
    position: relative;
}
.card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 2px;
    height: 100%;
    background: var(--accent, transparent);
    opacity: 0.6;
}
.card:hover {
    background: var(--surface2);
}

.card-label {
    font-size: 0.6rem;
    font-weight: 500;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: var(--ink3);
    margin-bottom: 0.6rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.card-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--line);
}
.card-value {
    font-family: 'Outfit', sans-serif;
    font-size: 0.88rem;
    font-weight: 300;
    color: var(--ink);
    line-height: 1.7;
    white-space: pre-wrap;
}

/* Wide cards */
.card-wide {
    grid-column: 1 / -1;
}

/* Summary cards */
.card-summary-detailed .card-label { color: var(--sage-deep); }
.card-summary-detailed::before { background: var(--sage-deep) !important; opacity: 1 !important; }
.card-summary-detailed { background: linear-gradient(to right, rgba(154,181,164,0.04), transparent); }

.card-summary-quick .card-label { color: var(--rose-deep); }
.card-summary-quick::before { background: var(--rose-deep) !important; opacity: 1 !important; }
.card-summary-quick { background: linear-gradient(to right, rgba(196,164,164,0.06), transparent); }

.card-summary-detailed .card-value,
.card-summary-quick .card-value {
    font-size: 0.92rem;
    line-height: 1.85;
    color: var(--ink2);
}

/* ── Keyword tags ── */
.tag-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin-top: 0.2rem;
}
.tag {
    font-size: 0.72rem;
    font-weight: 400;
    letter-spacing: 0.3px;
    padding: 0.2rem 0.65rem;
    border-radius: 2px;
    background: var(--surface2);
    border: 1px solid var(--line);
    color: var(--ink2);
    transition: border-color 0.2s, color 0.2s;
}
.tag:hover {
    border-color: var(--rose);
    color: var(--rose-deep);
}

/* ── Spinner override ── */
[data-testid="stSpinner"] {
    text-align: center;
    color: var(--ink3) !important;
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    font-size: 1.05rem;
}

/* ── Expander ── */
.stExpander {
    border: 1px solid var(--line) !important;
    border-radius: 4px !important;
    margin: 1.5rem auto !important;
    max-width: 1100px !important;
    background: var(--surface) !important;
}
.stExpander summary {
    font-size: 0.72rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    color: var(--ink3) !important;
}

/* ── Warning ── */
[data-testid="stAlert"] {
    border-radius: 4px !important;
    border: 1px solid var(--sand) !important;
    background: rgba(212,197,169,0.12) !important;
    font-size: 0.85rem !important;
}

/* ── Footer ornament ── */
.footer-ornament {
    text-align: center;
    padding: 2rem 0 3rem;
    color: var(--ink3);
    font-size: 0.75rem;
    letter-spacing: 1.5px;
}
.footer-ornament span {
    color: var(--rose);
    font-size: 1rem;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(8px); }
    to   { opacity: 1; transform: translateY(0); }
}
</style>
""", unsafe_allow_html=True)

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

@st.cache_resource
def get_model():
    return ChatOpenAI(
        model="openai/gpt-oss-120b:free",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1"
    )

model = get_model()
prompt_template = ChatPromptTemplate.from_template(template)

def parse_sections(text: str) -> dict:
    sections = {}
    parts = text.split("==============================")
    i = 1
    while i < len(parts) - 1:
        key = parts[i].strip()
        value = parts[i + 1].strip()
        if key:
            sections[key] = value
        i += 2
    return sections

SECTION_ACCENTS = {
    "TITLE":                       "#c4a4a4",
    "CONTENT TYPE":                "#d4c5a9",
    "GENRE":                       "#9ab5a4",
    "SUB-GENRE":                   "#9ab5a4",
    "SETTING":                     "#a4b8c4",
    "TIME PERIOD":                 "#c4b8a4",
    "MAIN CHARACTERS":             "#c4a4a4",
    "PROTAGONIST":                 "#c4a4b8",
    "MAIN CONFLICT":               "#c4a4a4",
    "MISSION / OBJECTIVE":         "#a4c4b4",
    "STAKES":                      "#c4b4a4",
    "THEMES":                      "#b4a4c4",
    "EMOTIONS / MOOD":             "#c4a4a4",
    "TONE":                        "#a4b4c4",
    "IMPORTANT OBJECTS":           "#c4c4a4",
    "SCIENTIFIC / TECHNICAL CONCEPTS": "#a4c4c4",
    "IMPORTANT LOCATIONS":         "#a4b8c4",
    "KEYWORDS":                    "#d4c5a9",
    "DETAILED SUMMARY":            "#6b8f7c",
    "QUICK SUMMARY":               "#9e7070",
}

SECTION_ORDER = [
    "TITLE", "CONTENT TYPE", "GENRE", "SUB-GENRE",
    "SETTING", "TIME PERIOD", "MAIN CHARACTERS", "PROTAGONIST",
    "MAIN CONFLICT", "MISSION / OBJECTIVE", "STAKES", "THEMES",
    "EMOTIONS / MOOD", "TONE", "IMPORTANT OBJECTS",
    "SCIENTIFIC / TECHNICAL CONCEPTS", "IMPORTANT LOCATIONS", "KEYWORDS",
    "DETAILED SUMMARY", "QUICK SUMMARY"
]

WIDE_SECTIONS = {
    "MAIN CHARACTERS", "THEMES", "KEYWORDS",
    "DETAILED SUMMARY", "QUICK SUMMARY", "SCIENTIFIC / TECHNICAL CONCEPTS"
}

TAG_SECTIONS = {"KEYWORDS", "THEMES", "EMOTIONS / MOOD"}

st.markdown("""
<div class="hero">
    <div class="hero-eyebrow">Simple · Fast · Smart</div>
    <h1>Content <span>Analyzer</span></h1>
    <p class="hero-sub">Paste any paragraph and get a clear, detailed breakdown in seconds</p>
    <div class="hero-divider">
        <div class="hero-divider-line"></div>
        <div class="hero-divider-dot"></div>
        <div class="hero-divider-line"></div>
    </div>
</div>
""", unsafe_allow_html=True)

col_l, col_c, col_r = st.columns([1, 5, 1])
with col_c:
    st.markdown('<div class="input-label">Your text</div>', unsafe_allow_html=True)
    para = st.text_area(
        "",
        placeholder="A story, article, synopsis, book excerpt — anything you'd like to understand more deeply…",
        height=160,
        label_visibility="collapsed"
    )
    btn_cols = st.columns([4, 2, 4])
    with btn_cols[1]:
        analyze = st.button("Analyze", use_container_width=True)

if analyze:
    if not para.strip():
        st.warning("Please enter some text before analyzing.")
    else:
        with st.spinner("Reading your content…"):
            final_prompt = prompt_template.invoke({"text": para})
            response = model.invoke(final_prompt)
            raw = response.content

        sections = parse_sections(raw)

        st.markdown("<div class='results-header'><p>Here is what I found</p></div>", unsafe_allow_html=True)

    
        st.markdown("<div class='cards-grid'>", unsafe_allow_html=True)

        for section_name in SECTION_ORDER:
            value = sections.get(section_name, "Not Mentioned")
            accent = SECTION_ACCENTS.get(section_name, "#c4a4a4")
            wide_class = "card-wide" if section_name in WIDE_SECTIONS else ""

            extra_class = ""
            if section_name == "DETAILED SUMMARY":
                extra_class = "card-summary-detailed"
            elif section_name == "QUICK SUMMARY":
                extra_class = "card-summary-quick"

            if section_name in TAG_SECTIONS and value != "Not Mentioned":
                items = [t.strip() for t in value.replace("\n", ",").split(",") if t.strip()]
                tags_html = "".join(f'<span class="tag">{t}</span>' for t in items)
                value_html = f'<div class="tag-list">{tags_html}</div>'
            else:
                value_html = f'<div class="card-value">{value}</div>'

            st.markdown(f"""
            <div class="card {wide_class} {extra_class}" style="--accent: {accent};">
                <div class="card-label">{section_name.lower()}</div>
                {value_html}
            </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="footer-ornament">
            <span>✦</span>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("view raw output"):
            st.text(raw)