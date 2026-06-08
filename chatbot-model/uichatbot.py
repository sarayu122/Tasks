import sys
sys.stdout.reconfigure(encoding='utf-8')

from dotenv import load_dotenv
import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

st.set_page_config(
    page_title="RudeBot",
    page_icon="😤",
    layout="centered",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Syne:wght@400;700;800&display=swap');

:root {
    --bg: #0d0d0d;
    --surface: #161616;
    --border: #2a2a2a;
    --accent: #ff3c3c;
    --accent2: #ff8c00;
    --text: #e8e8e8;
    --muted: #666;
    --user-bg: #1a1a1a;
    --bot-bg: #1f0000;
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'Space Mono', monospace;
}

[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stSidebar"] { display: none; }

/* Main container */
.main .block-container {
    max-width: 780px;
    padding: 2rem 1.5rem 6rem;
}

/* Title */
.rudbot-title {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 2.4rem;
    color: var(--accent);
    letter-spacing: -1px;
    margin: 0;
    line-height: 1;
}
.rudbot-sub {
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem;
    color: var(--muted);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-top: 4px;
    margin-bottom: 2rem;
}

/* Chat messages */
.msg-row {
    display: flex;
    margin-bottom: 1.1rem;
    gap: 10px;
    align-items: flex-start;
}
.msg-row.user { flex-direction: row-reverse; }

.avatar {
    width: 32px;
    height: 32px;
    border-radius: 4px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1rem;
    flex-shrink: 0;
    margin-top: 2px;
}
.avatar.bot { background: var(--accent); }
.avatar.user { background: #222; border: 1px solid var(--border); }

.bubble {
    max-width: 82%;
    padding: 0.75rem 1rem;
    border-radius: 2px;
    font-size: 0.87rem;
    line-height: 1.65;
    white-space: pre-wrap;
    word-break: break-word;
}
.bubble.bot {
    background: var(--bot-bg);
    border: 1px solid #3a0000;
    border-left: 3px solid var(--accent);
    color: #ffbfbf;
}
.bubble.user {
    background: var(--user-bg);
    border: 1px solid var(--border);
    color: var(--text);
    text-align: right;
}

/* Thinking indicator */
.thinking {
    color: var(--muted);
    font-size: 0.78rem;
    font-style: italic;
    padding: 0.5rem 0;
    letter-spacing: 1px;
}

/* Input area */
[data-testid="stChatInput"] {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 2px !important;
    color: var(--text) !important;
}
[data-testid="stChatInput"] textarea {
    font-family: 'Space Mono', monospace !important;
    font-size: 0.85rem !important;
    color: var(--text) !important;
    background: transparent !important;
}
[data-testid="stChatInput"] button {
    background: var(--accent) !important;
    border-radius: 2px !important;
}

/* Divider */
hr { border-color: var(--border) !important; }

/* Scrollbar */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 2px; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div>
  <div class="rudbot-title">😤 RudeBot</div>
</div>
<hr/>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a rude assistant.")
    ]

@st.cache_resource
def get_model():
    return ChatOpenAI(
        model="openai/gpt-oss-120b:free",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1"
    )

model = get_model()

for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.markdown(f"""
        <div class="msg-row user">
            <div class="avatar user">🧑</div>
            <div class="bubble user">{msg.content}</div>
        </div>
        """, unsafe_allow_html=True)
    elif isinstance(msg, AIMessage):
        st.markdown(f"""
        <div class="msg-row">
            <div class="avatar bot">🤖</div>
            <div class="bubble bot">{msg.content}</div>
        </div>
        """, unsafe_allow_html=True)

if prompt := st.chat_input("Say something... if you dare"):

    st.markdown(f"""
    <div class="msg-row user">
        <div class="avatar user">🧑</div>
        <div class="bubble user">{prompt}</div>
    </div>
    """, unsafe_allow_html=True)

    st.session_state.messages.append(HumanMessage(content=prompt))

    thinking = st.markdown('<div class="thinking">// bot is thinking (reluctantly)...</div>', unsafe_allow_html=True)

    response = model.invoke(st.session_state.messages)
    reply = response.content

    thinking.empty()

    st.session_state.messages.append(AIMessage(content=reply))

    st.markdown(f"""
    <div class="msg-row">
        <div class="avatar bot">🤖</div>
        <div class="bubble bot">{reply}</div>
    </div>
    """, unsafe_allow_html=True)