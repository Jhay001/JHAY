import os
from dotenv import load_dotenv # type: ignore
from google import genai
load_dotenv()

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="How does AI works?"
)
print(response.text)