from openai import OpenAI

from config import OPENROUTER_API_KEY, OPENROUTER_MODEL


if not OPENROUTER_API_KEY:
    raise RuntimeError("OPENROUTER_API_KEY is missing from the environment")


client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)


def generate_answer(system_prompt: str, user_prompt: str) -> str:
    response = client.chat.completions.create(
        model=OPENROUTER_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content.strip()