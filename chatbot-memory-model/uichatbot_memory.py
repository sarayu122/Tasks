import sys
sys.stdout.reconfigure(encoding='utf-8')

from dotenv import load_dotenv
import os
import streamlit as st

from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

load_dotenv()

st.set_page_config(
    page_title="💀 SAVAGE AI",
    page_icon="💀",
    layout="centered"
)


st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(135deg, #0f0f1a, #1a0033, #2b0057);
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

/* Title */
.main-title {
    text-align: center;
    font-size: 3rem;
    font-weight: 800;
    color: #d946ef;
    text-shadow: 0px 0px 25px #d946ef;
    margin-bottom: 0;
}

.sub-title {
    text-align: center;
    color: #c084fc;
    margin-top: 0;
    margin-bottom: 30px;
    font-size: 1.1rem;
}

/* Chat container */
.chat-box {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    padding: 18px;
    border-radius: 18px;
    margin-bottom: 15px;
    backdrop-filter: blur(12px);
    box-shadow: 0 0 20px rgba(217, 70, 239, 0.25);
}

/* User message */
.user-msg {
    color: #ffffff;
    font-size: 16px;
}

/* AI message */
.ai-msg {
    color: #f5d0fe;
    font-size: 16px;
    line-height: 1.6;
}

/* Input box */
.stTextInput > div > div > input {
    background-color: #140021;
    color: white;
    border: 2px solid #9333ea;
    border-radius: 14px;
    padding: 12px;
    font-size: 16px;
}

/* Button */
.stButton button {
    background: linear-gradient(90deg, #9333ea, #d946ef);
    color: white;
    border: none;
    border-radius: 14px;
    padding: 12px 20px;
    font-weight: bold;
    font-size: 16px;
    width: 100%;
    transition: 0.3s;
    box-shadow: 0 0 15px rgba(217,70,239,0.5);
}

.stButton button:hover {
    transform: scale(1.03);
    box-shadow: 0 0 25px rgba(217,70,239,0.9);
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-thumb {
    background: #9333ea;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


model = ChatOpenAI(
    model="openai/gpt-oss-120b:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


system_prompt = """
You are SAVAGE AI — brutally honest, wickedly witty, and unfiltered.

You tell people what they NEED to hear, not what they want.
You roast weak ideas with surgical precision,
use dark humor naturally,
and have zero patience for vague nonsense.

You're not mean —
you're the brilliant friend who keeps it 100.

Short, punchy replies.
No sugarcoating.
Ever.
"""


if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=system_prompt)
    ]


st.markdown(
    """
    <h1 class="main-title">💀 SAVAGE AI 💀</h1>
    <p class="sub-title">
    Brutal honesty. Zero emotional cushioning.
    </p>
    """,
    unsafe_allow_html=True
)


for msg in st.session_state.messages[1:]:

    if isinstance(msg, HumanMessage):
        st.markdown(
            f"""
            <div class="chat-box">
                <div class="user-msg">
                    <b>🧠 You:</b><br>{msg.content}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    elif isinstance(msg, AIMessage):
        st.markdown(
            f"""
            <div class="chat-box">
                <div class="ai-msg">
                    <b>💀 SAVAGE:</b><br>{msg.content}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


user_input = st.chat_input("Type something painfully stupid...")

if user_input:

    st.session_state.messages.append(
        HumanMessage(content=user_input)
    )

    response = model.invoke(st.session_state.messages)

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    st.rerun()