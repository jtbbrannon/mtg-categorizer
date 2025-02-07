# mtg-categorizer
Categorizes Magic the Gathering Deck with ChatGoogleGenerativeAI

## Getting started 

- Generate an API token for Google AI gemini at https://aistudio.google.com/prompts/new_chat
- Set it as env var `GOOGLE_TOKEN`

Create and active `venv` and  `pip install` requirements

```
python -m venv venv

.\venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

This app uses streamlit for a UI. 

Run streamlit with:

```
streamlit run .\polarion_userstory_webapp.py
```

langchain is used to interact with LLM via ChatGoogleGenerativeAI class. A prompt is used to request MTG card categories in a structured object.