import sys
sys.stdout.reconfigure(encoding='utf-8')

from dotenv import load_dotenv
import os
import streamlit as st

from pydantic import BaseModel, Field, EmailStr
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

class CustomerSupportTicket(BaseModel):
    """
    Structured schema for customer support extraction.
    """

    name: str = Field(
        description="Customer full name"
    )

    email: EmailStr = Field(
        description="Customer email address"
    )

    order_id: str = Field(
        description="Customer order ID"
    )

    issue_type: str = Field(
        description="Type of issue faced by customer"
    )


model = ChatOpenAI(
    model="openai/gpt-oss-120b:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

structured_model = model.with_structured_output(
    CustomerSupportTicket
)


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert AI information extraction assistant.

Your task:
Extract structured information from unstructured customer messages.

Instructions:
- Extract only accurate information.
- Do not invent data.
- Detect issue_type clearly.
- Return properly structured fields.
- If any value is missing, return "Not Mentioned".
"""
    ),

    (
        "human",
        "{text}"
    )
])


user_input = st.text_area(
    "Enter Customer Support Message",
    height=250,
    placeholder="Paste long customer support text here..."
)


if st.button("Extract Structured Data"):

    if not user_input.strip():

        st.warning("Please enter some text.")

    else:

        try:

            final_prompt = prompt.invoke({
                "text": user_input
            })

            result = structured_model.invoke(
                final_prompt
            )

            st.success("Extraction Successful ✅")

            st.subheader("Validated Structured Output")

            st.json(
                result.model_dump()
            )

            st.subheader("Key-Value Format")

            st.write(f"**Name:** {result.name}")
            st.write(f"**Email:** {result.email}")
            st.write(f"**Order ID:** {result.order_id}")
            st.write(f"**Issue Type:** {result.issue_type}")

        except Exception as e:

            st.error(f"Error: {e}")


