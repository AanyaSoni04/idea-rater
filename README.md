# Idea Rater

An AI-powered startup idea evaluation platform that conducts interactive, multi-turn conversations to assess startup ideas — asking targeted clarifying questions and returning structured, actionable feedback.

## Features

- **Conversational evaluation** — engages in a multi-turn Q&A flow, asking clarifying questions before scoring an idea (rather than a single-shot rating)
- **AI-driven scoring** — powered by Google Gemini 3.5 Flash for question generation and idea assessment
- **Structured, validated output** — JSON response validation ensures consistent, parseable feedback across every conversation turn
- **Secure API key handling** — credentials are managed via environment variables, never hard-coded
- **Persistent session state** — Streamlit session-state management keeps multi-step conversations stable across interactions
- **Modular architecture** — clean separation of concerns for easier maintenance and extension

## Tech Stack

- **Language:** Python
- **Frontend:** Streamlit
- **AI/LLM:** Google Gemini API (Gemini 3.5 Flash)
- **Data format:** JSON
- **Version control:** Git

## Getting Started


### Installation

```bash
# Clone the repository
git clone https://github.com/AanyaSoni04/idea-rater.git
cd idea-rater

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root and add your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

> **Note:** Update the variable name above to match whatever your code actually reads (e.g. `GOOGLE_API_KEY`) — check your config/env loading file to confirm.

### Running the App

```bash
streamlit run app.py
```

> Update `app.py` to your actual entry-point filename if different.

Then open the local URL Streamlit prints in your terminal (typically `http://localhost:8501`).

## How It Works

1. The user describes their startup idea.
2. The app asks targeted clarifying questions to fill in gaps (market, users, differentiation, etc.).
3. Once enough context is gathered, Gemini scores the idea and generates structured feedback.
4. Results are validated and returned in a consistent JSON format for display.

## Project Structure

```
idea-rater/
├── app.py              # Main Streamlit application
├── requirements.txt     # Python dependencies
├── .env                 # API keys (not committed)
└── ...
```

> Update this tree to reflect your actual file layout.

## Future Improvements

- Add persistent storage for evaluated ideas
- Support additional LLM providers
- Export feedback reports as PDF


## Author

**Aanya Soni**
GitHub: [@AanyaSoni04](https://github.com/AanyaSoni04)
