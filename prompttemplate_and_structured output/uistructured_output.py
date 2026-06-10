import sys
sys.stdout.reconfigure(encoding='utf-8')

from dotenv import load_dotenv
import os
import streamlit as st

from pydantic import BaseModel, Field, EmailStr
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

st.set_page_config(
    page_title="Data Extraction Agent",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background-color: #0D1117;
}

#MainMenu, footer, header { visibility: hidden; }

.app-header {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 1.5rem 0 1rem;
    border-bottom: 1px solid #1E2736;
    margin-bottom: 2rem;
}
.app-header h1 {
    font-size: 18px;
    font-weight: 600;
    color: #E8EDF5;
    margin: 0;
}
.app-header p {
    font-size: 13px;
    color: #6B7896;
    margin: 0;
}

.panel-label {
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #6B7896;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 8px;
}
.panel-label::before {
    content: '';
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #4F8EF7;
    display: inline-block;
}

.stTextArea textarea {
    background-color: #111827 !important;
    border: 1px solid #1E2736 !important;
    border-radius: 10px !important;
    color: #E8EDF5 !important;
    font-size: 13px !important;
    line-height: 1.75 !important;
    padding: 14px !important;
    resize: none !important;
    font-family: 'Inter', sans-serif !important;
}
.stTextArea textarea:focus {
    border-color: #4F8EF7 !important;
    box-shadow: 0 0 0 3px rgba(79,142,247,0.12) !important;
}
.stTextArea textarea::placeholder { color: #3D4F6E !important; }
.stTextArea label { display: none !important; }

.stButton > button {
    width: 100%;
    background: #4F8EF7 !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 13px 20px !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    letter-spacing: 0.02em !important;
    transition: opacity 0.15s, transform 0.1s !important;
    margin-top: 0.75rem !important;
}
.stButton > button:hover { opacity: 0.87 !important; }
.stButton > button:active { transform: scale(0.98) !important; }

.field-card {
    background: #111827;
    border: 1px solid #1E2736;
    border-radius: 10px;
    padding: 12px 14px;
    margin-bottom: 10px;
}
.field-card-key {
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.09em;
    text-transform: uppercase;
    color: #6B7896;
    margin-bottom: 5px;
}
.field-card-val {
    font-size: 14px;
    font-weight: 500;
    color: #E8EDF5;
    word-break: break-all;
}
.field-card-val.muted {
    color: #3D4F6E;
    font-style: italic;
    font-weight: 400;
}

.json-block {
    background: #111827;
    border: 1px solid #1E2736;
    border-radius: 10px;
    padding: 14px;
    font-family: 'SF Mono', 'Fira Code', monospace;
    font-size: 12px;
    line-height: 1.75;
    color: #6B7896;
    white-space: pre;
    overflow-x: auto;
    margin-top: 14px;
}
.json-key { color: #4F8EF7; }
.json-str { color: #4ADE80; }

.status-success {
    display: flex; align-items: center; gap: 8px;
    font-size: 12px; color: #4ADE80;
    padding: 10px 0 0;
    border-top: 1px solid #1E2736;
    margin-top: 1rem;
}
.status-error {
    display: flex; align-items: center; gap: 8px;
    font-size: 12px; color: #F87171;
    padding: 10px 0 0;
    border-top: 1px solid #1E2736;
    margin-top: 1rem;
}

.empty-state {
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    gap: 10px; padding: 3rem 1rem;
    color: #3D4F6E; font-size: 13px; text-align: center;
}
.empty-icon { font-size: 32px; opacity: 0.5; }

.char-count {
    font-size: 11px; color: #3D4F6E;
    text-align: right; margin-top: 6px;
}

@keyframes scanline {
    0%   { opacity: 0; transform: scaleX(0); }
    20%  { opacity: 0.6; transform: scaleX(1); }
    80%  { opacity: 0.6; transform: scaleX(1); }
    100% { opacity: 0; transform: scaleX(1); }
}
.scan-bar {
    height: 1.5px;
    background: #4F8EF7;
    border-radius: 1px;
    transform-origin: left;
    animation: scanline 1.6s ease-in-out forwards;
    margin: 4px 0 12px;
}
</style>
""", unsafe_allow_html=True)


# ── Header ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="app-header">
    <div>
        <h1>Data Extraction Agent</h1>
        <p>AI-powered structured data extraction from customer messages</p>
    </div>
</div>
""", unsafe_allow_html=True)


# ── Schema ──────────────────────────────────────────────────────────────────
class CustomerSupportTicket(BaseModel):
    name: str = Field(description="Customer full name")
    email: EmailStr = Field(description="Customer email address")
    order_id: str = Field(description="Customer order ID")
    issue_type: str = Field(description="Type of issue faced by customer")


# ── Model ───────────────────────────────────────────────────────────────────
@st.cache_resource
def get_model():
    model = ChatOpenAI(
        model="openai/gpt-oss-120b:free",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1"
    )
    return model.with_structured_output(CustomerSupportTicket)


prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are an expert AI information extraction assistant.

Your task:
Extract structured information from unstructured customer messages.

Instructions:
- Extract only accurate information.
- Do not invent data.
- Detect issue_type clearly.
- Return properly structured fields.
- If any value is missing, return "Not Mentioned".
"""),
    ("human", "{text}")
])

EXAMPLE_TEXT = (
    "Hi team,\n"
    "My name is Rahul Sharma. I placed an order yesterday but the payment failed.\n"
    "Order ID is ORD-45678.\n"
    "My email is rahul.sharma@gmail.com.\n"
    "Please help resolve this issue as soon as possible.\n"
    "Thanks\n"
    "Rahul"
)


# ── Layout ──────────────────────────────────────────────────────────────────
left, right = st.columns(2, gap="medium")

with left:
    st.markdown('<div class="panel-label">Customer message</div>', unsafe_allow_html=True)

    # Buttons BEFORE textarea so session_state can be set before widget renders
    btn_col1, btn_col2 = st.columns([2, 1])
    with btn_col1:
        extract_clicked = st.button("✦  Extract structured data", key="extract_btn")
    with btn_col2:
        if st.button("📋  Try example", key="example_btn"):
            st.session_state["msg_input"] = EXAMPLE_TEXT
            st.rerun()

    user_input = st.text_area(
        label="",
        height=300,
        placeholder="Paste or type a customer support message here…",
        key="msg_input"
    )

    char_count = len(user_input) if user_input else 0
    st.markdown(f'<div class="char-count">{char_count} characters</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="panel-label">Extracted fields</div>', unsafe_allow_html=True)

    result_placeholder = st.empty()

    if not extract_clicked:
        result_placeholder.markdown("""
<div class="empty-state">
    <div class="empty-icon">🔍</div>
    <div>Extracted fields will appear here</div>
</div>
""", unsafe_allow_html=True)

    if extract_clicked:
        if not user_input.strip():
            result_placeholder.markdown("""
<div class="empty-state">
    <div class="empty-icon">✏️</div>
    <div>Please enter a customer message first.</div>
</div>
""", unsafe_allow_html=True)
        else:
            result_placeholder.markdown('<div class="scan-bar"></div>', unsafe_allow_html=True)

            with st.spinner(""):
                try:
                    structured_model = get_model()
                    final_prompt = prompt.invoke({"text": user_input})
                    result = structured_model.invoke(final_prompt)

                    def field_html(label, value, icon):
                        is_missing = str(value).strip().lower() in ("not mentioned", "none", "")
                        val_class = "field-card-val muted" if is_missing else "field-card-val"
                        display = value if not is_missing else "Not mentioned"
                        return f"""
<div class="field-card">
    <div class="field-card-key">{icon} &nbsp; {label}</div>
    <div class="{val_class}">{display}</div>
</div>"""

                    data = result.model_dump()

                    json_lines = "{\n"
                    items = list(data.items())
                    for i, (k, v) in enumerate(items):
                        comma = "," if i < len(items) - 1 else ""
                        json_lines += f'  <span class="json-key">"{k}"</span>: <span class="json-str">"{v}"</span>{comma}\n'
                    json_lines += "}"

                    html = ""
                    html += field_html("Name",       result.name,       "👤")
                    html += field_html("Email",      result.email,      "✉️")
                    html += field_html("Order ID",   result.order_id,   "🏷️")
                    html += field_html("Issue type", result.issue_type, "⚠️")
                    html += f'<div class="json-block">{json_lines}</div>'
                    html += '<div class="status-success">✓ &nbsp; Extraction complete</div>'

                    result_placeholder.markdown(html, unsafe_allow_html=True)

                except Exception as e:
                    result_placeholder.markdown(f"""
<div class="empty-state">
    <div class="empty-icon">⚠️</div>
    <div>Something went wrong.</div>
</div>
<div class="status-error">✕ &nbsp; {str(e)[:120]}</div>
""", unsafe_allow_html=True)