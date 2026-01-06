# importing the os module
import os

# importing load_dotenv function from dotenv module
from dotenv import load_dotenv # type: ignore
load_dotenv()

# Getting and printing API key
api_key = os.getenv("GEMINI_API_KEY")
print(f"API_KEY: {api_key}")