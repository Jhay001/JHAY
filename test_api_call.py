import os
from dotenv import load_dotenv # type: ignore
from google import genai
load_dotenv()

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

# Model generates a response
response = client.models.generate_content(
    model="gemini-3-flash-preview", 
    contents="Give me a warm welcome back to using you"
)
print(response.text)