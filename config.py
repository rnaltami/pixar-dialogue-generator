import os
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("Missing OpenAI API Key. Check your .env file.")
