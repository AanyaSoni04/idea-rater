import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

DEFAULT_MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")


def call_llm(
    prompt: str,
    system: str = "",
    model: str | None = None,
    max_tokens: int = 2000,
) -> str:
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    model_name = model or DEFAULT_MODEL

    full_prompt = prompt
    if system:
        full_prompt = f"{system}\n\n{prompt}"

    response = client.models.generate_content(
        model=model_name,
        contents=full_prompt,
    )

    return response.text