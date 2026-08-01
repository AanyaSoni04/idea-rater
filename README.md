# 💡 AI Idea Rater

An AI-powered web application that evaluates startup and product ideas through an interactive conversation instead of a single prompt.

Instead of immediately rating an idea, the AI first asks clarifying questions to understand the target users, distribution strategy, differentiation, and business model. It then generates structured feedback including pros, cons, reasoning, and an overall score.

---

## Features

- Interactive multi-step AI conversation
- AI-generated clarifying questions
- Structured evaluation with:
  - Pros
  - Cons
  - Overall score (1–10)
  - Detailed reasoning
- Modern Streamlit interface
- Google Gemini 3.5 Flash integration
- Robust JSON parsing and validation
- Secure API key management using environment variables

---

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- Google GenAI SDK
- python-dotenv
- Git

---

## Project Structure

```
idea-rater/
│
├── app.py              # Streamlit UI
├── idea_logic.py       # Prompt construction and JSON parsing
├── llm_client.py       # Gemini API integration
├── test_idea_logic.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## How It Works

1. User enters a startup or product idea.
2. Gemini generates 3–5 clarifying questions.
3. User answers the questions.
4. Gemini evaluates the idea and returns:
   - Pros
   - Cons
   - Score (1–10)
   - Explanation

---

## Installation

```bash
git clone https://github.com/AanyaSoni04/idea-rater.git

cd idea-rater

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key
GEMINI_MODEL=gemini-3.5-flash
```

Run:

```bash
streamlit run app.py
```

---

## Improvements Made

Compared to the original implementation, this version:

- Migrated from OpenAI API to Google Gemini 3.5 Flash
- Updated the LLM integration using the Google GenAI SDK
- Added secure environment-based configuration
- Resolved deprecated model compatibility issues
- Improved API key security with `.gitignore`

---

## Future Improvements

- User authentication
- PDF export
- Idea history
- Analytics dashboard
- Side-by-side idea comparison
- Charts for idea scoring

---

## Screenshots

(Add screenshots here)

---

## License

MIT
